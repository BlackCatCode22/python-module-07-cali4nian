# Hyena class
class Hyena:
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

    make_sound = "hahaha, I'm a hyena"

    def create_hyena_item(self):
        return self.animal_id + ";" + self.name + "; birthdate: " + str(self.birthdate) + ";" + self.color + ";" + self.sex + ";" + self.weight + ";" + self.originating_zoo + "; arrived " + str(self.date_arrival)