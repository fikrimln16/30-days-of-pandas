import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diabetic_patients = patients[patients['conditions'].str.contains(r'\bDIAB1')][['patient_id', 'patient_name', 'conditions']]
    return diabetic_patients
