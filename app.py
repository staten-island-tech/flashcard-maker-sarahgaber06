#Student and Teacher Modes
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

        guess = input("What emperor?")
        if guess == flashcard["emperor"]:
            print("correct")
            points +=1
            streaks +=1
        else:
            print("incorrect")

        guess = input("What year?")
        if guess == flashcard["year"]:
            print("correct")
            points +=1
            streaks +=1
        else:
            print("incorrect")

        guess = input("What climate?")
        if guess == flashcard["climate"]:
            print("correct")
            points +=1
            streaks +=1
        else:
            print("incorrect")
        break 


