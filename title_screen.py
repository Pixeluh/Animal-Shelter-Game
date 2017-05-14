# TO DO LIST
# 1) Change the title to whatever fits
def start_title_sequence():

    import sys
    import os

    game_title = """
    *    ** *    **
     **    * * **    **
       * *
          * *

       *   ** *   **
    **
      **
     *   * *   *
          animals
    *    ** *    **
     **    ** **    **
       * *
          * *

       *   ** *   **
    * *
      * *
     *   * *   *
    """

    game_title_menu = """
    -----------------
    Select an option:
    0) Quit
    1) Start
    -----------------
    """

    print(game_title)

    user_response = ""

    while user_response not in ("0", "1"):

        user_response = str(input(game_title_menu))

        if user_response == "0":

            print("Good-bye.")
            sys.exit()

        elif user_response == "1":

            os.system('cls')
