password = 'asd5200529'
x = 3
while x > 0:
	x = x - 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功')
		break
	else:
		if x > 0:
			print('您輸入的密碼錯誤還有', x, '次機會')
		else:	
			print('登入失敗!')
		
