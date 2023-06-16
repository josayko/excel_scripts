import pandas as pd

df = pd.read_excel(
    "Copie de Matrice des VISA à compléter  BET SEDRI - CFO-GTB.xlsx", header=1
).fillna("")

data = df.to_dict()
typs = []

for typ in data["Unnamed: 0"].values():
    if not typ:
        break
    typs.append(typ)

print(typs)

for col in range(1, len(data) - 1):
    print(f'Lot {col}: ', list(data[col].values())[:len(typs)])


