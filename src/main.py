
# main.py
from data_fetcher import fetch_data
from display import print_sensor_data
from utils import clear, print_logo
import requests

def main():
    clear()
    try:
        request_data = fetch_data()
    except requests.exceptions.ConnectionError as e:
        print("Connection Error, Please check your internet connection and try again!")
        return

    sol = None
    while True:
        clear()
        print_logo()
        param = -1
        while param < 0:
            try:
                param = int(input('''
======= ==== MENU ==== ======
   1. Atmospheric Temperature
   2. Pressure
   3. Horizontal wind speed
   4. Graphical Representation
   5. Exit
Enter your choice: '''))
                if param not in range(1, 6):
                    raise ValueError
                if param == 5:
                    exit(0)
            except ValueError:
                print('Invalid input! Try again...')
                param = -1
                continue

            if (param <= 3):
               print()
               sols = request_data['sol_keys']
               print('Available sols: ', sols)
               sol = input('Enter the sol: ').strip()
               if sol not in sols:
                   print('Invalid input!')
                   continue
            print_sensor_data(param, request_data, sol)
        input('\n\nPress Enter to continue...')

if __name__ == '__main__':
    main()
