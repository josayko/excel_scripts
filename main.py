import sys
import pandas as pd

def parse(filename):
    df = pd.read_excel(
        filename, header=1
    ).fillna("")

    data = df.to_dict()
    typs = []

    for typ in data["Unnamed: 0"].values():
        if not typ:
            break
        typs.append(typ)

    # print(typs)

    res = {}

    for col in range(1, len(data) - 1):
        vals = list(data[col].values())[:len(typs)]
        comb = tuple(zip(typs, vals))
        if comb not in res:
            res[comb] = [str(col)]
        else:
            res[comb].append(str(col))

    # print(res)

    for key in res.keys():
        types = []
        for t in key:
            if (t[1]):
                types.append(t[0])

        if types:
            print(f"LOT={','.join(res[key])};TYP={','.join(types)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse(sys.argv[1])
