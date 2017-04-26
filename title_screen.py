# Print out the title / menu
import sys

game_title = """
*    **
 **    **
   *
      *

   *   **
*
  *
 *   * 
dont fall
*    **
 **    **
   *
      *

   *   **
*
  *
 *   *
"""

game_title_menu = """
Select an option:
0) Quit
1) Start
"""

print(game_title)

user_response = ""

while user_response not in ("0", "1"):
    user_response = str(input(game_title_menu))
    if user_response == "0":
        sys.exit()
    elif user_response == "1":
        # run the main code here to start the game
        # the print() is used as a filler here
        print("Yay you started the game!")
