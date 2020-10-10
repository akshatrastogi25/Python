import pandas as pd

print pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None]))