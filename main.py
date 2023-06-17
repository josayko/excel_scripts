import sys
import re
import pandas as pd


def compute_results(res):
    for key in res.keys():
        types = []
        for t in key:
            if t[1]:
                types.append(t[0])
        if types:
            print(f"LOT={','.join(res[key])};TYP={','.join(types)}")


def parse_lot_column(rows, data):
    res = {}
    for key in data:
        vals = list(data[key].values())[: len(rows)]
        comb = tuple(zip(rows, vals))
        if comb not in res:
            res[comb] = [str(key)]
        else:
            res[comb].append(str(key))

    compute_results(res)


def parse_lot_row(rows, data):
    res = {}
    col_vals = [list(x.values()) for x in data.values()]
    row_vals = zip(*col_vals)

    for index, vals in enumerate(row_vals):
        comb = tuple(zip(data.keys(), vals))
        if comb not in res:
            res[comb] = [str(rows[index])]
        else:
            res[comb].append(str(rows[index]))

    compute_results(res)


def parse(file_name, sheet_name=0, lot_direction="col"):
    df = pd.read_excel(file_name, sheet_name, header=1).fillna("")
    df_dic = df.to_dict()
    rows = []

    for typ in df_dic["Unnamed: 0"].values():
        if not typ:
            break
        rows.append(typ)

    regex = re.compile(r"^Unnamed.*")
    data = {
        str(key): value for key, value in df_dic.items() if not regex.match(str(key))
    }
    if lot_direction.lower() == "row":
        parse_lot_row(rows, data)
    else:
        parse_lot_column(rows, data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse(*sys.argv[1:])
