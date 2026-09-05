from analyzer.models import ProjectAnalysis, EffortEstimate

def test_project_analysis():
    analysis = ProjectAnalysis(
        project_type="Web Application",
        summary="A web application for managing tasks.",

        requirements=[
            "User authentication", 
            "Task management", 
            "Notifications"
        ],

        complexity="medium",

        missing_information=[
            "Database schema", 
            "API endpoints"
        ],

        clarifying_questions=[
            "What is the expected user load?", 
            "Are there any specific security requirements?"
        ],

        estimated_effort=EffortEstimate(min_hours=100, max_hours=200),

        assumptions=[
            "Standard web application architecture"
        ],

        confidence="medium"
    )

    assert analysis.complexity == "medium"
    assert analysis.estimated_effort.min_hours == 100