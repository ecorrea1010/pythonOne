def read():
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        numbers = [int(line) for line in f]
    print(numbers)


def write():
    names = ['Leidys', 'Garbancito', 'Eduardo', 'María', 'Carlos']
    with open('./files/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    write()

if __name__ == '__main__':
    run()