# import requests as req

# response = req.get('https://api.sandbox.midtrans.com/v2/token?card_number=4617%200069%205974%206656&card_cvv=123&card_exp_month=01&card_exp_year=2020&client_key=SB-Mid-client-iCkHzDAZ038U9GzK&')
# response_dict = response.json()
# token = response_dict.get('token_id')
# print(token)
import math


def print_lyric():
    print('Hello')
    print('World')


def repeat_lyric():
    print_lyric()
    print_lyric()


def print_twice(stuff):
    print(stuff)
    print(stuff)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


line1 = 'Bing tiddle '
line2 = 'Tiddle bang'
cat_twice(line1, line2)

input = [1, 2, 22, 1, 2, 3, 4, 0]
while x >= 0:
    print(input[x])
#     if x <= a:
#         z += 1
#         a = x = int(input())
# print(z - 1)
