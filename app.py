#You will be creating an application that has two modes

#Teacher Mode

#In teacher mode you will be asking the user to input a word/phrase and the
#answer as a key:value pair. These pairs will be written to a json file called
#FlashCards.json
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
x =History_studies("Emperor Wu", "141 to 87 BC", "The Tang Dynasty", "Humid")
history = [
   
]
history.append(x.to_dict())
print(history)

#Student Mode
#In student mode you will present the student with the
#phrases/words/images and the user will type the answer in the terminal.
#Keep a tally of correct answers and provide a score. Give students bonus
#points for “Streaks”