class Calc:
    def __init__(self, filename):
        self.filename = filename

    def input(self):
        buffer = ""
        with open(self.filename, "w") as f:
            while buffer.upper() != "EXIT":
                try:
                    buffer = input("Enter a number (type 'EXIT' to finish)? ")
                    n = int(buffer)
                    f.write(buffer+"\n")                
                except ValueError:
                    pass

    def calc(self):
        with open(self.filename) as f:
            lines = f.readlines()
        
        numbers = [int(l) for l in lines]
        
        return sum(numbers)

def main():
    calc = Calc("FileCalc.txt")
    calc.input()
    print(calc.calc())


if __name__ == "__main__":
    main()