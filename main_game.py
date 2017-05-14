import title_screen, map_v3

def main():
    # Load up the title screen + selection option to play + select player name
    title_screen.start_title_sequence()
    import player
    map_v3.run_the_map()
        # insert code to allow player to interact with animal/cages
        # add limitations on the map borders

    # tally up the good points, bad points
    # trigger the question set (file i/o)
    # if X amount right, trigger good ending
    # if X amount wrong, trigger bad ending

    # end game

main()
