age=int(input('enter any age:-'))
sex=input('enter any sex:-')
num_of_day=int(input('enter any num:-'))
if age>=18 and age<=30 and sex=='m':
	amount=num_of_day*700
	print(amount)
if age>=18 and age<=30 and sex=='f':
	amount=num_of_day*750
	print(amount)
if age>=30 and age<=40 and sex=='m':
	amount=num_of_day*800
	print(amount)
if age>=30 and age<=40 and sex=='f':
	amount=num_of_day*800
	print(amount)
else:
	print('enter approciate age')