from pydantic import BaseModel
from typing import List, Optional

class ToothResult(BaseModel):
    tooth_number: int
    condition: str
    confidence: float
    boundingBox: Optional[List[float]] = None # [x, y, w, h]

class ScanResult(BaseModel):
    quality_passed: bool
    quality_reason: Optional[str]
    teeth: List[ToothResult]
    overall_risk_score: float
    archetype: str

class AssociationRule(BaseModel):
    rule: str
    support: float
    confidence: float

class InsightsResponse(BaseModel):
    clusters: List[str]
    association_rules: List[AssociationRule]
