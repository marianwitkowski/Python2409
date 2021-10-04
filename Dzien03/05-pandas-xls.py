
# Dostęp do XLS z Pandas
import pandas as pd

df : pd.DataFrame = pd.read_excel("../misc/uod-kopia.xlsx")
print(df.loc[0,"KUP"])
print(df.iloc[0,4])