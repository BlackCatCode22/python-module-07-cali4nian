# Tiger class
class Tiger:
    # constructor
    def __init__(self, species, name, animal_id, birthdate, color, sex, weight, originating_zoo, date_arrival):
        self.species = species
        self.name = name
        self.animal_id = animal_id
        self.birthdate = birthdate
        self.color = color
        self.sex = sex
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.date_arrival = date_arrival
    # property
    make_sound = "rrrrroar, I'm a tiger"
    # method
    def create_tiger_item(self):
        return self.animal_id + ";" + self.name + "; birthdate: " + str(self.birthdate) + ";" + "sound: " + self.make_sound + ";" + self.color + ";" + self.sex + ";" + self.weight + ";" + self.originating_zoo + "; arrived " + str(self.date_arrival)