import re

# content scrapped from https://www.simplilearn.com/aws-technical-essentials-free-practice-test
filedata = open("aws_fundamentals.txt", "r").read()

blocks = list(re.findall('(id=\"ques.*?\d{1,9}\. .*?)(?=<\/article>)', filedata, flags = re.M|re.S))

n = len(blocks)
ques = [None] * n
answ = [[] for x in range(n)]
option = [[] for x in range(n)]
explanation = [None] * n
data = '# AWS Fundamentals CheatSheet by [agavrel](http:\/\/www.github.com\/agavrel)\n'

for i in range(len(blocks)):
    pattern = 'id=\"ques.*?\d{1,9}\. (.*?)<\/b>'
    tmp = re.search(pattern, blocks[i], flags = re.M|re.S)
    if tmp:
        ques[i] = tmp.group(1)
    pattern = '<\/span>\n\t?(.*?) <\/label>'
    option[i] = list(re.findall(pattern, blocks[i], flags = re.M|re.S))
    pattern = '<label class="test-right-ans">.*?<\/span>\n\t?(.*?) <\/label>'
    answ[i] = re.search(pattern, blocks[i], flags = re.M|re.S).group(1)
    pattern = 'Explanation:<\/b>\n\t?<p>(.*)<\/p>'
    explanation[i] = re.search(pattern, blocks[i], flags = re.M|re.S)
    c = 97
    data += '\n### Question ' + str(i + 1) + ' - ' + ques[i] + '  \n' #print( '\n### Question ' + str(i + 1) + '\n' + ques[i])
    for f in option[i]:
        if f != answ[i]:
            data += '* ' + chr(c) + ') ' + f + '  \n' #print(chr(c) + ') ' + f)
        else:
            data += '* **' + chr(c) + ') ' + f + '**  \n'
        c += 1
    #data += '\n**' + answ[i] + '**' + '  \n'   # print('*' + f + '*')
    if explanation[i] and len(explanation[i].group(1)) > 4:
        data += '\n_' + explanation[i].group(1) + '_  ' # print(explanation[i])
    data += '<br/><br/><br/>\n'

with open('README.md', 'w') as f:
    f.write(data)
# re.I (ignore case), re.L (locale dependent), re.M (multi-line), re.S (dot matches all)
