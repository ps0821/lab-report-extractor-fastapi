from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils import extract_lab_tests
from app.models import LabTestResponse

app = FastAPI()

@app.post("/get-lab-tests", response_model=LabTestResponse)
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        
        with open("temp_image.png", "wb") as f:
            f.write(contents)

        
        lab_test_data = extract_lab_tests("temp_image.png")

        return JSONResponse(content={"is_success": True, "data": lab_test_data})

    except Exception as e:
        return JSONResponse(status_code=500, content={"is_success": False, "error": str(e)})

