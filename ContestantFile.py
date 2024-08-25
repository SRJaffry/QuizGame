# ContestantFile.py

from Questions import ManageQuestions
from quiz_data import correct_answers_dict

class Contestant:
    contestant_cnt = 0
    Max_allowed_questions = 5

    def __init__(self, name = None):
        Contestant.contestant_cnt +=1
        self.id = self.contestant_cnt
        self.name = name
        self.score = 0
        self.No_of_questions_asked = 0
        self.max_allowed_questions = Contestant.Max_allowed_questions

        # make object of class ManageQuestions
        self.question_obj = ManageQuestions()

    def set_name(self, name):
        self.name = name
    
    def get_details(self, details):
        
        if details in list(vars(self)): # We can also use if hasattr(self, details):        
            return getattr(self, details)
        else:
            #raise Exception("{} does not exist.")    
            return 0 
    
    def display(self):
        print('Total {} contestant participating'.format(Contestant.contestant_cnt))

    def get_score(self):
        return self.score

    def play(self, Max_no_of_questions_asked = None):
        # 1. Asking the question / Displaying the question
        # 2. Show all the options for the question
        # 3. Select the answer/options
        # 4. Check if the answer is correct, and score calculate.

        if Max_no_of_questions_asked is not None:
            self.Max_allowed_questions = Max_no_of_questions_asked

        len_of_question_list = 0

        # Play the game Following Number of Times self.Max_allowed_questions
        # while self.No_of_questions_asked < self.Max_allowed_questions:
        while len_of_question_list < self.Max_allowed_questions:    

            print("--------------\n--------------")
            
            # 1. Asking the question
            # question_key is the integer value key which we will use to find answers, or see options etc.
            len_of_question_list, question_key = self.question_obj.ask_questions()
            
            self.No_of_questions_asked += 1

            # assert statement to make sure len_of_question_list is equal to self.No_of_questions_asked
            assert len_of_question_list == self.No_of_questions_asked, "len_of_question_list is not equal to self.No_of_questions_asked"

            # 2. Now Showing the options
            self.question_obj.show_options(question_key)
        
            # 3. Selecting the answers/options
            self.current_answer = input("Select from the following options: A, B, C, D : ").upper()
            while self.current_answer not in ["A", "B", "C", "D"]:
                self.current_answer = input("Wrong input. Please select from the following options: A, B, C, D : ").upper()


            # 4. Checking if the answer is correct
            if self.current_answer == correct_answers_dict[question_key]:
                self.score += 1
            # else:
            #     print("Wrong Answer. The correct answer is : {}".format(correct_answers_dict[question_key]))    

