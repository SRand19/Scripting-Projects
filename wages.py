HourlyWage = float(input('Please input your average hourly wage: '))
NormalHours = float(input('Please input your amount of normal hours worked: '))
OvertimeHours = float(input('Please input the amount of overtime hours worked: '))
overtimePay = OvertimeHours*1.5
wages = HourlyWage*NormalHours + overtimePay
print('Your estimated pay is',wages)
