import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cartesian_product = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop(columns='key')
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    merged_data = cartesian_product.merge(exam_counts, how='left', on=['student_id', 'subject_name'])
    final_result = merged_data.fillna(0)[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(by=['student_id', 'subject_name'])
    return final_result
