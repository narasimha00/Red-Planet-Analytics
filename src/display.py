
# display.py
import matplotlib.pyplot as plt
from utils import clear

def print_sensor_data(param: int, data: dict, sol: str):
    if param in [1, 2, 3] and not sol:
        raise AttributeError("Sol is required for this option.")
    print()
    match param:
        case 1:
            print('Temperature details for sol', sol)
            print(f"Average: {data[sol]['AT']['av']} °F")
            print(f"Min: {data[sol]['AT']['mn']} °F")
            print(f"Max: {data[sol]['AT']['mx']} °F")
            print(f"Samples: {data[sol]['AT']['ct']}")
        case 2:
            print('Pressure details for sol', sol)
            print(f"Average: {data[sol]['PRE']['av']} Pa")
            print(f"Min: {data[sol]['PRE']['mn']} Pa")
            print(f"Max: {data[sol]['PRE']['mx']} Pa")
            print(f"Samples: {data[sol]['PRE']['ct']}")
        case 3:
            print('Wind speed details', sol)
            print(f"Average: {data[sol]['HWS']['av']} m/s")
            print(f"Min: {data[sol]['HWS']['mn']} m/s")
            print(f"Max: {data[sol]['HWS']['mx']} m/s")
            print(f"Samples: {data[sol]['HWS']['ct']}")
        case 4:
            plot_graphs(data)
        case _:
            exit(0)

def plot_graphs(data):
    sols = data['sol_keys']
    temps, pressures, winds, valid_sols = [], [], [], []

    for sol in sols:
        try:
            temps.append(data[sol]['AT']['av'])
            pressures.append(data[sol]['PRE']['av'])
            winds.append(data[sol]['HWS']['av'])
            valid_sols.append(sol)
        except KeyError:
            continue

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(valid_sols, temps, marker='o', color='orange')
    plt.title('Average Atmospheric Temperature')
    plt.ylabel('Temperature (°F)')

    plt.subplot(3, 1, 2)
    plt.plot(valid_sols, pressures, marker='o', color='green')
    plt.title('Average Pressure')
    plt.ylabel('Pressure (Pa)')

    plt.subplot(3, 1, 3)
    plt.plot(valid_sols, winds, marker='o', color='blue')
    plt.title('Average Wind Speed')
    plt.xlabel('Sol')
    plt.ylabel('Speed (m/s)')

    plt.tight_layout()
    plt.show()
