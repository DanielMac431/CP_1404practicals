import wikipedia

menu_input = str(input('Enter "s" for search, enter "p" for page title \n>>>'))
while menu_input != '':
    if menu_input == 's':
        search_input = str(input('Search Request: '))
        results = wikipedia.search(search_input, 3)
        i = 0
        for result in results:
            print('{}.. {}'.format(i, result))
            i += 1
        choice = int(input('Choose Page: '))
        choice = wikipedia.page(results[choice])
        print(choice.title)
        print(choice.summary)
        print(choice.url)
    if menu_input == 'p':
        choice = wikipedia.page(str(input('Page Title: ')))
        print(choice.title)
        print(choice.summary)
        print(choice.url)
    menu_input = str(input('Enter "s" for search, enter "p" for page title \n>>>'))
