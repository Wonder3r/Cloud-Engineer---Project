import pandas as pd
import random

def generate_patient_data(rows=1000):

    data = {
        "PatientID": [f"P{str(i).zfill(4)}" for i in range(1, rows + 1)], ##Patient IDs from P0001 to P1000
        "Age": [random.randint(18, 90) for _ in range(rows)], ## Ages from 18 to 90
        "BMI": [round(random.uniform(18, 35), 2) for _ in range(rows)], ## BMI values from 18 to 35
        "ChronicCondition": [random.choice(['Diabetes', 'Hypertension', 'None']) for _ in range(rows)], ## Chronic conditions: Diabetes, Hypertension, or None

    }

    df = pd.DataFrame(data) ## Create a DataFrame from the data dictionary
    df.to_csv("patient_data.csv", index=False) ## Save the DataFrame to a CSV file

generate_patient_data() ## Call the function to generate patient data
print("Patient data generated and saved to patient_data.csv") ## Print confirmation message