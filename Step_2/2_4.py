import xlrd

def get_answer():
    table = []
    for i in range(1, 1001):
        path = 'resource/2_4/' + str(i) + '.xlsx'
        wb = xlrd.open_workbook(path)
        page = wb.sheet_by_index(0)
        name = page.row_values(1)[1] 
        gold = int(page.row_values(1)[3])
        table.append([name, gold])
    return table

def form(table):
    result = ''
    for i in range(1000):
        result += table[i][0] + ' ' + str(table[i][1]) + '\n'
    return result[0:-1]

table = get_answer()
table.sort()
result = form(table)

f = open('answer.txt', 'w', encoding='utf-8')
f.write(result)
f.close()