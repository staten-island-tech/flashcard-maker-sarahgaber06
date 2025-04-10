#You will be creating an application that has two modes

#Teacher Mode

#In teacher mode you will be asking the user to input a word/phrase and the
#answer as a key:value pair. These pairs will be written to a json file called
#FlashCards.json
import json 


#Student Mode
#In student mode you will present the student with the
#phrases/words/images and the user will type the answer in the terminal.
#Keep a tally of correct answers and provide a score. Give students bonus
#points for “Streaks”
import json 
class History_studies:
    def __init__(self, emperor, year, empire, climate, image=None):
        self.emperor = emperor
        self.year = year
        self.empire = empire
        self.climate = climate
        self.image = image
    def display_info(self):
        return f"{self.emperor} {self.make} {self.model}"
    def to_dict(self):
        return{"emperor": self.emperor, "year": self.year, "empire": self.empire, "climate": self.climate, "image": self.image}
y =History_studies("Emperor Wu", "141 to 87 BC", "The Tang Dynasty", "Humid")
history = []
history.append(y.to_dict())
file_name = 'history_data.json'
score = 0
streak = 0
thing =  {
        "emperor": "Emperor Wu",
        "year": "141 to 87 BC",
        "empire": "The Tang Dynasty",
        "climate": "Humid",
        
    },



try:
    with open("history.json", "r") as file:
        history_data = json.load(file)
except FileNotFoundError: 
    history_data = []
with open("history.json", "w") as file:
    json.dump(history_data, file, indent=4)
history_data.append(history.to_dict())

