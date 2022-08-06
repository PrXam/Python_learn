import datetime
import sys
import time


def main():
    date_beg = datetime.datetime.strptime('2020-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')
    date_end = datetime.datetime.strptime('2021-01-31 23:59:59', '%Y-%m-%d %H:%M:%S')
    total = 0
    with open("input.txt", "r") as file:
        line = file.readline()
        while line:
            date, sum = line.rsplit(' ', 1)
            sum = int(sum)
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            total += sum
            time_away = ((date - date_beg).total_seconds()) / 60
            speed_pay = total / time_away
            with open("output.txt", "a") as file1:
                file1.write(format(round(10000 - total - ((date_end - date).total_seconds() / 60) * speed_pay, 2), '.2f'))
                file1.write('\n')
            line = file.readline()


if __name__ == "__main__":
    main()