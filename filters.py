from functools import reduce

def run():
    reduceNums(addValues())

def filterNums(list_nums):
    odd = list(filter(lambda x: x%2 != 0, list_nums))
    print(odd)

def mapNums(list_nums):
    squares = list(map(lambda x: x**2, list_nums))
    print(squares)

def reduceNums(list_nums):
    all_multiplied = reduce(lambda a, b: a * b, list_nums)
    print(all_multiplied)

def addValues():
    return [i for i in range(1, 101)]

if __name__ == '__main__':
    run()