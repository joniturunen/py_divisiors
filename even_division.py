# Application asks a number from user and tells what are the divisiors for the number

class EvenDivision:
    def __init__(self):
        self.quit = False
        self.number = 0.0
        self.ask_input()
    
    def ask_input(self):
        while not self.quit:
            try:
                self.number = int(input(f"\nEnter a number: "))
                self.quit = False
                self.evenDivisors(self.number)

            except ValueError:
                print("Not an integer! Exiting...")  
                self.quit = True


    def evenDivisors(self, number):
        for i in range(1, number):
            if number % i == 0:
                print(f'{number} / {i} = {number // i}')



if __name__ == "__main__":
    prog = EvenDivision()