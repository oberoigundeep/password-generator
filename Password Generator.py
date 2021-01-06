import random

upper_content = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_content = 'abcdefghijklmnopqrstuvwxyz'
digits_content = '0123456789'
sp_chr_content = '`~!@#$%^&*()_-+={[]}|\\\'"<>?,./'
sample_space = ''

print('Password Generator')
len_pass = int(input('Enter the length of password required: '))
upper = input('Do you want upper case letter?(Yes/No): ')
lower = input('Do you want lower case letter?(Yes/No): ')
digit = input('Do you want Digits?(Yes/No): ')
sp_chr = input('Do you want Special Characters?(Yes/No): ')

if upper in 'YESyesYes':
	sample_space += upper_content
if lower in 'YesYESyes':
	sample_space += lower_content
if digit in 'YesYESyes':
	sample_space += digits_content
if sp_chr in 'YesYESyes':
	sample_space += sp_chr_content

print('Password:', end = '\t')

more = True
while more :
	new_pass = ''
	listrandom = random.sample(sample_space, len_pass)
	for x in range(len(listrandom)):
		new_pass += listrandom[x]
	print(new_pass)
	ask_more = input('Do you want another password(yes/no)? ')
	if ask_more in 'YESyes':
		more = True
		print('New Password:', end = '\t')
	else :
		more = False