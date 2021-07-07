import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cave_adventure import SubTask

from object import Object


class Player(Object):

    def __init__(self, name: str):
        super().__init__(name)
        self.inventory = []

    def take(self, item: Object, sub_task: "SubTask"):
        if item in sub_task.treasure:
            self.inventory.append(item)
            sub_task.treasure.remove(item)
            print(f"You picked up the {item.name}")
            if sub_task.monster.alive:
                print("now go rest before continuing the mission ...")
                self.snooze()
                print("Great! now you are awake and rested.")
        else:
            print(f"The {item.name} is not here. You can't pick up what is not there")

    @staticmethod
    def attack(sub_task: "SubTask"):
        if sub_task.monster.alive:
            sub_task.monster.alive = False
            print(f"You gave a left-right-good-night to the {sub_task.monster.name}")
        else:
            print("You hated the goblin so much that even though it was dead, "
                  "you spit on it one more time to show disrespect")

    @staticmethod
    def snooze():
        animals = ["cows", "chicks", "pigs"]
        random.shuffle(animals)
        animal_sound = {"cows": "moo", "chicks": "cluck", "pigs": "oink"}
        for animal in animals:
            print(f"Old MacDonald had a farm\nEe i ee i o\nAnd on his farm he had some {animal}\nEe i ee i oh\n"
                  f"With a {animal_sound[animal]}-{animal_sound[animal]} here\n"
                  f"And a {animal_sound[animal]}-{animal_sound[animal]} there\n"
                  f"Here a {animal_sound[animal]}, there a {animal_sound[animal]}\n"
                  f"Everywhere a {animal_sound[animal]}-{animal_sound[animal]}")

    @staticmethod
    def math_questions(num_questions:int = 5):
        print("The Goblins have tricked you into picking up the second treasure, "
              "your penance is to answer 5 math questions")
        for _ in range(num_questions):
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            operation = random.choice(["+", "-", "*"])
            answer = eval(f"{num1}{operation}{num2}")
            question = f"{num1}{operation}{num2}=?"
            user_answer = ""
            while user_answer != answer:
                user_answer = int(input(question))

    @staticmethod
    def christmas():
        print("The Goblins have tricked you into picking up the second treasure, your penance is to sing the Twelve "
              "Days of Christmas")
        print("""
                On the first day of Christmas my true love gave to me
                A partridge in a pear tree
                On the second day of Christmas my true love gave to me
                Two turtle doves and a partridge in a pear tree
                On the third day of Christmas my true love gave to me
                Three French hens, two turtle doves and a partridge in a pear tree
                On the fourth day of Christmas my true love gave to me
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the fifth day of Christmas my true love gave to me
                Five gold rings, four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the sixth day of Christmas my true love gave to me
                Six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the seventh day of Christmas my true love gave to me
                Seven swans a swimming, six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the eighth day of Christmas my true love gave to me
                Eight maids a milking, seven swans a swimming
                Six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the ninth day of Christmas
                Nine ladies dancing, eight maids a milking
                Seven swans a swimming, six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the tenth day of Christmas my true love gave to me
                Ten lords a leaping, nine ladies dancing, eight maids a milking
                Seven swans a swimming, six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the eleventh day of Christmas my true love gave to me
                Eleven pipers piping, ten lords a leaping
                Nine ladies dancing, eight maids a milking
                Seven swans a swimming, six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                On the twelfth day of Christmas my true love gave to me
                Twelve drummers drumming, eleven pipers piping
                Ten lords a leaping, nine ladies dancing, eight maids a milking
                Seven swans a swimming, six geese a laying, five gold rings
                Four calling birds, three French hens
                Two turtle doves and a partridge in a pear tree
                """)