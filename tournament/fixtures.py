def generate_fixtures(teams, existing_fixtures=None):
    """Generate a single round-robin fixture list."""

    if not isinstance(teams, list):
        raise ValueError("Teams must be provided as a list.")

    if not 4 <= len(teams) <= 8:
        raise ValueError("A tournament requires between 4 and 8 teams.")

    if existing_fixtures:
        raise ValueError("Fixtures have already been generated.")

    fixtures = []
    match_number = 1

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):

            fixture = {
                "id": f"M{match_number:03d}",
                "home_id": teams[i]["id"],
                "away_id": teams[j]["id"],
                "status": "pending",
                "home_score": None,
                "away_score": None
            }

            fixtures.append(fixture)
            match_number += 1

    return fixtures


def list_fixtures(fixtures, teams):
    """Return fixtures with team names for display."""

    team_names = {
        team["id"]: team["name"]
        for team in teams
    }

    result = []

    for fixture in fixtures:
        result.append({
            "id": fixture["id"],
            "home": team_names[fixture["home_id"]],
            "away": team_names[fixture["away_id"]],
            "status": fixture["status"]
        })

    return result
