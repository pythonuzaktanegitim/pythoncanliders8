class Cats:
    def __init__(self,name,color,owner):
        self.name = name
        self.color = color
        self.owner = owner
    
    def add_list(self):
        _list = []

cat = Cats("name_of_cat","color_of_cat","owner_of_cat")
print(cat.name,cat.color,cat.owner)
