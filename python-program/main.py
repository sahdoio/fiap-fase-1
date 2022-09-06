class Smoker:
    def __init__(self):
        self.totalYears      = input("Tempo como fumante (em anos)......: ")
        self.itemValue       = input("Valor do maço.......................: ")
        self.itemQuantity    = input("Quantidade de maços por dia.........: ")
        self.totalSpent      = float(self.totalYears) * 12 * 30 * float(self.itemQuantity) * float(self.itemValue)

    def exec(self):
        print('\n')

        if (self.totalSpent < 20000):
            print(f"Com o valor R$ {self.totalSpent}, você poderia ter dado entrada em um carro.")

        elif (self.totalSpent >= 20000 and self.totalSpent <= 50000):
            print(f"Com o valor R$ {self.totalSpent}, você poderia ter comprado um carro popular usado.")

        else:
            print(f"Com o valor R$ {self.totalSpent}, você poderia ter comprado um carro zero.")

smoker = Smoker()
smoker.exec()
