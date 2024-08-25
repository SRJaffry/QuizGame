# main.py

from ContestantFile import Contestant

def main():
    # Create an object of Contestant
    contestant1 = Contestant(name="John Doe")
    contestant2 = Contestant(name="Jimmy Dio")
    contestant3 = Contestant(name="Shan Jaffry")
    # contestant3 = Contestant()

    contestant3.display()
    
# Step 3: Ensure the script runs as the main program
if __name__ == "__main__":
    main()
