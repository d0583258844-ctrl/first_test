from utils.deck import shuffle,create_deck,compare_cards,P1_WON,P2_WON,WAR

def create_player(name :str="AI") ->dict:
    return{"name":name,
            "hand": [],
            "won_pil": []
         }
  


   






def init_game()->dict:
   p1 = create_player("Daniel")
   p2= create_player()
   deck = create_deck()
   shuffle_deck = shuffle(deck)

   p1["hand"] = shuffle_deck[:26]
   p2["hand"] = shuffle_deck[26:]



   game = {
      "p1":p1,
      "p2":p2
   }

   return game


def play_round(p1:dict,p2:dict)-> None:
   card_p1=p1["hand"].pop()
   card_p2=p2["hand"].pop()

   round_winner = compare_cards(card_p1,card_p2)

   if round_winner == P1_WON:
      return 