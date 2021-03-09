number = input('請輸入密碼：')
x = 3
while True:
	if number == 'asd5200529':
		print('登入成功')
		break
	else:
		x = x - 1
		print('您輸入的密碼錯誤,還有', x, '次機會')
		number = input('請輸入密碼：')
		if x == 0:
			print('密碼輸入錯誤')
			break

					

		