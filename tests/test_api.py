from unittest.mock import patch

from fastapi.testclient import TestClient

from analyzer.main import app
from analyzer.models import EffortEstimate, ProjectAnalysis


client = TestClient(app)


def test_analyze_endpoint():
    fake_analysis = ProjectAnalysis(
        project_type="Web Application",
        summary="A test web application.",
        requirements=["Manage customer orders"],
        complexity="low",
        missing_information=["Number of users"],
        clarifying_questions=["How many users are expected?"],
        estimated_effort=EffortEstimate(
            min_hours=80,
            max_hours=160,
        ),
        assumptions=["Basic web application"],
        confidence="medium",
    )

    with patch(
        "analyzer.main.analyze_request",
        return_value=fake_analysis,
    ):
        response = client.post(
            "/analyze",
            json={
                "request": "We need a simple web application for managing customer orders."
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["project_type"] == "Web Application"
    assert data["complexity"] == "low"
    assert data["estimated_effort"]["min_hours"] == 80
    assert data["estimated_effort"]["max_hours"] == 160

def test_analyze_endpoint_invalid_request():
    response = client.post(
        "/analyze",
        json={
            "foo": "bar"
        },
    )

    assert response.status_code == 422