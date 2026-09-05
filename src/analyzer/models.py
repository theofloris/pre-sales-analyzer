from pydantic import BaseModel, Field
from typing import Literal

class EffortEstimate(BaseModel):
    min_hours: int = Field(ge=0)
    max_hours: int = Field(ge=0)

class ProjectAnalysis(BaseModel):
    project_type: str
    summary: str

    requirements: list[str]
    
    complexity: Literal["low", "medium", "high"]

    missing_information: list[str]

    clarifying_questions: list[str]

    estimated_effort: EffortEstimate

    assumptions: list[str]

    confidence: Literal["low", "medium", "high"]