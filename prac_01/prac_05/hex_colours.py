COLOUR_NAMES = {'blue1': "#0000ff", 'BlanchedAlmond': '#ffebcd', 'BlueViolet': '#8a2be2',
                'chartreuse3': '66cd00', 'coral': '#ff7f50', 'cyan3': '#00CDCD', 'DarkGreen': '#006400',
                'DarkOrange': '#ff8c00'}
for colour, code in COLOUR_NAMES.items():
    print('{} is {}'.format(colour, code))
colour_input = input('Enter colour name: ')
while colour_input != '':
    if colour_input in COLOUR_NAMES:
        print(COLOUR_NAMES[colour_input])
    else:
        print('Invalid input')
    colour_input = input('Enter colour name: ')
    