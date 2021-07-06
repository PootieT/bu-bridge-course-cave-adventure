import unittest
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
            second_treasure=None
        )

        game = CaveAdventure(intro_description=intro_description, sub_tasks=[task1])
        game.play()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
