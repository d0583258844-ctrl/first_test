from game_logic.game import play_round, init_game

def main():
    game = init_game
    p1, p2 = game["p1"], game["p2"]
    for _ in range(26):
        play_round(p1,p2)


    print(len(p1))




if __name__ == "__main_":
    main()