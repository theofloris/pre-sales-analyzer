from analyzer.models import ProjectAnalysis
import ollama

def analyze_request(request: str) -> ProjectAnalysis:
    """
    Analyze the project request and return a structured analysis.
    """
    response=ollama.chat(
        model="gemma3",
        messages=[
            {
                "role": "system",
                "content": """
You are a pre-sales software requirements analyst.

Analyze the customer's request and extract only information
that is explicitly stated or can be reasonably inferred.

Do not design the entire software project.
Do not suggest technologies.
Do not provide a long explanation.

Return a structured analysis containing:
- project type
- short summary
- functional requirements
- missing information
- clarifying questions
- project complexity
- estimated effort
- confidence level
""",   
            },
            {
            "role": "user",
            "content": request
        },
        ],
        format=ProjectAnalysis.model_json_schema(),
    )
    return ProjectAnalysis.model_validate_json(
        response["message"]["content"]
    )