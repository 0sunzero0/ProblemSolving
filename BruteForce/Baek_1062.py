from itertools import combinations

N, K = map(int, input().split())
words = [list(input()) for _ in range(N)]

alphabet = [chr(n + 97) for n in range(0, 26)]
alphabet.remove('a')
alphabet.remove('c')
alphabet.remove('i')
alphabet.remove('n')
alphabet.remove('t')

max_word_num = 0

def get_word_num(case):
    dict = {'a': 1, 'c': 1, 'i': 1, 'n': 1, 't': 1}
    count = 0

    for select_word in case:
        dict[select_word] = 1
    for word in words:
        is_readable = True
        check_words = word[4:-4]
        for check_word in check_words:
            if check_word not in dict:
                is_readable = False
        if is_readable:
            count += 1
    return count

if K < 5:
    print(0)
else:
    cases = list(combinations(alphabet, K - 5))
    for case in cases:
        max_word_num = max(get_word_num(case), max_word_num)
    print(max_word_num)

'''
3 6
antarctica
antahellotica
antacartica
'''
