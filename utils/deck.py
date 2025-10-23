all_cards =[ {}]
def create_card(rank:str,suite:str):
    card={"rank":"","suite":"","value":""}   
    card["rank"] = rank 
    card["suite"] = str(suite)
    
    return card



create_card("A","D")




def create_deck():
    rank = [2, 3, 4, 5, 6, 7, 8, 9 ,10 ,"J", "Q", "K", "A" ]
    suite = ["H", "S", "D", "C"]
    global all_cards
    temporary_dict = {}



    create_card()
    for i in suite:
        for j in rank: 
            temporary_dict[rank],[suite],[value] = j , i , j         
        return temporary_dict

create_card("2"  ,"H")






# cards_dict = {"rank": int/str, "suite": str, "value": int}
#     return str[dict]




# def compare_cards(p1_card:dict, p2_card:dict):
#     return str



# def shuffle(deck:list[dict]):
#     return list[dict]