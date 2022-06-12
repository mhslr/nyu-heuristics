from pprint import pprint
import zmq
import time
import random

PORT = 50018
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%d" % PORT)
# socket.connect("tcp://2.tcp.ngrok.io:17918")
my_name = input("what's your name? ")
is_bot = "n" not in input("are you a bot? (Y/n) ").lower()

happy_bot = [
    "Why aren't you cheering louder?",
    "Aren't you proud of me?",
    "Damn I'm good, and I don't even have a brain!",
]
sad_bot = [
    "I'm doing my best, okay?",
    "And do you think you could do any better?",
    "I feel like it's me doing all the work, you're just chilling in your chair",
    "If I lose this it's your fault not mine... I'm doing EXACTLY what you told me to do!",
]

sample_info = {
    "cur_round": 10,
    "history": [
        {"bid": 76, "item": "Van_Gogh", "player": "charlie"},
        {"bid": 79, "item": "Da_Vinci", "player": "bob"},
        {"bid": 11, "item": "Van_Gogh", "player": "bob"},
        {"bid": 92, "item": "Da_Vinci", "player": "alice"},
        {"bid": 2, "item": "Picasso", "player": "bob"},
        {"bid": 10, "item": "Picasso", "player": "charlie"},
        {"bid": 9, "item": "Van_Gogh", "player": "charlie"},
        {"bid": 6, "item": "Picasso", "player": "bob"},
        {"bid": 6, "item": "Rembrandt", "player": "alice"},
        {"bid": 3, "item": "Picasso", "player": "charlie"},
    ],
    "item_types": ["Picasso", "Van_Gogh", "Rembrandt", "Da_Vinci"],
    "items": [
        "Van_Gogh",
        "Da_Vinci",
        "Van_Gogh",
        "Da_Vinci",
        "Picasso",
        "Picasso",
        "Van_Gogh",
        "Picasso",
        "Rembrandt",
        "Picasso",
        "Picasso",
        "Da_Vinci",
        "Da_Vinci",
        "Van_Gogh",
        "Van_Gogh",
        "Van_Gogh",
        "Rembrandt",
        "Van_Gogh",
        "Rembrandt",
        "Van_Gogh",
        "Rembrandt",
        "Rembrandt",
        "Picasso",
        "Picasso",
        "Picasso",
        "Rembrandt",
        "Rembrandt",
        "Da_Vinci",
        "Da_Vinci",
        "Rembrandt",
        "Van_Gogh",
        "Da_Vinci",
        "Picasso",
        "Da_Vinci",
        "Rembrandt",
        "Picasso",
        "Rembrandt",
    ],
    "others": [
        {
            "budget": 2,
            "item_count": {"Da_Vinci": 1, "Picasso": 2, "Rembrandt": 0, "Van_Gogh": 1},
            "name": "bob",
        },
        {
            "budget": 2,
            "item_count": {"Da_Vinci": 1, "Picasso": 0, "Rembrandt": 1, "Van_Gogh": 0},
            "name": "alice",
        },
    ],
    "self": {
        "budget": 2,
        "item_count": {"Da_Vinci": 0, "Picasso": 2, "Rembrandt": 0, "Van_Gogh": 2},
        "name": "charlie",
    },
    "type": "info",
}


def dennis_fmt(info):
    """
    converts info to Dennis' format

    itemsinauction is a list where at index "rd" the item in that round is being sold is displayed.

    winnerarray is a list where at index "rd" the winner of the item sold in that round is displayed.

    winneramount is a list where at index "rd" the amount of money paid for the item sold in that round is displayed.

    example: I will now construct a sentence that would be correct if you substituted the outputs of the lists:
    In round 5 winnerarray[4] bought itemsinauction[4] for winneramount[4] dirhams/dollars/money unit.

    numberbidders is an integer displaying the amount of people playing the auction game.

    players is a list containing all the names of the current players.

    mybidderid is a string that contains your name.

    artists is a list containing all the names of the artists (paintings) that are for sale in our auction.

    standings is a set of nested dictionaries (standings is a dictionary that for each person has another dictionary
    associated with them). standings[name][artist] will return how many paintings "artist" the player "name" currently has
    standings[name]['money'] (remember quotes for string, important!) returns how much money the player "name" has left.
    If you want to access information about yourself use standings[mybidderid][(name of artist)/'money']

    rd is the current round in 0 based indexing.
    """
    itemsinauction = info["items"]
    winnerarray = [x["player"] for x in info["history"]]
    winneramount = [x["bid"] for x in info["history"]]
    numberbidders = len(info["others"]) + 1
    all_p = info["others"] + [info["self"]]
    players = [p["name"] for p in all_p]
    mybidderid = info["self"]["name"]
    artists = info["item_types"]
    standings = [
        {artist: p["item_count"][artist] for artist in artists}
        | {"money": p["budget"]}
        for p in all_p
    ]
    rd = info["cur_round"]
    return (
        itemsinauction,
        winnerarray,
        winneramount,
        numberbidders,
        players,
        mybidderid,
        artists,
        standings,
        rd,
    )


def compute_bid(info):
    """
    TODO: complete this function to determine the best bid.
    >>> compute_bid(sample_info)
    2
    """
    # convert info to Dennis' format
    # you are free to apply further preprocessing to make your life easier
    (
        itemsinauction,
        winnerarray,
        winneramount,
        numberbidders,
        players,
        mybidderid,
        artists,
        standings,
        rd,
    ) = dennis_fmt(info)
    rd = info["cur_round"]
    bid = info["self"]["budget"] * random.random()
    bid = round(bid)
    print(f"bidding ${bid} for a", info["items"][rd])
    return bid


def ask_bid(info):
    """
    >>> ask_bid(sample_info)
    5
    """
    rd = info["cur_round"]
    info["items"] = info["items"][rd : rd + 10]  # too long to print
    pprint(info)
    return int(input("place your bid (integer): "))


def done_msg(winner):
    if my_name == winner:
        return f"Congrats {winner}, you won!"
    else:
        return f"Too bad, you lost to {winner}."

def round_msg(info):
    if info["history"]:
        last = info["history"][-1]
        print('auction won by %s at $%d' % (last['player'], last['bid']))
        if is_bot:
            print(random.choice(happy_bot if info['history'][-1]['player'] == my_name else sad_bot))
            print()
    else:
        print("Let's go!")


while True:
    request = {"type": "info", "name": my_name}
    socket.send_json(request)
    response = socket.recv_json()

    if response["type"] == "info":
        info = response.copy()
        round_msg(info)
        # we recieved the latest info, we can compute and place our bid
        if is_bot:
            bid = int(compute_bid(info))
        else:
            bid = ask_bid(info)

        bid_request = {"type": "bid", "name": my_name, "bid": bid}
        socket.send_json(bid_request)
        bid_response = socket.recv_json()
        # check that there was no error
        assert bid_response["type"] == "bid"

    elif response["type"] == "wait":
        time.sleep(0.1)

    elif response["type"] == "done":
        print(done_msg(response["winner"]))
        break

    else:
        print("ERROR:", response)
