import numbers
import random
import time
import zmq

num_bidders = 3
needed_to_win = 3
init_budget = 100
item_types = ["Picasso", "Van_Gogh", "Rembrandt", "Da_Vinci"]
items = random.choices(item_types, k=300)

PORT = 50018
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%d" % PORT)

sample_info = {
    "type": "info",
    "cur_round": 5,
    "item_types": ["Picasso", "Van_Gogh", "Rembrandt", "Da_Vinci"],
    "items": [
        "Rembrandt",
        "Rembrandt",
        "Picasso",
        "Van_Gogh",
        "Rembrandt",
        "Van_Gogh",
        "Van_Gogh",
        "Da_Vinci",
        "Van_Gogh",
        "Picasso",
        "Da_Vinci",
        "Da_Vinci",
    ],
    "self": {
        "budget": 11,
        "item_count": {"Da_Vinci": 0, "Picasso": 0, "Rembrandt": 1, "Van_Gogh": 0},
        "name": "alice",
    },
    "others": [
        {
            "budget": 16,
            "item_count": {"Da_Vinci": 0, "Picasso": 0, "Rembrandt": 2, "Van_Gogh": 0},
            "name": "bob",
        },
        {
            "budget": 21,
            "item_count": {"Da_Vinci": 0, "Picasso": 1, "Rembrandt": 0, "Van_Gogh": 1},
            "name": "charlie",
        },
    ],
}


def init_player_info(player_name):
    return {
        "name": player_name,
        "budget": init_budget,
        "item_count": {it: 0 for it in item_types},
    }


def answer_phase1(req):
    """
    In phase 1, we wait for num_players to connect.
    >>> answer_phase1({"type": "info", "name": "alice"})
    {"type": "wait", "msg": "ok, waiting for all players to join"}
    """
    global players
    player = req["name"]
    if req["type"] == "info":
        if player not in players:
            print(player, "joined")
            players[player] = init_player_info(player)
        return {"type": "wait", "msg": "ok, waiting for all players to join"}
    else:
        print("Error wait", player)
        return {"type": "error", "msg": "wait for everyone!"}


players = {}  # player_name -> player_info
# phase1: waiting for players to join
print(f"waiting for {num_bidders} players")
while len(players) < num_bidders:
    request = socket.recv_json()
    response = answer_phase1(request)
    socket.send_json(response)


def answer_phase2(req, cur_round, bids):
    """
    In phase 2, we accept info and bid requests.
    To info we reply with the current state if the player needs to play
    or with wait if the player should wait for the next round.
    Bids are capped by the player's budget.
    >>> answer_phase2({"type": "info", "name": "alice"})
    sample_info
    >>> answer_phase2({"type": "info", "name": "alice"})
    {"type": "wait", "msg": "others are placing their bids"}
    >>> answer_phase2({"type": "bid", "name": "alice", "bid": 3.14})
    {"type": "bid", "msg": "got it", "bid": 3.14}
    >>> answer_phase2({"type": "bid", "name": "alice", "bid": 999999999})
    {"type": "bid", "msg": "entire budget", "bid": 42}
    """
    global players, items, item_types
    cur_player = req["name"]
    if req["type"] == "info":
        if cur_player in bids:
            return {"type": "wait", "msg": "others are placing their bids"}
        return {
            "type": "info",
            "item_types": item_types,
            "items": items,
            "cur_round": cur_round,
            "self": players[cur_player],
            "others": [info for name, info in players.items() if name != cur_player],
        }
    if req["type"] == "bid":
        budget = players[cur_player]["budget"]
        bid = max(0, min(budget, int(req["bid"])))
        bids[cur_player] = bid
        return {
            "type": "bid",
            "msg": ("got it" if bid < budget else "all in"),
            "bid": bid,
        }


for cur_round, item in enumerate(items):
    print(f"new round, competing for: {item}")
    bids = {}
    while len(bids) < len(players):
        request = socket.recv_json()
        response = answer_phase2(request, cur_round, bids)
        socket.send_json(response)
        print(bids, end="\r")

    print("final bids:", bids)

    bid, _, winner = max((bid, random.random(), player) for player, bid in bids.items())
    print(f"auction won by {winner}, at ${bid}")

    players[winner]["budget"] -= bid
    players[winner]["item_count"][item] += 1

    if players[winner]["item_count"][item] == needed_to_win:
        break  # keep last value for winner

print(f"Auction terminated winner {winner}")
for i in range(num_bidders):
    request = socket.recv_json()
    response = {"type": "done", "winner": winner}
    socket.send_json(response)
