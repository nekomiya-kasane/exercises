from select import select
import sqlite3
import openpyxl
from functools import partial
import datetime

wb = openpyxl.load_workbook('banks.xlsx')
st = wb.active
db = sqlite3.connect('data.db')
cur = db.cursor()

letters = [chr(ord('A') + i) for i in range(ord('Z') - ord('A') + 1)]
numbers = list(range(len(letters)))


def get_history_capital(year, row):
    return "" if float(row["capital_history"][year - 2008]) < 0 else str(row["capital_history"][year - 2008])


def get_history_branches(year, row):
    return "" if float(row["branches_history"][year - 2008]) < 0 else str(row["branches_history"][year - 2008])


titles = {
    "公司名称": (lambda x: x["name"]),
    "银行股东": (lambda x: x["shareholder"]),
    "银行股东持股比重": (lambda x: str(x["shareholder_ratio"]) + "%"),
    "当期资本2008": (lambda x: partial(get_history_capital, 2008)(x)),
    "当期资本2009": (lambda x: partial(get_history_capital, 2009)(x)),
    "当期资本2010": (lambda x: partial(get_history_capital, 2010)(x)),
    "当期资本2011": (lambda x: partial(get_history_capital, 2011)(x)),
    "当期资本2012": (lambda x: partial(get_history_capital, 2012)(x)),
    "当期资本2013": (lambda x: partial(get_history_capital, 2013)(x)),
    "当期资本2014": (lambda x: partial(get_history_capital, 2014)(x)),
    "当期资本2015": (lambda x: partial(get_history_capital, 2015)(x)),
    "当期资本2016": (lambda x: partial(get_history_capital, 2016)(x)),
    "当期资本2017": (lambda x: partial(get_history_capital, 2017)(x)),
    "当期资本2018": (lambda x: partial(get_history_capital, 2018)(x)),
    "当期资本2019": (lambda x: partial(get_history_capital, 2019)(x)),
    "当期资本2020": (lambda x: partial(get_history_capital, 2020)(x)),
    "当期资本2021": (lambda x: partial(get_history_capital, 2021)(x)),
    "当期资本2022": (lambda x: partial(get_history_capital, 2022)(x)),
    "分支数量2008": (lambda x: partial(get_history_branches, 2008)(x)),
    "分支数量2009": (lambda x: partial(get_history_branches, 2009)(x)),
    "分支数量2010": (lambda x: partial(get_history_branches, 2010)(x)),
    "分支数量2011": (lambda x: partial(get_history_branches, 2011)(x)),
    "分支数量2012": (lambda x: partial(get_history_branches, 2012)(x)),
    "分支数量2013": (lambda x: partial(get_history_branches, 2013)(x)),
    "分支数量2014": (lambda x: partial(get_history_branches, 2014)(x)),
    "分支数量2015": (lambda x: partial(get_history_branches, 2015)(x)),
    "分支数量2016": (lambda x: partial(get_history_branches, 2016)(x)),
    "分支数量2017": (lambda x: partial(get_history_branches, 2017)(x)),
    "分支数量2018": (lambda x: partial(get_history_branches, 2018)(x)),
    "分支数量2019": (lambda x: partial(get_history_branches, 2019)(x)),
    "分支数量2020": (lambda x: partial(get_history_branches, 2020)(x)),
    "分支数量2021": (lambda x: partial(get_history_branches, 2021)(x)),
    "分支数量2022": (lambda x: partial(get_history_branches, 2022)(x)),
    "前任银行股东": (lambda x: x["ex_shareholder"] if x["ex_shareholder"] != 'None' else ''),
    "变更时间": (lambda x: x["shareholder_renew_time"] if (x["shareholder_renew_time"] == '-1') or (
                datetime.datetime.date(datetime.datetime.strptime(
                    x["shareholder_renew_time"], '%Y-%m-%d'))
                > datetime.date(1971, 1, 1)) else ''
             ),
    "经营状态": (lambda x: x["status"]),
    "法定代表人": (lambda x: x["legal_representative"]),
    "注册资本": (lambda x: (x["registered_capital"] if float(x["registered_capital"]) > 0 else '-') + '万人民币'),
    "实缴资本": (lambda x: (x["contributed_capital"] if float(x["contributed_capital"]) > 0 else '-') + '万人民币')
}
titles_raw = list(titles.keys())

selected = ["name", "shareholder", "shareholder_ratio",
            "capital_history", "branches_history", "ex_shareholder",
            "shareholder_renew_time", "status", "legal_representative",
            "registered_capital", "contributed_capital"
            ]

target_titles = [st._get_cell(row=1, column=i).value for i in range(1, 64)]
index_map = {key: target_titles.index(key) + 1 for key in list(titles.keys())}
columns = len(index_map)

bank_names = [st._get_cell(row=i, column=1).value for i in range(1, 2000)]


def process_row(row: dict):
    if not (row['name'] in bank_names):
        print('\033[31m {} not found in the worksheet.\033[0m '.format(
            row['name']))
        return
    for i in range(1, columns):
        st.cell(
            row=bank_names.index(row['name']) + 1,
            column=index_map[titles_raw[i]],
            value=titles[titles_raw[i]](row)
        )


def main():
    cur.execute("SELECT {} FROM 'company'".format(
        '"' + '","'.join(selected) + '"'))
    for _, row in enumerate(cur):
        row = {selected[i]: row[i] for i in range(len(row))}
        row["capital_history"] = eval(row["capital_history"])
        row["branches_history"] = eval(row["branches_history"])
        process_row(row)
    wb.save('result_banks.xlsx')
    db.close()


if __name__ == '__main__':
    main()
