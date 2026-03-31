def mainProgram():
    num = int(input('Number (whole): '))

    numbers = []

    def multiply(n):
        numbers.append(n)
        for i in range(9):
            j = numbers[i] * 2
            numbers.append(j)
            i += 1

    multiply(num)
    print(numbers)

def restart():
    while True:
        cont = input('Start Program Again? (y/N): ').lower()

        if cont in ['yes', 'y']:
            return True
        elif cont in ['no', 'n']:
            return False
        else:
            print('Invalid input')

while True:
    mainProgram()
    if not restart():
        print('Stopping Program')
        break
