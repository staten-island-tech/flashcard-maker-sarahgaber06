#You will be creating an application that has two modes

#Teacher Mode
#In teacher mode you will be asking the user to input a word/phrase and the
#answer as a key:value pair. These pairs will be written to a json file called
#FlashCards.json
import json 
mode = input("Are you a teacher or a student?")
class History_studies:
    def __init__(self, emperor, year, empire, climate, image=None):
        self.emperor = emperor
        self.year = year
        self.empire = empire
        self.climate = climate
        self.image = image
    def display_info(self):
        return f"{self.emperor} {self.year} {self.empire} {self.climate}"
    def to_dict(self):
        return{"emperor": self.emperor, "year": self.year, "empire": self.empire, "climate": self.climate, "image": self.image}
    
try:
   with open("history.json", "r") as file:
        history_data = json.load(file)
except FileNotFoundError:
    history_data = []

if mode == "teacher":

    new_emperor = input("Enter an Emperor")
    new_year = input("Enter a year")
    new_empire = input("Enter an empire")
    new_climate = input("Enter a climate")

new_flashcard = History_studies(new_emperor, new_year, new_empire, new_climate)

history_data.append(new_flashcard.to_dict())

# Save updated data back to file
with open("history.json", "w") as file:
    json.dump(history_data, file, indent=4)
    
if mode == "student":
    streaks = 0
    points = 0

    for flashcard in history_data:
        print(flashcard["empire"])
    if "empire" == "The Tang Dynasty":
        print("correct")
        points +1
        streaks +1
    else:
        print("incorrect")

    for flashcard in history_data:
        print(flashcard["emperor"])
        if "emperor" == "Emperor Wu":
            print("correct")
            points +1
            streaks +1
        else:
            print("incorrect")

for flashcard in history_data:
    print(flashcard["year"])
    if "year" == "141 to 81 BC":
        print("correct")
        points +1
        streaks +1
    else:
        print("incorrect")

for flashcard in history_data:
    print(flashcard["climate"])
    if "climate" == "Humid":
        print("correct")
        points +1
        streaks +1
    else:
        print("incorrect")
    
#Student Mode
#In student mode you will present the student with the
#phrases/words/images and the user will type the answer in the terminal.
#Keep a tally of correct answers and provide a score. Give students bonus
#points for “Streaks”

