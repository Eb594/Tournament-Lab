def record_result(fixtures, fixture_id, home_score, away_score):
    """Record a result for a pending fixture."""

    # Find the fixture.
    selected_fixture = None

    for fixture in fixtures:
        if fixture["id"] == fixture_id:
            selected_fixture = fixture
            break

    if selected_fixture is None:
        raise ValueError("Fixture not found.")

    # Prevent duplicate result submissions.
    if selected_fixture["status"] == "played":
        raise ValueError("This fixture has already been played.")

    # Validate scores.
    for score in (home_score, away_score):
        if type(score) is not int or score < 0:
            raise ValueError("Scores must be nonnegative integers.")

    # Update the fixture only after validation.
    selected_fixture["home_score"] = home_score
    selected_fixture["away_score"] = away_score
    selected_fixture["status"] = "played"

    return selected_fixture
