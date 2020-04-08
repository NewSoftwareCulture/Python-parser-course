import xlrd

path = 'resource/trekking3.xlsx'

def get_dict(page):
    products = {}
    for i in range(1, page.nrows):
        product = page.row_values(i)[0]
        kkal = page.row_values(i)[1]
        bel = page.row_values(i)[2]
        fat = page.row_values(i)[3]
        carb = page.row_values(i)[4]
        products[product] = [kkal, bel, fat, carb]
    return products

def get_sums(wb, table):
    page_2 = wb.sheet_by_index(1)
    kkal = 0
    bel = 0
    fat = 0
    carb = 0
    day = 1
    sums_per_day = {}
    for i in range(1, page_2.nrows):
        product = page_2.row_values(i)[1]
        mass = page_2.row_values(i)[2]
        params = table[product]
        kkal += (params[0] * mass/100)
        bel += (params[1] * mass/100)
        fat += (params[2] * mass/100)
        if params[3] != '':
            carb += (params[3] * mass/100)
        if i+1 == page_2.nrows or page_2.row_values(i+1)[0] != day:
            sums_per_day[day] = [int(kkal) , int(bel), int(fat), int(carb)]
            day += 1
            kkal = 0
            bel = 0
            fat = 0
            carb = 0
    return sums_per_day

wb = xlrd.open_workbook(path)
page_1 = wb.sheet_by_index(0)

table = get_dict(page_1)
sums_per_day = get_sums(wb, table)

for i in range(1, 10):
    print(str(sums_per_day[i][0]) + ' ' + str(sums_per_day[i][1]) + ' ' + str(sums_per_day[i][2]) + ' ' + str(sums_per_day[i][3]))