# class Car():
#     model ="carrera"
#     color="Black"
#     style="Sedan"
#     wheels=4
    

class Car():
    wheels=4
    
    def __init__(self,make,color,style):
        self.make=make
        self.color=color
        self.style=style

    def show_description(self):
        return f"That car was a,{self.color} {self.style}"

    def change_gear(self):
        return f"Can you {self.change_gear}"
    
    def start_engine(self):
        return f"please {self.start_engine}"


