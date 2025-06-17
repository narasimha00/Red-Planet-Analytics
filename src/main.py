
# main.py
from data_fetcher import fetch_data
from display import print_sensor_data
from utils import clear
import requests

def main():
    try:
        request_data = fetch_data()
    except requests.exceptions.ConnectionError as e:
        print("Connection Error, Please check your internet connection and try again!")
        return


    while True:
        clear()
        sols = request_data['sol_keys']
        print('> Available sols: ', ' '.join(sols))

        sol = input('Enter the sol (or press `Enter` to view graph data or enter \'E\' to exit: ').strip()

        if sol == '':
            print_sensor_data(4, request_data, None)
        elif sol == 'E' or sol == 'e':
            exit(0)
        elif sol not in sols:
            print('Invalid sol! Try again.')
            input('Press Enter to continue...')
            continue
        else:
            param = -1
            while param < 0:
                try:
                    param = int(input('''
======= ==== MENU ==== ======
   1. Atmospheric Temperature
   2. Pressure
   3. Horizontal wind speed
   4. Exit
Enter your choice: '''))
                    if param not in range(1, 5):
                        raise ValueError
                    if param == 4:
                        exit(0)
                except ValueError:
                    print('Invalid input! Try again...')
                    param = -1

            print_sensor_data(param, request_data, sol)

        input('\n\nPress Enter to continue...')

if __name__ == '__main__':
    main()
