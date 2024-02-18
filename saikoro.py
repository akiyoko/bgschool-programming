import random
import sys


def main():
    args = sys.argv
    if len(args) >= 2:
        repeat_times = int(args[1])
    else:
        repeat_times = 100

    # 合計値
    total = 0
    for i in range(repeat_times):
        # サイコロを振って、目の値を変数に代入する
        eye = random.randint(1, 6)
        # 合計値に加える
        total += eye
        # 平均値を求める
        average = total / (i + 1)
        print(f'{i + 1: >5}回目は「{eye}」がでました。これまでの平均値は「{average:.10f}」です。')


if __name__ == '__main__':
    main()
