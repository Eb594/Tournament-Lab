def register_team(teams, name):
    """Register a team after validating its name."""

    if not isinstance(name, str):
        raise ValueError("Team name must be text.")

    name = name.strip()

    if len(name) < 2:
        raise ValueError("Team name must contain at least 2 characters.")

    if len(name) > 30:
        raise ValueError("Team name cannot exceed 30 characters.")

    # Check for duplicate names, ignoring letter case.
    for team in teams:
        if team["name"].casefold() == name.casefold():
            raise ValueError("A team with this name already exists.")

    if len(teams) >= 8:
        raise ValueError("A tournament cannot have more than 8 teams.")

    team_id = f"TM{len(teams) + 1:03d}"

    new_team = {
        "id": team_id,
        "name": name
    }

    teams.append(new_team)

    return new_team


def list_teams(teams):
    """Return all registered teams."""

    return teams.copy()
