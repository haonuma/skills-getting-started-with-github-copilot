from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    original_activities = deepcopy(activities)

    # Arrange: Reset in-memory state for test isolation.
    activities.clear()
    activities.update(deepcopy(original_activities))

    with TestClient(app) as test_client:
        yield test_client

    # Arrange: Restore original state after each test.
    activities.clear()
    activities.update(original_activities)
