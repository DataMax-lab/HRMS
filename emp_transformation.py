import pandas as pd
import duckdb

emp_path  = r'D:\DataMax\Data\emp.csv'
df_emp  = pd.read_csv(emp_path)

sql = f"""
select deptno, count(1) dp_count
from   df_emp
group by deptno,jobname11
"""
df_emp_trf = duckdb.sql(sql)
df_emp_trf = df_emp_trf.to_df()
print(df_emp_trf)