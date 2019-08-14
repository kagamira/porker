import random

#設定
suit_list = [0, 1, 2, 3]
Suit_list = ['S', 'C', 'D', 'H']
suit_hand = []
rank_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Rank_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
rank_hand = []
h = ""
H = []

i = 0

#手札5枚引く
while i < 5:
    num_s = random.choice(suit_list)    #ランダムにスートを抽出
    num_r = random.choice(rank_list)    #ランダムに番号を抽出
    suit_hand.append(num_s)
    rank_hand.append(num_r)
    H.append(Suit_list[num_s] + Rank_list[num_r])
    h = h + Suit_list[num_s] + Rank_list[num_r] + " "
    i += 1

H.sort()
print(H)
print(h)

#手札を引く関数
def card():
    i = 0
    h = ""
    while i < 5:
        num_s = random.choice(suit_list)    #ランダムにスートを抽出
        num_r = random.choice(rank_list)    #ランダムに番号を抽出
        suit_hand.append(num_s)
        rank_hand.append(num_r)
        H.append(Suit_list[num_s] + Rank_list[num_r])
        h = h + Suit_list[num_s] + Rank_list[num_r] + " "
        i += 1

#被りがないか調べる関数
def chk():
    print('chk')
    #rank_hand内の数字が被っていないか調べ、被っている数字の要素番号を記憶しsuit_handが同じかどうか調べる

#役を調べる関数
def hand():
    #ロイヤルストレートフラッシュがあるかどうかから調べていく
    print('hello')


