# coding: utf8
print 。
with open("zh_sampl.txt", 'r') as file:
    newf = open("zh_sample.txt", 'w')
    for line in file:
        for char in line:
            if char != '。':
                newf.write(char)
