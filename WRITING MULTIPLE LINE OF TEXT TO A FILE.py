#creating a file to write the text input by the user
my_file = open("mylife.txt","w")

#ask the user to enter the line of text
while True:
        line = input('Enter line: ')
        if line:
            my_file.write(line + '\n')

#ask the user if still wanted to add another line or not
        while True:
                choice = input('Are there more lines (y/n): ')
                if choice == 'y':
                    line = input('Enter line: ')
                    if line:
                        my_file.write(line + '\n')
                elif choice == 'n':
                    exit()

        else:
            break

#close the file
my_file.close()