import random

from tournament.teams import register_team, list_teams
from tournament.fixtures import generate_fixtures, list_fixtures
from tournament.results import record_result
from tournament.standings import calculate_standings, get_champion
from tournament.storage import save_tournament, load_tournament


def display_menu():
    print("\n========== TOURNAMENTLAB ==========")
    print("1. Register a team")
    print("2. List all teams")
    print("3. Generate fixtures")
    print("4. View fixtures")
    print("5. Record match results")
    print("6. View league standings")
    print("7. Save tournament")
    print("8. Load tournament")
    print("9. Simulate demo tournament")
    print("10. Show champion")
    print("0. Exit")
    print("===================================")


def show_teams(teams):
    if not teams:
        print("No teams have been registered.")
        return

    print("\nREGISTERED TEAMS")

    for team in teams:
        print(f"{team['id']} - {team['name']}")


def show_fixtures(fixtures, teams):
    if not fixtures:
        print("No fixtures available. Generate fixtures first.")
        return

    print("\nTOURNAMENT FIXTURES")

    for fixture in list_fixtures(fixtures, teams):
        print(
            f"{fixture['id']} | "
            f"{fixture['home']} vs {fixture['away']} | "
            f"{fixture['status'].upper()}"
        )

        if fixture["status"] == "played":
            original = next(
                item for item in fixtures
                if item["id"] == fixture["id"]
            )
            print(
                f"  Score: {original['home_score']} - "
                f"{original['away_score']}"
            )


def show_standings(teams, fixtures):
    if not teams:
        print("Register teams first.")
        return

    standings = calculate_standings(teams, fixtures)

    print("\n========== LEAGUE TABLE ==========")
    print(
        f"{'Team':<15} {'P':<3} {'W':<3} {'D':<3} "
        f"{'L':<3} {'GF':<4} {'GA':<4} {'GD':<4} {'PTS':<4}"
    )

    for team in standings:
        print(
            f"{team['name']:<15} "
            f"{team['played']:<3} "
            f"{team['wins']:<3} "
            f"{team['draws']:<3} "
            f"{team['losses']:<3} "
            f"{team['goals_for']:<4} "
            f"{team['goals_against']:<4} "
            f"{team['goal_difference']:<4} "
            f"{team['points']:<4}"
        )

    print("==================================")


def simulate_demo(teams, fixtures):
    """Run a demo using a repeatable random seed."""

    if not teams:
        demo_names = ["Falcons", "Titans", "Phoenix", "Warriors"]

        for name in demo_names:
            register_team(teams, name)

    if not fixtures:
        fixtures.extend(generate_fixtures(teams))

    rng = random.Random(42)

    for fixture in fixtures:
        if fixture["status"] == "pending":
            home_score = rng.randint(0, 5)
            away_score = rng.randint(0, 5)

            record_result(
                fixtures,
                fixture["id"],
                home_score,
                away_score
            )

    print("Demo tournament simulation completed.")


def run():
    teams = []
    fixtures = []

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        try:

            if choice == "1":
                name = input("Enter team name: ")

                team = register_team(teams, name)

                print(f"Team registered successfully: {team['name']}")

            elif choice == "2":
                show_teams(list_teams(teams))

            elif choice == "3":
                if fixtures:
                    print("Fixtures have already been generated.")
                else:
                    fixtures.extend(generate_fixtures(teams))
                    print(f"{len(fixtures)} fixtures generated.")

            elif choice == "4":
                show_fixtures(fixtures, teams)

            elif choice == "5":
                fixture_id = input("Enter fixture ID: ").strip()

                home_score = int(input("Enter home team score: "))
                away_score = int(input("Enter away team score: "))

                record_result(
                    fixtures,
                    fixture_id,
                    home_score,
                    away_score
                )

                print("Match result recorded successfully.")

            elif choice == "6":
                show_standings(teams, fixtures)

            elif choice == "7":
                save_tournament(teams, fixtures)
                print("Tournament saved successfully.")

            elif choice == "8":
                loaded_teams, loaded_fixtures = load_tournament()

                teams.clear()
                teams.extend(loaded_teams)

                fixtures.clear()
                fixtures.extend(loaded_fixtures)

                print("Tournament loaded successfully.")

            elif choice == "9":
                simulate_demo(teams, fixtures)

            elif choice == "10":
                champion = get_champion(teams, fixtures)

                if champion is None:
                    print("There is no champion yet.")
                    print("Complete all fixtures first.")
                else:
                    print(
                        f"TOURNAMENT CHAMPION: "
                        f"{champion['name']}"
                    )

            elif choice == "0":
                print("Thank you for using TournamentLab!")
                break

            else:
                print("Invalid option. Please choose from the menu.")

        except ValueError as error:
            print(f"Error: {error}")

        except FileNotFoundError as error:
            print(f"Error: {error}")

        except EOFError:
            print("\nInput ended. Exiting TournamentLab.")
            break
