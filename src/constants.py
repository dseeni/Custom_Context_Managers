from src.parse_utils import parse_date

# Files
fpersonal = 'data/personal_info.csv'
femployment = 'data/employment.csv'
fvehicles = 'data/vehicles.csv'
fupdate_status = 'data/update_status.csv'
fnames = fpersonal, femployment, fvehicles, fupdate_status

# Parsers
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicle_parser = (str, str, str, int)
update_status_parser = (str, parse_date, parse_date)
parsers = personal_parser, employment_parser, vehicle_parser, update_status_parser

# Compression Fileds Keys
personal_compress = (True, True, True, True, True)
employment_compress = (True, True, True, False)
vehicle_compress = (False, True, True, True)
update_status_compress = (False, True, True)
compress_fields = personal_compress, employment_compress, vehicle_compress, update_status_compress


# Named Tuple Class Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name

# Cut Off Date
cut_off_date = parse_date('2017-03-01T00:00:00Z')
