import sys

input = sys.stdin.readline
N = int(input())
number_card = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))

def check_card(card):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if number_card[mid] == card:
            return 1
        elif card < number_card[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0

for card in cards:
    print(check_card(card), end= " ")