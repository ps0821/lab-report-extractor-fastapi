from pydantic import BaseModel
from typing import List, Optional

class LabTest(BaseModel):
    lab_test_name: str
    lab_test_value: str
    bio_reference_range: str
    lab_test_out_of_range: bool

class LabTestResponse(BaseModel):
    is_success: bool
    data: Optional[List[LabTest]] = None
    error: Optional[str] = None

