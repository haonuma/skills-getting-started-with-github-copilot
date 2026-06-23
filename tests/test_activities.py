from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_count = len(activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == expected_count
    assert "Chess Club" in payload
