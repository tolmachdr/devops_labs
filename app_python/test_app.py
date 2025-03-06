from fastapi.testclient import TestClient
from main import app
import pytz
from datetime import datetime
from unittest.mock import patch
import os

client = TestClient(app)


def get_time():
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone)
    return time


def test_get():
    with patch("main.VISITS_FILE", "/tmp/visits.txt"):
        if not os.path.exists("/tmp/visits.txt"):
            with open("/tmp/visits.txt", "w") as f:
                f.write("0")

        response = client.get("/")
        assert response.status_code == 200

        assert "moscow_time" in response.json()
        assert response.json()["moscow_time"] is not None

        response_time = datetime.fromisoformat(response.json()["moscow_time"])
        current_time = get_time()

        time_diff = abs(current_time - response_time).total_seconds()
        assert time_diff < 2
