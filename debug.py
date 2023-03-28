import random
from os import system
import time
from progress.bar import FillingSquaresBar

class dInfo:
    def __init__(self, name):
        self.name = name

class dInfo2(dInfo):
    def __init__(self, name, swallow):
        super().__init__(name)
        self.swallow = swallow


def debug():
    print("fuck my ass")


def main():
    print("Модуль стоит импортировать")
    bar = FillingSquaresBar('Progress', max=100, suffix='%(index)d%% / %(max)d%%')
    bar.color = 'red'
    bar.goto(10)
    bar.start
    for i in range(100):
        # Do some work
        bar.next()
        time.sleep(0.1)
    bar.goto(0)
    system('CLS')

if __name__ == "__main__":
    main()
else:
    print("Импортирован модуль Debug")