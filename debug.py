import random

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
    print(random.randrange(50, 100)/100)

if __name__ == "__main__":
    main()
else:
    print("Импортирован модуль Debug")