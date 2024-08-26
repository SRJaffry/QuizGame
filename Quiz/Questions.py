from Quiz.quiz_data import questions_dict, options_dict, correct_answers_dict
import random

class ManageQuestions():

    def __init__(self):
        self.asked_questions_list = []
        self.answer_list = []
        self.current_question_key = None
        self.current_answer = None
        self.question_key_list = [keys for keys, values in questions_dict.items()]

    def ask_questions(self):
        
        # INPUT arguments
        # 1. question_key_list : list of all available questions. Not a direct input, but imported from quiz_data.
        # 2. asked_question : list of questions already asked. Ensure that questions are never asked again.
        # 3. ans_list: list of answers given as per the key/question
        #
        # RETURN: length of of question asked

        self.current_question_key = random.choice(self.question_key_list)
        while self.current_question_key in self.asked_questions_list:
            self.current_question_key = random.choice(self.question_key_list)
        
        self.asked_questions_list.append(self.current_question_key)

        print(questions_dict[self.current_question_key])

        return len(self.asked_questions_list), self.current_question_key


    def show_options(self, question_key = None):
        # INPUT arguemt
        # question_key is the key to the dictioray options_dic
        #
        # EXPLANATION
        # options_dict[self.current_question_key] is the dictionary which conains option A, B, C, D etc.
        # options_dict[self.current_question_key].items() will give us the key
        # and the value

        if question_key is None:
            question_key = self.current_question_key 

        for key, value in options_dict[question_key].items():
            print(f"{key} : {value}")

