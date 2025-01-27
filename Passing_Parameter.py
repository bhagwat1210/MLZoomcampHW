import pandas as pd

def get_Input(student_input: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_input, columns = ['Student_id','age'])
    return df

print(get_Input([[1,15],[2,11],[3,11],[4,20]]))
