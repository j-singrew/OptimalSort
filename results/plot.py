import seaborn as sns
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv("CSV_PATH")
df = pd.read_csv(env)

print(df.head(10))


