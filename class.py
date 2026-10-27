class car:
    def __init__(self,model,year,color,for_sale): 
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
car1=car("benz",2024,"red",False)
print(car1.model)
car2=car("bmw",2016,"blue",True)
print(car2.color)
car3=car("audi",2022,"yellow",True)
print(car3.year)