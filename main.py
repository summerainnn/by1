import re


def divide(word, ListsCopy):
    s = ''
    for i in range(0, len(word)):
        if re.match('\w|\.', word[i]):
            s = s + word[i]
            if i == len(word) - 1:
                ListsCopy.append(s)
        elif s != '':
            ListsCopy.append(s)
            ListsCopy.append(word[i])
            s = ''
        else:
            ListsCopy.append(word[i])
            s = ''


dic = {'begin': 1, 'end': 2, 'case': 3, 'const': 4, 'else': 5, 'for': 6, 'goto': 7, 'if': 8, 'while': 9, 'int': 10,
       'float': 11, 'char': 12, 'main': 13, 'return': 14, '+': 15, '-': 16, '*': 17, '/': 18, '>': 19, '<': 20, '=': 21,
       '(': 22, ')': 23, '{': 24, '}': 25, '[': 26, ']': 27, '&': 28, ',': 29,
       ';': 30, ':': 31, 'ID': 32
       }

print('读取的代码：')
with open("text.txt", "r") as af:
    data = af.read()
    print(data)

# 按照空格先进行切分
Lists = data.split()

ListsCopy = []
for i in range(len(Lists)):
    other = re.search('\W', Lists[i])
    if other is None:
        ListsCopy.append(Lists[i])
        continue
    divide(Lists[i], ListsCopy)

# print(ListsCopy)
output = []
fhList = []
nums = ['1','2','3','4','5','6','7','8','9','0']
for l in ListsCopy:
    if dic.__contains__(l):
        output.append((l, dic[l]))
    else:
        if l[0] in nums:
            if '.' in l:
                output.append((l, dic['float']))
            else:
                output.append((l, dic['int']))
        else:
            output.append((l,dic['ID']))
            if l in fhList:
                pass
            else:
                fhList.append(l)

print('----------------------------------------')
df = open('token.txt','w')
print('词法分析器输出单词：')
for out in output:
    df.write(str(out)+'\n')
    print(out)
df.close()
print('----------------------------------------')
ff = open('fh.txt','w')
print('词法分析器输出符号表：')
for i in range(len(fhList)):
    ff.write(str(i)+' '+fhList[i]+'\n')
    print(i,' '+fhList[i])
ff.close()
