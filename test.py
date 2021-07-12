import unittest
import random

from monster import Monster
from object import Object
from cave_adventure import CaveAdventure, SubTask


class MyTestCase(unittest.TestCase):

    def test_zero_tasks(self):
        # no tasks, just enter your name, and say yes, you win the game
        game = CaveAdventure(intro_description="The village is on fire", sub_tasks=[])
        game.play()
        self.assertTrue(True)

    def test_one_task(self):
        # one task
        intro_description = "Our village is being overrun by the goblins of the NorthernCaves. " \
                            "We need you to defeat them! "

        task1 = SubTask(
            location_description="Entering the mouth of the cave",
            attack_description="Attack the evil goblin and clean all the cob webs",
            monster=Monster("evil goblin Marcel"),
            treasure=Object("golden sword"),
            second_treasure=None
        )

        game = CaveAdventure(intro_description=intro_description, sub_tasks=[task1])
        game.play()
        self.assertTrue(True)

    def test_one_task_two_treasure(self):
        # one task
        intro_description = "Our village is being overrun by the goblins of the NorthernCaves. " \
                            "We need you to defeat them! "

        task1 = SubTask(
            location_description="Entering the mouth of the cave",
            attack_description="Attack the evil goblin and clean all the cob webs",
            monster=Monster("evil goblin Marcel"),
            treasure=Object("golden sword"),
            second_treasure=Object("silver box")
        )

        game = CaveAdventure(intro_description=intro_description, sub_tasks=[task1])
        game.play()
        self.assertTrue(True)

    def test_three_tasks(self):
        # one task
        intro_description = "Our village is being overrun by the goblins of the NorthernCaves. " \
                            "We need you to defeat them! "

        task1 = SubTask(
            location_description="Entering the mouth of the cave",
            attack_description="Attack the evil goblin and clean all the cob webs",
            monster=Monster("evil goblin Marcel"),
            treasure=Object("golden sword"),
            second_treasure=None
        )
        task2 = SubTask(
            location_description="Going deeper into the cave",
            attack_description="Attack the evil wombat and turn off the water supply",
            monster=Monster("evil wombat Limpian"),
            treasure=Object("golden shield"),
            second_treasure=None
        )
        task3 = SubTask(
            location_description="Reaching the depth of the cave",
            attack_description="Attack the goblin lord",
            monster=Monster("hobgoblin lord DivaDon"),
            treasure=Object("golden helmet"),
            second_treasure=None
        )
        sub_tasks = [task1, task2, task3]
        rand_task = random.choice(sub_tasks)
        rand_task.second_treasure = Object("silver tray of life")
        rand_task.treasure.append(rand_task.second_treasure)

        game = CaveAdventure(intro_description=intro_description, sub_tasks=sub_tasks)
        game.play()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
