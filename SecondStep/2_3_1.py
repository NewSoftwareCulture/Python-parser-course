import xlrd

path = 'resource/trekking1.xlsx'

def get_table(page):
    table = []
    for i in range(1, page.nrows):
        product = page.row_values(i)[0]
        kkal = page.row_values(i)[1]
        bel = page.row_values(i)[2]
        fat = page.row_values(i)[3]
        carb = page.row_values(i)[4]
        # print(product + ' ' + str(kkal) + ' ' + str(bel) + ' ' + str(fat) + ' ' + str(carb))
        pos = [product, kkal, bel, fat, carb]
        table.append(pos)
    return table


wb = xlrd.open_workbook(path)
page = wb.sheet_by_index(0)

table = get_table(page)

table.sort(key=lambda x: (-x[1], x[0]))

for i in table:
    print(i[0])