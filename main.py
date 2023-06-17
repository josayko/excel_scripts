import sys
import re
import pandas as pd

def parse(file_name, sheet_name=0, row_type="LOT"):
    df = pd.read_excel(
        file_name, sheet_name, header=1
    ).fillna("")

    df_dic = df.to_dict()
    typs = []

    for typ in df_dic["Unnamed: 0"].values():
        if not typ:
            break
        typs.append(typ)

    # print(typs)
    regex = re.compile(r"^Unnamed.*")
    data = {str(key): value for key, value in df_dic.items() if not regex.match(str(key))}
    res = {}

    for key in data:
        vals = list(data[key].values())[:len(typs)]
        comb = tuple(zip(typs, vals))
        if comb not in res:
            res[comb] = [str(key)]
        else:
            res[comb].append(str(key))

    # print(res)

    for key in res.keys():
        types = []
        for t in key:
            if (t[1]):
                types.append(t[0])

        if types:
            if row_type == "LOT":
                lots = f"LOT={','.join(res[key])}"
                types = f"TYP={','.join(types)}"
            else:
                lots = f"LOT={','.join(types)}"
                types = f"TYP={','.join(res[key])}"

            print(f"{lots};{types}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse(*sys.argv[1:])

