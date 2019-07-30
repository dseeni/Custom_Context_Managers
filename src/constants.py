# Files
fpersonal = 'data/personal_info.csv'
fcars = 'data/cars.csv'
fnames = fpersonal, fcars

# Parsers
personal_parser = (str, str, str, str, str)
cars_parser = (str, float, int, float, float, float, float, float, str)
parsers = personal_parser, cars_parser

# Named Tuple Class Names
personal_class_name = 'Personal_Info'
cars_class_name = 'Vehicle_Info'
class_names = personal_class_name, cars_class_name

