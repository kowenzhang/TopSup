from fuzzywuzzy import process
from fuzzywuzzy import fuzz

# 加载题库文件
with open('./tiku.txt', 'r') as file:
    lines = file.readlines()


def find_match(question):
    print('=' * 20)
    # match = process.extractOne(question, lines)
    match = process.extractOne(question, lines, scorer=fuzz.token_sort_ratio)
    if match[1] == 0:
        print('该死，题库没有，看着办吧！')
    else:
        print_match(match)


def find_matches(question):
    print('=' * 20)
    matchs = process.extract(question, lines, limit=3, scorer=fuzz.token_sort_ratio)
    # matchs = process.extract(question, lines, limit=3)
    print(matchs)
    for match in matchs:
        print_match(match)
        print('-'*20)


def print_match(match):
    index = lines.index(match[0])
    print('第{0}行：匹配度{1}'.format(index, match[1]))
    print(lines[index])
    print(lines[index + 1])
    print(lines[index + 2])
    print(lines[index + 3])
    print(lines[index + 4])


print('=' * 20)
