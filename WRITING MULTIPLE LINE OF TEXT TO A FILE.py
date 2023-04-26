#creating a file to write the text input by the user
my_file = open("mylife.txt","w")

#ask the user to enter the line of text
while True:
        line = input('Enter line: ')
        if line:
            my_file.write(line + '\n')
        else:
              break