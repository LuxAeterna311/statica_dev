import numpy as np 
import pandas as pd 

if __name__ != "__main__":
	rng = np.random.RandomState(0)
	df = pd.DataFrame(rng.uniform(0, 100, 45).reshape(15, 3), columns = list("ABC"))
	df = np.round(df, 3)

	desc_df = df.describe()
else:
	print("Этот файл не является рабочим")