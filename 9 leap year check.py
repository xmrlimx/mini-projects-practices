from datetime import datetime

while True:
	year = int(input('Nhập năm muốn check vào đây: '))
	try : 
		this_year = datetime(year,2,29)
		print('Năm %s là năm nhuận' % this_year.strftime("%Y"))
	except ValueError: 
		print('Năm %s không phải năm nhuận đâu em'% this_year.strftime("%Y"))