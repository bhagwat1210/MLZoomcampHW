import pandas as pd
import numpy as np
# passing parameter
def get_Input(student_input: list[list[int]]): # it returns dataframe
    df = pd.DataFrame(student_input, columns = ['Student_id','age'])
    return df
print(get_Input([[1,15],[2,11],[3,11],[4,20]]))


## get number of rows and columns
def get_row_column(player: pd.DataFrame):
    return [len(player),len(player.columns)]

print(get_row_column(pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])))