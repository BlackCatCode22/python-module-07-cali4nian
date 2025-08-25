import datetime
import random
import re
import calendar


# What do they all have in common
class Animal:
    # CONSTRUCTOR
    def __init__(self):
        self.names_static_file = 'animalNames.txt'
        self.uni_number = '00'

    # METHODS

    def get_birthday(self, season, month, years_old):
        current_year = datetime.date.today().year
        age = int(re.findall(r'\d+', years_old)[0])
        birth_year = current_year - age
        num_of_days = calendar.monthrange(birth_year, month)[1]
        random_number = random.randint(0, num_of_days)
        return datetime.date(birth_year, month, random_number)

    def gen_birth_date(self,years_old, season):
        winter = ["Dec", "Jan", "Feb"]
        spring = ["March", "April", "May"]
        summer = ["Jun", "Jul", "Aug"]
        fall = ["Sep", "Oct", "Nov"]
        month_map = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
            'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        birth_date = None
        random_number = random.randint(0, 2)
        month = month_map[winter[random_number]]
        if 'winter' in season:
            birth_date = self.get_birthday("winter", month, years_old)
        if 'spring' in season:
            birth_date = self.get_birthday("spring", month, years_old)
        if 'summer' in season:
            birth_date = self.get_birthday("summer", month, years_old)
        if 'fall' in season:
            birth_date = self.get_birthday("fall", month, years_old)
        return birth_date

    # get number of uni id
    def get_num(self):
        number = None
        if int(self.uni_number) >= 1 and int(self.uni_number) < 10:
            number = '0' + str(self.uni_number)
            self.uni_number = int(self.uni_number) + 1
        if int(self.uni_number) >= 10:
            number = self.uni_number
            self.uni_number = int(self.uni_number) + 1
        if int(self.uni_number) == 0:
            number = str(self.uni_number)
            self.uni_number = int(self.uni_number) + 1
            return str(number)
        return str(number)

    # generate random ID
    def gen_unique_id(self, species, integer):
        return species[0].upper()+species[1]+str(integer)

    # get random name
    def get_name(self, species):
        with open(self.names_static_file, 'r') as file:
            animal_names = file.readlines()
        name_array = []
        for line in animal_names:
            cleaned_line = line.strip()
            if cleaned_line:
                name_array.append(line.strip())
        try:
            index = name_array.index(species + ' Names:')
            string = name_array[index + 1]
            list00 = [name.strip() for name in string.split(',')]
            return random.choice(list00)
        except ValueError:
            return "Error"

    # clean array data
    def clean_data(self, array):
        clean_array = []
        for item in array:
            item = item.strip()
            clean_array.append(item)
        return clean_array
