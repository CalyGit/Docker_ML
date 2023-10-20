# Import required libraries
from fastapi import FastAPI, HTTPException, Form, Depends
from pydantic import BaseModel
import uvicorn
import joblib
import pandas as pd


# Load the pre-trained pipeline
model = joblib.load('../dev/pipelin.pkl')

# Create a FASTAPI app
app = FastAPI(
    title="Sepsis Prediction API"
)

@app.get("/")
async def root():
    return {
        "info": "Welcome to the Sepsis Prediction API! This API predicts the probability of a patient having sepsis based on their vitals."
    }

# Define a Pydantic model for input data
class Sepsis(BaseModel):
    plasma_glucose: float
    blood_work_result_1: float
    blood_pressure: float
    blood_work_result_2: float
    blood_work_result_3: float
    body_mass_index: float
    blood_work_result_4: float
    Age: int
    Insurance: int

    @classmethod
    def as_form(
        cls,
        plasma_glucose: float = Form(...),
        blood_work_result_1: float = Form(...),
        blood_pressure: float = Form(...),
        blood_work_result_2: float = Form(...),
        blood_work_result_3: float = Form(...),
        body_mass_index: float = Form(...),
        blood_work_result_4: float = Form(...),
        Age: int = Form(...),
        Insurance: int = Form(...)
    ):
        return cls(
            plasma_glucose=plasma_glucose,
            blood_work_result_1=blood_work_result_1,
            blood_pressure=blood_pressure,
            blood_work_result_2=blood_work_result_2,
            blood_work_result_3=blood_work_result_3,
            body_mass_index=body_mass_index,
            blood_work_result_4=blood_work_result_4,
            Age=Age,
            Insurance=Insurance
        )

# Define a route for prediction
@app.post("/predict/")
async def create_dataframe(form_data: Sepsis = Depends(Sepsis.as_form)):
    try:
        # Convert the form data to a data frame
        df = pd.DataFrame(form_data.dict(), index=[0])

        # Predicting
        output = model.predict_proba(df)
               
        df["predicted_label"] = output.argmax(axis=-1)
        mapping = {0: "Sepsis Negative", 1: "Sepsis Positive"}
        df["predicted_label"] = [mapping[x] for x in df["predicted_label"]]

        # Calculating confidence score
        confidence_score = output.max(axis=-1)
        df["confidence_score"] = f"{round((confidence_score[0] * 100), 2)}%"
        
        # Creating a display output
        msg = "Execution Successful!"
        code = 1
        pred = df.to_dict("records")

        result = {"Execution Message": msg, "Execution Code": code, "Prediction": pred}

    except Exception as e:
        # If there is an error...
        msg = "Execution failed!"
        code = 0
        pred = None

        result = {"Error": str(e), "Execution Message": msg, "Execution Code": code, "Prediction": pred }

    return result

# Run the FASTAPI application
if __name__ == "__main":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)




