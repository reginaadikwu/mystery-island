
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


    def test_rope_can_be_collected_at_beach(self):
        from game import collect_item

        result = collect_item(self.player, "Rope")

        self.assertTrue(result)
        self.assertIn("Rope", self.player["inventory"])

    def test_rope_cannot_be_collected_twice(self):
        from game import collect_item

        collect_item(self.player, "Rope")
        result = collect_item(self.player, "Rope")

        self.assertFalse(result)
        self.assertEqual(self.player["inventory"].count("Rope"), 1)

    def test_lantern_cannot_be_collected_at_beach(self):
        from game import collect_item

        result = collect_item(self.player, "Lantern")

        self.assertFalse(result)
        self.assertNotIn("Lantern", self.player["inventory"])

    def test_lantern_can_be_collected_in_cave(self):
        from game import collect_item

        self.player["location"] = "Cave"

        result = collect_item(self.player, "Lantern")

        self.assertTrue(result)
        self.assertIn("Lantern", self.player["inventory"])


if __name__ == "__main__":
    unittest.main()
