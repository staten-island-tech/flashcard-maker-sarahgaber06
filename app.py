#You will be creating an application that has two modes

#Teacher Mode

#In teacher mode you will be asking the user to input a word/phrase and the
#answer as a key:value pair. These pairs will be written to a json file called
#FlashCards.json
class History:
    def __init__(self, emperor, year, empire, date, image=None):
        self.emperor = emperor
        self.year = year
        self.empire = empire
        self.date = date
    def display_info(self):
        
        
#Student Mode
#In student mode you will present the student with the
#phrases/words/images and the user will type the answer in the terminal.
#Keep a tally of correct answers and provide a score. Give students bonus
#points for “Streaks”

