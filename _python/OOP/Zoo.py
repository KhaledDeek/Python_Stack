class Animals:
    def __init__(self , name , age , health_level , happiness_level):
        self.name = name 
        self.age = age 
        self.health_level = health_level
        self.happiness_level = happiness_level
    
    def display_info(self):
        print(f"{self.name}, 'Age = ' {self.age}, 'Happiness_level = '{self.happiness_level},'Health_level = '{self.health_level}"   ) 
    def feed(self):
        self.health_level+10
        self.happiness_level+10
    def __str__(self):
        return f"{self.name}, 'Age = ' {self.age}, 'Happiness_level = '{self.happiness_level},'Health_level = '{self.health_level}"    
        
class Tigers(Animals):
    def __init__(self, name, age, health_level, happiness_level , type_food):
        super().__init__(name, age, health_level, happiness_level)
        self.health_level = 80
        self.happiness_level = 75
        self.type_food = "meat"
    def feed(self):
        self.health_level+=7
        self.happiness_level+=6
        return self

class Lions(Animals):
    def __init__(self, name, age, health_level, happiness_level , type_food):
        super().__init__(name, age, health_level, happiness_level)
        self.health_level = 76
        self.happiness_level = 78
        self.type_food = "meat"
    def feed(self):
        self.health_level+=4
        self.happiness_level+=8
        return self

class Bears(Animals):
    def __init__(self, name, age, health_level, happiness_level , type_food):
        super().__init__(name, age, health_level, happiness_level)
        self.health_level = 90
        self.happiness_level = 83
        self.type_food = "vegetables"
    def feed(self):
        self.health_level+8
        self.happiness_level+7
        return self

masha = Bears("masha", 18 , 0 , 0 , "veges" )
mofasa = Lions("mofasa" , 20 , 0 , 0 , "meat")
zinker = Tigers("Zinkers" , 15 , 0 , 0 , "meat")
zinker.feed()
mofasa.feed()
masha.display_info()

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append(Lions(name , 50 , 0 , 0, 0 )) 
    def add_tiger(self, name):
        self.animals.append(Tigers(name , 50 , 0 , 0, 0 ))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def feed(self , animalno):
        for i in self.animals:
            self.animals[animalno].feed()
            i.display_info()
        return self
            
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
zoo1.feed(1)