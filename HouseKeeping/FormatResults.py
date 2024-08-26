
from Players import ContestantFile

class FormatResults:
    def __init__(self, contestant_list):
        self.contestant_list = contestant_list

    @staticmethod
    def show_results(contestant_list):
        print("Total {} contestant participating".format(len(contestant_list)))

        for contestant in contestant_list:
            print(f"Player {contestant.name} (player ID  = {contestant.id}), Your score is {contestant.get_score()}")

        # contestant_list.sort(key = lambda contestant:contestant.score)
        # Sorting contestant_lit list in increaseing order of score
        contestant_list.sort(key = lambda contestant:contestant.score, reverse=True)
        

        print("\nRanking:\n")
        for contestant in contestant_list:
            print(f"Player {contestant.name} (player ID  = {contestant.id}), Your score is {contestant.get_score()}")