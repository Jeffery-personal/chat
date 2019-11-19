def read_file(filename):
    lines= []
    with open(filename, 'r', encoding='UTF-8-SIG') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    # None 出場 !
    person = None # 要先宣告, 避免第一列不是人名
    for line in lines:
        print(line)

    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'UTF-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('-LINE-Viki.txt')
    lines = convert(lines)
    # write_file('abc.txt', lines)
    #print(new)

"""
奇怪的符號: \ufeff 是甚麼意思 ? 記事本自動存取的一種編碼資料, 經常被藏起來, 
如何去除 ? encoding='UTF-8-SIG'
['\ufeffAllen\n', '哈囉\n', '你好\n', 'Tom\n', '你好\n', '今天一樣是買三份雞肉飯嗎?\n', 'Allen\n', '對\n', '飲料一樣紅茶\n', 'Tom\n', '半糖去冰對不對\n', 'Allen
\n', '對，謝謝，我十分鐘後到']
"""

main()