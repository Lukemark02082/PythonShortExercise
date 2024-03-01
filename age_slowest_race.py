import csv
import datetime

def get_data():
    """Return content from the 10k_racetimes.csv file"""
    with open('10k_racetimes.csv', 'rt') as file:
        reader = csv.DictReader(file)
        content = list(reader)
    return content

def get_event_time(row):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""    
    birth_date = datetime.datetime.strptime(row['Date of birth'], "%d %b %Y")
    event_date = datetime.datetime.strptime(row['Race date'], "%d %b %Y")

    # Calculate age at event date
    age_days = (event_date - birth_date).days
    age_years = age_days / 365.25

    age_str = f"Age: {int(age_years)} years old and {int((age_years - int(age_years)) * 365.25)} days"
    race_time_str = f"Race Time: {row['TIME']}"

    return (age_str, race_time_str)

def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()

    # Extract Jennifer Rhines' race times along with her age at each race
    rhines_race_data = [get_event_time(row) for row in races if 'Jennifer Rhines' in row['Athlete']]

    # Find the slowest race time and Jennifer Rhines' age at that race
    slowest_time = min(rhines_race_data, key=lambda x: x[1])

    return slowest_time

# Testing the functions
if __name__ == "__main__":
    all_race_data = get_data()
    for race_data in all_race_data:
        if 'Jennifer Rhines' in race_data['Athlete']:
            age_str, race_time_str = get_event_time(race_data)
            print("Jennifer Rhines' age at each race and her race time:", (age_str, race_time_str))
    print("Jennifer Rhines' age at her slowest race time:", get_age_slowest_times())
