# ContestantFile.py

class Contestant:
    contestant_cnt = 0

    def __init__(self):
        Contestant.contestant_cnt +=1
        self.id = self.contestant_cnt
        self.name = None
        self.score = 0

    def __init__(self, name):
        Contestant.contestant_cnt +=1
        self.id = self.contestant_cnt
        self.name = name
        self.score = 0

    def set_name(self, name):
        self.name = name
    
    def get_details(self, details):
        
        if details in list(whos(self)):
            return getattr(self, details)
        else:
            raise Exception("{} does not exist.")    
    

    def display(self):
        print('Total {} contestant participating'.format(Contestant.contestant_cnt))
