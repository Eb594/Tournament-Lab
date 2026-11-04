import json
import tempfile
import unittest
from pathlib import Path

from tournament.teams import register_team
from tournament.fixtures import generate_fixtures
from tournament.results import record_result
from tournament.standings import calculate_standings, get_champion
from tournament.storage import save_tournament, load_tournament


class TestTournamentLab(unittest.TestCase):

    def setUp(self):
        self.teams = []
        for name in ["Falcons", "Titans", "Phoenix", "Warriors"]:
            register_team(self.teams, name)

        self.fixtures = generate_fixtures(self.teams)

    def test_register_team(self):
        self.assertEqual(len(self.teams), 4)

    def test_team_name_is_trimmed(self):
        teams = []
        team = register_team(teams, "  Eagles  ")
        self.assertEqual(team["name"], "Eagles")

    def test_duplicate_team_is_rejected(self):
        with self.assertRaises(ValueError):
            register_team(self.teams, "falcons")

    def test_short_team_name_is_rejected(self):
        with self.assertRaises(ValueError):
            register_team(self.teams, "A")

    def test_maximum_eight_teams(self):
        for name in ["Eagles", "Sharks", "Dragons", "Lions"]:
            register_team(self.teams, name)

        with self.assertRaises(ValueError):
            register_team(self.teams, "Tigers")

    def test_generate_round_robin_fixtures(self):
        self.assertEqual(len(self.fixtures), 6)

    def test_every_team_pair_is_unique(self):
        pairs = [
            frozenset((f["home_id"], f["away_id"]))
            for f in self.fixtures
        ]
        self.assertEqual(len(pairs), len(set(pairs)))

    def test_fixture_generation_requires_four_teams(self):
        with self.assertRaises(ValueError):
            generate_fixtures(self.teams[:3])

    def test_record_match_result(self):
        result = record_result(self.fixtures, "M001", 2, 0)
        self.assertEqual(result["home_score"], 2)
        self.assertEqual(result["away_score"], 0)
        self.assertEqual(result["status"], "played")

    def test_invalid_fixture_is_rejected(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M999", 2, 0)

    def test_negative_score_is_rejected(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", -1, 0)

    def test_float_score_is_rejected(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", 2.5, 0)

    def test_duplicate_result_is_rejected(self):
        record_result(self.fixtures, "M001", 2, 0)
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", 1, 1)

    def test_standings_calculation(self):
        record_result(self.fixtures, "M001", 2, 0)
        standings = calculate_standings(self.teams, self.fixtures)

        falcons = next(t for t in standings if t["name"] == "Falcons")
        self.assertEqual(falcons["points"], 3)
        self.assertEqual(falcons["wins"], 1)

    def test_goal_difference(self):
        record_result(self.fixtures, "M001", 3, 1)
        standings = calculate_standings(self.teams, self.fixtures)

        falcons = next(t for t in standings if t["name"] == "Falcons")
        self.assertEqual(falcons["goal_difference"], 2)

    def test_champion_not_declared_early(self):
        record_result(self.fixtures, "M001", 2, 0)
        self.assertIsNone(get_champion(self.teams, self.fixtures))

    def test_save_and_load_tournament(self):
        record_result(self.fixtures, "M001", 2, 0)

        with tempfile.TemporaryDirectory() as directory:
            filepath = Path(directory) / "data.json"
            save_tournament(self.teams, self.fixtures, filepath)

            loaded_teams, loaded_fixtures = load_tournament(filepath)

            self.assertEqual(loaded_teams, self.teams)
            self.assertEqual(loaded_fixtures, self.fixtures)

    def test_missing_file_is_rejected(self):
        with self.assertRaises(FileNotFoundError):
            load_tournament("missing_tournament_file.json")

    def test_invalid_json_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            filepath = Path(directory) / "invalid.json"
            filepath.write_text("{invalid json", encoding="utf-8")

            with self.assertRaises(ValueError):
                load_tournament(filepath)

    def test_unsupported_schema_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            filepath = Path(directory) / "wrong_version.json"
            filepath.write_text(
                json.dumps({
                    "schema_version": 99,
                    "teams": self.teams,
                    "fixtures": self.fixtures
                }),
                encoding="utf-8"
            )

            with self.assertRaises(ValueError):
                load_tournament(filepath)


if __name__ == "__main__":
    unittest.main()
