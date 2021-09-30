from datetime import datetime

CSE246_3 = [{
    'start': '2021, 1, 2, 8, 0, 0',
    'end': '2021, 1, 2, 10, 0, 0'
}, {
    'start': '2021, 1, 2, 10, 10, 0',
    'end': '2021, 1, 2, 11, 40, 0'
}, {
    'start': '2021, 1, 4, 10, 10, 0',
    'end': '2021, 1, 4, 11, 40, 0'
}]

date = 'sat, 10, 10'
date2 = 'sun, 10, 10'

formt = '%a, %H, %M'
format2 = '%Y, %m, %d, %H, %M, %S'
a = datetime.strptime(CSE246_3[0]['start'], format2)
b = datetime.strptime(CSE246_3[1]['start'], format2)
print(a < b)
