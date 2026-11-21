
import unittest

from game import new_game, move_player, ISLAND_MAP


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Gold")

    def test_new_game_starts_at_beach(self):
        self.assertEqual(self.player["location"], "Beach")

    def test_new_game_starts_with_five_energy(self):
        self.assertEqual(self.player["energy"], 5)

    def test_valid_move_to_jungle(self):
        result = move_player(self.player, "Jungle")

        self.assertTrue(result)
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_invalid_move_does_not_change_state(self):
        result = move_player(self.player, "Cave")

        self.assertFalse(result)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_movement_is_case_insensitive(self):
        result = move_player(self.player, "jungle")

        self.assertTrue(result)
        self.assertEqual(self.player["location"], "Jungle")

    def test_map_contains_five_locations(self):
        self.assertEqual(len(ISLAND_MAP), 5)

    def test_cannot_move_without_energy(self):
        self.player["energy"] = 0

        result = move_player(self.player, "Jungle")

        self.assertFalse(result)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 0)


if __name__ == "__main__":
    unittest.main()
