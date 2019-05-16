from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    menu_selection = ''
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    while menu_selection != 'q':
        print('q)uit, c)hoose, d)rive')
        menu_selection = input('>>> ').lower()
        if menu_selection == 'c':
            print('Taxis available:')
            display_taxis(taxis)
            user_taxi = int(input('Choose Taxi: '))
            current_taxi = taxis[user_taxi]
            print('Bill to date: ${:.2f}'.format(bill_to_date))
        elif menu_selection == 'd':
            current_taxi.start_fare()
            distance = float(input('Drive how far? '))
            current_taxi.drive(distance)
            print('Your {} trip cost you ${:.2f}'.format(current_taxi.name, current_taxi.get_fare()))
            bill_to_date += current_taxi.get_fare()
            print('Bill to date: ${:.2f}'.format(bill_to_date))
        else:
            print('Invalid Option')
            print('Bill to date: ${:.2f}'.format(bill_to_date))
    print('Total trip cost: {}'.format(bill_to_date))
    print('Taxis are now:')
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print('{} - {}'.format(i, str(taxi)))


main()
