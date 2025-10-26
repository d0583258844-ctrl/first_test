import random


CARDS_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9" ,"10" ,"J", "Q", "K", "A" ]
CARDS_SUITES = ["h", "s", "d", "c"]


def create_card(rank:str,suite:str) ->dict:

    speical_ranks = {
    "J":11,
    "Q":12,
    "K":13,
    "A":14
    }
    try:
        value = int(rank)
    except ValueError:
        value = speical_ranks[rank]

    return {
    "rank": rank,
    "suite": suite,
    "value": value
    }








def create_deck()->list[dict]:
    cards = []

    for s in CARDS_SUITES:
        for r in CARDS_RANKS:        
            cards.append(create_card(r,s))

    return cards
    
print(create_deck())










def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    if p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "WAR"


print(compare_cards({"value": 9, "suite":"s","rank":14}, {"value": 13,"sutie":"d"}))









def shuffle(deck:list[dict]) -> list[dict]:
    index1 = random.randint(0, 51)
    index2 = random.randint(0, 51)
    for _ in range(1000):
        if index1 == index2:
            continue
        else:
            deck[index1],deck[index2] =  deck[index2],deck[index1]
    return deck

print(shuffle(create_deck()))