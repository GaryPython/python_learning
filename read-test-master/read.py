#讀取檔案
#'r'讀,'w'寫
data = []
with open('food.txt', 'r') as f:#當作f
	for line in f:
		data.append(line.strip())#去掉多餘功能對字串
print(data)