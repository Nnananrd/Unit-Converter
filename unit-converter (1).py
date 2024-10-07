import sys

def select_source_unit():
    print("Select source unit:")
    print("1. Meters")
    print("2. Feet")
    return input("Enter your choice (1 or 2): ")

def enter_value():
    return float(input("Enter the value to convert: "))

def perform_conversion(source_unit, value):
    if source_unit == '1':
        return value * 3.28084  # meters to feet
    elif source_unit == '2':
        return value / 3.28084  # feet to meters
    else:
        raise ValueError("Invalid source unit")

def select_target_unit(source_unit):
    if source_unit == '1':
        return 'feet'
    elif source_unit == '2':
        return 'meters'
    else:
        raise ValueError("Invalid source unit")

def check_for_errors(source_unit, value):
    if source_unit not in ['1', '2']:
        return "Invalid source unit selected"
    if not isinstance(value, (int, float)):
        return "Invalid value entered"
    return None

def display_error_message(error):
    print(f"Error: {error}")

def display_converted_value(value, unit):
    print(f"Converted value: {value:.2f} {unit}")

def main():
    while True:
        source_unit = select_source_unit()
        value = enter_value()
        
        error = check_for_errors(source_unit, value)
        if error:
            display_error_message(error)
            continue
        
        try:
            converted_value = perform_conversion(source_unit, value)
            target_unit = select_target_unit(source_unit)
            display_converted_value(converted_value, target_unit)
        except ValueError as e:
            display_error_message(str(e))
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
