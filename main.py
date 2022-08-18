def run():
    clasificationNums()

def clasificationNums():
    squares = [i**2 for i in range(1, 101) if i % 3 == 0]
    read(squares)

def read(list):
    for value in list:
        print(value)

if __name__ == '__main__':
    run()