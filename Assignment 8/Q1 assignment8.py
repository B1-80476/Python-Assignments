
class Mobile():

    def __init__(self, ModelName, Company, Price):
        self.ModelName = ModelName
        self.Company = Company
        self.Price = Price


    def print_details(self):
        print(f"Modelname = {self.ModelName}")
        print(f"Company = {self.Company}")
        print(f"Price = {self.Price}")

    def can_afford(self):
        if self.Price > 150000:
            print("Not.. this is affordable")
        else:
            print("Yes.. this is affordable")

details = Mobile("Galaxy","Samsung",130000)
details.print_details()
details.can_afford()



