import random
import sys

HANDS = ['グー', 'チョキ', 'パー']


def play():
    # print('じゃんけんぽん！')

    while True:
        # print('あいこでしょ！')
        player_hand = random.choice(HANDS)
        opponent_hand = random.choice(HANDS)

        result = None
        if player_hand == 'グー':
            if opponent_hand == 'チョキ':
                result = True
            elif opponent_hand == 'パー':
                result = False
        elif player_hand == 'チョキ':
            if opponent_hand == 'グー':
                result = False
            elif opponent_hand == 'パー':
                result = True
        elif player_hand == 'パー':
            if opponent_hand == 'グー':
                result = True
            elif opponent_hand == 'チョキ':
                result = False

        if result is None:
            print(f"{player_hand} vs {opponent_hand} ... あいこ")
        else:
            print(f"{player_hand} vs {opponent_hand} ... {'勝ち' if result else '負け'}")
            return result


def main():
    args = sys.argv
    if len(args) >= 2:
        repeat_times = int(args[1])
    else:
        repeat_times = 10

    # じゃんけん実行
    win = 0
    lose = 0
    for _ in range(repeat_times):
        result = play()
        if result:
            win += 1
        else:
            lose += 1

    print(f'結果は あなたの{win}勝、相手の{lose}勝でした。')


if __name__ == '__main__':
    main()
