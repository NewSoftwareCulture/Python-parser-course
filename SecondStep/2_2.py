import xlrd

path = 'resource/salaries.xlsx'


def get_medians(page):
    cities = {}
    for i in range(1,8):
        city = page.row_values(i)[0]
        values = page.row_values(i)[1:8]
        values.sort()
        median_val = int(values[3])
        cities[median_val] = city
    return cities

def get_profs(page):
    profs = {}
    for i in range(1,8):
        prof = page.row_values(0)[i]
        sum = 0
        for j in range(1,8):
            sum += page.row_values(j)[i]
        # cities[value] = city
        value = sum/7
        profs[value] = prof
    return profs



wb = xlrd.open_workbook(path)
page = wb.sheet_by_index(0)
median = get_medians(page)
max_v_m = max(median.keys())

profs = get_profs(page)
max_v_p = max(profs.keys())

print(median[max_v_m] + ' ' + profs[max_v_p])