import pandas as pd
import numpy as np
import os

os.system('cls');

df = pd.read_excel("C:\\Users\\TSRAJESH\\Downloads\\Employee.xlsx", index_col=None, usecols="B, AM, V, X, Y, Z");

mgr = (df['Job Profile'] == "Engineering Manager").sum();
assocmgr = (df['Job Profile'] == "Assoc Engineering Mgr").sum();
le =  (df['Job Profile'] == "Lead Engineer").sum();
srengr = (df['Job Profile'] == "Senior Engineer").sum();
engr = (df['Job Profile'] == "Engineer").sum();
assocengr = (df['Job Profile'] == "Associate Engineer").sum();

df['underpaid'] = np.where(df["Annual Rate LC"] < df["Full time Minimum"], 'True','False');

resultdf = df[df['underpaid'] == "True"];

print(resultdf);

mgr = (resultdf['Job Profile'] == "Engineering Manager").sum();
assocmgr = (resultdf['Job Profile'] == "Assoc Engineering Mgr").sum();
le = (resultdf['Job Profile'] == 'Lead Engineer').sum();
srengr = (resultdf['Job Profile'] == 'Senior Engineer').sum();
engr = (resultdf['Job Profile'] == 'Senior Engineer').sum();
assocengr = (resultdf['Job Profile'] == "Associate Engineer").sum();

print("Manager = ", mgr);
print("Assoc. Manager =", assocmgr);
print("Lead Engineer", le);
print("Senior Engineer", srengr);
print("Engineer", engr);
print("Associate Engineer",assocengr);

# resultdf.to_excel("C:\\Users\\TSRAJESH\\Downloads\Output.xlsx");
