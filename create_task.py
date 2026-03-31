def mainProgram():
    def fibonacciSeq(n):
        series = []

        if n <= 0:
            print('Positive number of terms')
            return
        
        a = 0
        b = 1
        series.append(a)
        series.append(b)
        print(f"Fibonacci series with {n} terms:")

        if n == 1:
            print(series[0])
            return
        
        for _ in range(2, n):
            next_term = a + b
            series.append(next_term)
            a = b
            b = next_term

        print(series)

    print('Fibonacci series generator') 
    num_terms = int(input('Number of terms (positive wholes): '))
    fibonacciSeq(num_terms)

def restart():
    while True:
        cont = input('Start Program Again? (y/N): ').lower()
        if cont in ['yes', 'y']:
            return True
        elif cont in ['no', 'n', '']:
            return False
        else:
            print('Invalid input')

while True:
    mainProgram()
    if not restart():
        print('Stopping Program')
        break
