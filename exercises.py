# Number 1
trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

direction_train_111 = trains[-1]['direction']

# Number 2
frequency_train_80B = trains[-3]['frequency_in_minutes']


# Number 3
direction_train_610 = trains[2]['direction']

# Numbers 4, 5 and 6
def list_of_trains_by_direction(direction, list_of_trains):
    
    trains_in_the_direction = []

    for item in list_of_trains:
        if item["direction"] == direction:
            trains_in_the_direction.append(item['train'])
    return trains_in_the_direction

list_of_trains_by_direction("north", trains)
list_of_trains_by_direction("east", trains)

# Number 7
trains[0]["first_departure_time"] = 6

# Number 8
trains_by_frequency = {}
for train in trains:

    if (train["frequency_in_minutes"] in trains_by_frequency.keys()):
        trains_by_frequency[train["frequency_in_minutes"]].append(train["train"])
    else:
        trains_by_frequency[train["frequency_in_minutes"]] = [train["train"]]

print(trains_by_frequency)
