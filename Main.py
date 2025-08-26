# imports
import datetime
from Animal import Animal
from Lion import Lion
from Tiger import Tiger
from Bear import Bear
from Hyena import Hyena
# files
arriving_animals = open('arrivingAnimals.txt')
animal_names= open('animalNames.txt')
# instances
animal = Animal()
# logic
# lists to separate animals by species
lion_list = []
tiger_list = []
bear_list = []
hyena_list = []
# for loop to loop through lines of text in arrivingAnimals.txt
lines = arriving_animals.readlines()
for line in lines:
    # split line by , into array
    line_array = line.split(',')
    # call clean_data to clean data
    clean_array = animal.clean_data(line_array)
    # create object based on if word is in first item in clean array, needs refactor for repetitive code but works
    sex = None
    if 'lion' in clean_array[0]:
        id_number = animal.get_num()
        species = "lion"
        name = animal.get_name('Lion')
        animal_id = animal.gen_unique_id(species, str(id_number))
        birthdate = animal.gen_birth_date(clean_array[0], clean_array[1])
        color = clean_array[2]
        sex = "female" if "female" in clean_array[0] else "male"
        weight = clean_array[3]
        originating_zoo = clean_array[4]+', '+clean_array[5]
        date_arrival = datetime.date.today()
        lion = Lion(species, name, animal_id, birthdate, color, sex, weight, originating_zoo, date_arrival)
        lion_list.append(lion.create_lion_item())
    if 'tiger' in clean_array[0]:
        id_number = animal.get_num()
        species = "tiger"
        name = animal.get_name('Tiger')
        animal_id = animal.gen_unique_id(species, str(id_number))
        birthdate = animal.gen_birth_date(clean_array[0], clean_array[1])
        color = clean_array[2]
        sex = "female" if "female" in clean_array[0] else "male"
        weight = clean_array[3]
        originating_zoo = clean_array[4] + ', ' + clean_array[5]
        date_arrival = datetime.date.today()
        tiger = Tiger(species, name, animal_id, birthdate, color, sex, weight, originating_zoo, date_arrival)
        tiger_list.append(tiger.create_tiger_item())
    if 'bear' in clean_array[0]:
        id_number = animal.get_num()
        species = "bear"
        name = animal.get_name('Bear')
        animal_id = animal.gen_unique_id(species, str(id_number))
        birthdate = animal.gen_birth_date(clean_array[0], clean_array[1])
        color = clean_array[2]
        sex = "female" if "female" in clean_array[0] else "male"
        weight = clean_array[3]
        originating_zoo = clean_array[4] + ', ' + clean_array[5]
        date_arrival = datetime.date.today()
        bear = Bear(species, name, animal_id, birthdate, color, sex, weight, originating_zoo, date_arrival)
        bear_list.append(bear.create_bear_item())
    if 'hyena' in clean_array[0]:
        id_number = animal.get_num()
        species = "hyena"
        name = animal.get_name('Hyena')
        animal_id = animal.gen_unique_id(species, str(id_number))
        birthdate = animal.gen_birth_date(clean_array[0], clean_array[1])
        color = clean_array[2]
        sex = "female" if "female" in clean_array[0] else "male"
        weight = clean_array[3]
        originating_zoo = clean_array[4] + ', ' + clean_array[5]
        date_arrival = datetime.date.today()
        hyena = Hyena(species, name, animal_id, birthdate, color, sex, weight, originating_zoo, date_arrival)
        hyena_list.append(hyena.create_hyena_item())
# The 'with' statement handles file closing automatically
# CREATE FILE
with open('zooPopulation.txt', 'w') as file:
    file.write("******* Zoo Population and Habitat Assignment Report *******\n")
    file.write("\n")
    file.write("Hyena Habitat:\n")
    file.write("\n")
    for hyena in hyena_list:
        file.write(hyena + "\n")
    file.write("\n")
    file.write("Lion Habitat:\n")
    file.write("\n")
    for lion in lion_list:
        file.write(lion + "\n")
    file.write("\n")
    file.write("Tiger Habitat:\n")
    file.write("\n")
    for tiger in tiger_list:
        file.write(tiger + "\n")
    file.write("\n")
    file.write("Bear Habitat:\n")
    file.write("\n")
    for bear in bear_list:
        file.write(bear + "\n")
    file.write("\n")
