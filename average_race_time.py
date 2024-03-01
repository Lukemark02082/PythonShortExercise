import csv

def get_data():
    """Return content from the 10k_racetimes.csv file"""
    with open('10k_racetimes.csv', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    with open('10k_racetimes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rhines_race_times = [row['TIME'] for row in reader if 'Jennifer Rhines' in row['Athlete']]
    return rhines_race_times

def get_average():
    """Return Jennifer Rhines' average race time"""
    racetimes = get_rhines_times()

    # Convert race times to milliseconds for easier calculations
    total_ms = 0
    for time in racetimes:
        components = time.split(':')
        minutes = int(components[0])
        seconds = int(components[1].split('.')[0])
        milliseconds = int(components[1].split('.')[1]) if '.' in components[1] else 0
        total_ms += (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

    # Calculate the average in milliseconds
    average_ms = total_ms / len(racetimes)

    # Convert the average back to mm:ss:M format
    minutes = int(average_ms / (60 * 1000))
    seconds = int((average_ms % (60 * 1000)) / 1000)
    milliseconds = int((average_ms % (60 * 1000)) % 1000)
    average_time = f"{minutes:02d}:{seconds:02d}:{milliseconds // 100}"

    return average_time

# Testing the functions
if __name__ == "__main__":
    print("Jennifer Rhines' race times:", get_rhines_times())
    print("Jennifer Rhines' average race time:", get_average())
