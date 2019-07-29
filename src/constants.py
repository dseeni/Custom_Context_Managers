# Files
fpersonal = 'data/personal_info.csv'
fcars = 'data/cars.csv'
fnames = fpersonal, fcars

# Parsers
personal_parser = (str, str, str, str, str)
# Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US
cars_parser = (str, float, int, float, float, float, float, float, str)
parsers = personal_parser, cars_parser

# Named Tuple Class Names
personal_class_name = 'Personal'
cars_class_name = 'Vehicle'
class_names = personal_class_name, cars_class_name

