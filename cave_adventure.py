import random
from typing import List, Optional

from monster import Monster
from object import Object
from player import Player


class SubTask:
    def __init__(self,
                 location_description: str,
                 attack_description:str,
                 monster: Monster,
                 treasure: Object,
                 second_treasure: Optional[Object]):
        self.location_description = location_description
        self.attack_description = attack_description
        self.exit_description = "Move on to the next adventure"
        self.monster = monster
        self.treasure = [treasure]
        self.second_treasure = second_treasure
        pick_up_description = f"Pick up the {treasure.name}"
        self.options = [attack_description, pick_up_description]

        if second_treasure:
            self.treasure.append(second_treasure)

        self.lb = "\n"

    def task_accomplished(self):
        """For a task to be accomplished, the monster must be slayed, and the original treasure has to be taken"""
        return not self.monster.alive \
               and ( len(self.treasure)==0 or (len(self.treasure)==1 and self.second_treasure is not None) )

    def play(self, player: Player):
        """main finite state machine logic"""
        print(f"you are {self.location_description}")

        while self.options:
            print("What will you do now?")
            print(f"{self.lb.join([str(idx)+'.'+opt for idx, opt in enumerate(self.options)])}")
            print(self.lb)
            player_choice = input()

            option = self.options.pop(int(player_choice))
            if "pick up" in option.lower():
                if self.second_treasure is not None and self.treasure[0] == self.second_treasure:
                    if random.random() < 0.5:
                        player.christmas()
                    else:
                        player.math_questions()
                # pretty bad design here, str match would be better
                player.take(self.treasure[0], self)

            elif "attack" in option.lower():
                player.attack(self)

            elif "move on" in option.lower():
                break

            # updating options
            if len(self.treasure) == 1 and self.second_treasure is not None:
                self.treasure.append(self.second_treasure)
                self.options.append(f"Pick up the {self.second_treasure.name}")
            if self.task_accomplished():
                self.options.append(self.exit_description)
        print(self.exit_description)


class CaveAdventure:

    def __init__(self, intro_description: str, sub_tasks: List[SubTask]):
        self.intro_description = intro_description
        self.sub_tasks = sub_tasks

    @staticmethod
    def is_yes(s: str):
        return s.lower() in ["y", "yes", "yeah", "ya", "of course", "let's go", "let's do it"]

    @staticmethod
    def poem():
        words = []
        for i in range(random.randint(10, 20)):
            word = input(f"Villager Idiot {i}, what is your special word?")
            words.append(word)
        random.shuffle(words)

        i = 0
        while i < len(words):
            print(" ".join(words[i: i + min(5, len(words) - i)]))
            i += min(5, len(words) - i)
            print(" ".join(words[i: i + min(7, len(words) - i)]))
            i += min(7, len(words) - i)
            print(" ".join(words[i: i + min(5, len(words) - i)]))
            i += min(5, len(words) - i)
            print("")

    def play(self):
        player_name = input(f"Brave knight! What is your name?")
        player = Player(player_name)
        print(f"We need your help {player.name}! {self.intro_description} ")

        response = input(f"Oh mighty brave knight, might I interest you to enter the mouth of the cave?")
        cnt = 1
        while not self.is_yes(response):
            response = input(" ".join(["PLEASE!"]*cnt)+" Might I interest you to enter the mouth of the cave?")
            cnt += 1
            if cnt > 3:
                print("You are helpless. We will find our champion elsewhere then.")
                exit()

        for task in self.sub_tasks:
            task.play(player)

        print("You have collected all three golden treasures and are ready to move on to your final mission")
        response = input("Are you ready for the final mission?")
        cnt = 0
        while not self.is_yes(response):
            response = input(" ".join(["PLEASE!"] * cnt) + " Are you ready for the final mission?")
            cnt += 1
            if cnt > 2:
                print("I cannot help you help yourself. Your salvation must be earned somewhere else")
                exit()

        self.poem()

        print("Congratulations you have beat the game! The village is forever in debt to you. May we offer you "
              "full-ride to our Masters in AI program?")

