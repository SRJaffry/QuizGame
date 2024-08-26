# main.py

from Players.ContestantFile import Contestant 
from HouseKeeping.HouseKeeping import clear_screen
from HouseKeeping.FormatResults import FormatResults


def main():
    # Create an object of Contestant
    C1 = Contestant(name="Riaz Jaffry")
    C2 = Contestant(name="Ali Meesum")
    C3 = Contestant(name="Shan Jaffry")

    # print(f"contestant 2 ID is :{C2.get_details('id')}")
    C1.play(3) # Ask N questions    
    print(f"Player {C1.name} (player ID  = {C1.id}), Your score is {C1.get_score()}")
    clear_screen()

    C2.play(3) # Ask N questions   
    print(f"Player {C2.name} (player ID  = {C2.id}), Your score is {C2.get_score()}")
    clear_screen()

    C3.play(3) # Ask N questions    
    print(f"Player {C3.name} (player ID  = {C3.id}), Your score is {C3.get_score()}")

    clear_screen()
    print("Thank you for playing. ")
    FormatResults.show_results([C1, C2, C3])
    
# Step 3: Ensure the script runs as the main program
if __name__ == "__main__":
    main()
