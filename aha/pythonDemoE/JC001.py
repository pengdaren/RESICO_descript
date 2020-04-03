day = 0
daysList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
input_day = str(input('请输入年月日\n'))  #2012年11月11日
print(input_day.index('年'))
yearNum = int(input_day[0: input_day.index('年')])
monthNum = int(input_day[input_day.index('年')+1: input_day.index('月')])
dayNum = int(input_day[input_day.index('月')+1: input_day.index('日')])
if yearNum % 4 == 0:
    daysList[1] = 29
else:
    pass
if monthNum == 1:
    day = dayNum
else:
    for i in range(monthNum-1):
        day += daysList[i] + dayNum
print('这是今年的第%d天' % day)
