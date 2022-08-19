def getNum():
    try:
        num = int(input('Enter a number: '))
        divisrs_list = divisors(num)
        print(divisrs_list)
        print('End of algorithm')
    except ValueError:
        print('Only numbers are allowed')

def divisors(num):
    try:
        if num < 0:
            raise ValueError('Only positive numbers allowed')
        return [divisor for divisor in range(1, num+1) if num % divisor == 0]
    except ValueError as ve:
        print(ve)
        return False

def run():
    getNum()

if __name__ == '__main__':
    run()