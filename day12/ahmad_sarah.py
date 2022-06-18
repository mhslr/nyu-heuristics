def artists_by_3rd(info):
    """
    returns a list [(rd1, artist1), (rd2, artist2), ...]
    sorted by rdX, where rdX the minimum round at which
    we could have collected 3 paintings of artistX,
    takes into account our current collection
    """
    my_collection = info["self"]["item_count"]  # {artist: how_many_i_own}
    auction_items = info["items"]  # paintings, in order
    artists = info["item_types"]
    cur_round = info["cur_round"]
    never = 12345  # after end of auction

    def get_round3(artist):
        # compute rdX for artist
        left_to_win = 3 - my_collection[artist]
        artist_rounds = [
            rd
            for rd, item in enumerate(auction_items)
            if item == artist and rd >= cur_round
        ]
        return (
            artist_rounds[left_to_win - 1]  # 0-indexed
            if left_to_win <= len(artist_rounds)
            else never
        )

    round_3 = [(get_round3(artist), artist) for artist in artists]
    return sorted(round_3)


def single_double_paintings(info):
    """
    returns (single, double), where
      single: painters we own one painting of
      double: painters we own two paintings of
    """
    my_collection = info["self"]["item_count"]

    single = [artist for artist, count in my_collection.items() if count == 1]
    double = [artist for artist, count in my_collection.items() if count == 2]
    return single, double


def block_others(info):
    """
    if an opponent is about to win, bid above their budget
    """
    cur_item = info["items"][info["cur_round"]]
    opponents = info["others"]

    blocks = [
        player["budget"] + 1
        for player in opponents
        if player["item_count"][cur_item] == 2
    ]
    return max([0] + blocks)


def compete_for_first(others, want):
    """
    compete for our first painting
    bidding according to others budget
    """
    if len(others) == 1:
        other_budget = others[0]["budget"]
        return other_budget // 3 + 1
    else:  # many players, focus on direct competition
        competition = [
            player["budget"] for player in others if player["item_count"][want] >= 1
        ]
        if len(competition) > 0:
            return max(competition) // 2
        avg_others = sum(player["budget"] for player in others) // len(others)
        return avg_others // 3 + 1


def compute_bid_noblock(info):
    cur_item = info["items"][info["cur_round"]]
    my_coll = info["self"]["item_count"]
    my_budget = info["self"]["budget"]
    others = info["others"]
    min_bid = 2

    # top priority == want
    _, want = artists_by_3rd(info)[0]
    single, double = single_double_paintings(info)

    if my_coll[cur_item] == 2:
        return my_budget  # going all-in, we could win here

    if double:  # smth in double, but not cur_item: we want something else
        return min_bid

    if cur_item == want and my_coll[cur_item] == 1:
        return int(0.4 * my_budget) # leave 60% for last bid

    if cur_item == want and my_coll[cur_item] == 0:
        # we extracted this logic into its own function
        return max(compete_for_first(others, want), 20)

    return min_bid


def compute_bid_withblock(info):
    # simplify logic by making sure we block
    others = info["others"]
    bid = compute_bid_noblock(info)
    block = block_others(info)

    if len(others) <= 2 or block <= my_budget // 2:
        return max(bid, block)
    return bid


def compute_bid_state(info, prev_state):
    # main function
    bid = compute_bid_withblock(info)
    bid = min(info["self"]["budget"], max(0, int(bid)))  # safeguard
    return bid, None
