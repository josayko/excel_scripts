import sys
import re
import pandas as pd


def compute_results(mapping):
    for pattern in mapping.keys():
        types = []
        for t in pattern:
            if t[1]:
                types.append(t[0])
        if types:
            print(f"LOT={','.join(mapping[pattern])};TYP={','.join(types)}")


def parse_by_type(types, data):
    res = {}
    for lot in data:
        vals = list(data[lot].values())[: len(types)]
        comb = tuple(zip(types, vals))
        if comb not in res:
            res[comb] = [str(lot)]
        else:
            res[comb].append(str(lot))

    compute_results(res)


def parse_by_lot(lots, data):
    mapping = {}
    col_vals = [list(x.values()) for x in data.values()]
    row_vals = zip(*col_vals)

    for index, vals in enumerate(row_vals):
        pattern = tuple(zip(data.keys(), vals))
        if pattern not in mapping:
            mapping[pattern] = [str(lots[index])]
        else:
            mapping[pattern].append(str(lots[index]))

    compute_results(mapping)


def parse(file_name, sheet_name=None, parse_by="lot"):
    df = pd.read_excel(file_name, sheet_name, header=1)

    for sheet in df.items():
        df_dic = sheet[1].fillna("").to_dict()
        row_headers = []

        for value in df_dic["Unnamed: 0"].values():
            if not value:
                break
            row_headers.append(value)

        regex = re.compile(r"^Unnamed.*")
        data = {
            str(key): value for key, value in df_dic.items() if not regex.match(str(key))
        }

        print(sheet[0])
        if parse_by.lower() == "lot":
            parse_by_lot(row_headers, data)
        else:
            parse_by_type(row_headers, data)
        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse(*sys.argv[1:])
