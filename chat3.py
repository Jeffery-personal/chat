# 當對話記錄時間與人名連在一起時, 該如何分割 ?
# 字串也可以當成清單來看待

lines = []
with open('3.txt', 'r', encoding = 'UTF-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(time)
    print(name)