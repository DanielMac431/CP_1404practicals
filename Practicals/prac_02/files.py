OUTPUT_FILE = open('Name', 'w')
name = str(input("Your Name:"))
print(name, file=OUTPUT_FILE)
OUTPUT_FILE.close()