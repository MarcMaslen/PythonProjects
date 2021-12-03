# defines the input and output of the read and write function
def tuple1(line):
    n = line.split() #this splits each of the data from the txt file and makes them there own word
    n[3]+=','        #this takes the word in the 3rd position and adds a comma stright after the word  
    return tuple(n)

# defines a loop that allows the user to keep going back through my menu
def loop():
    x = input('Press x to return back to the menu: ')
    print(' ')   #this is just used to make a space between two outputs
    if x == 'x': #this just means if the user types x then it is true and will continue
        catagory()
        assign2(list2)
    else:
        print('sorry that command doesnt work')
        loop()

#defines the catagory of all of the columns in the table, also it allows me to lines it up with the data
def catagory():
    a=['Lastname','Firstname','Salary','Position','Team']
    catagory = ('{0:15} |{1:16} |{2:11} |{3:11} |{4:8} |'.format(a[0],a[1],a[2],a[3],a[4]))
    print('-'*len(catagory))
    print(catagory)
    print('-'*len(catagory))

#defines the catagory for the question air in option 4
def catagory2():
    a=['Lastname','Firstname','Salary','Position','Team']
    catagory = ('{0:15} |{1:16} |{2:11} |{3:11} |{4:8} |'.format(a[2],a[0],a[1],a[3],a[4]))
    print('-'*len(catagory))
    print(catagory)
    print('-'*len(catagory))
    

# defining how it will be printed out to the user.
def assign2(list2):
    for n in list2:
        x = ('{0:15} | {1:15} | {2:7} | {3:10} | {4:8}|'.format(n[3],n[2],n[4],n[1],n[0]))
        print(x)
        print('_'*len(x))
    print('')  

    while True:
       print('''This is the table of football player data, choose one of the following 4 options
       -------------------------------------------------
       |option 1 - Choose a players by last name       |
       -------------------------------------------------
       |option 2 - Choose a players by Salary          |
       -------------------------------------------------
       |option 3 - Choose the names of players by team |
       -------------------------------------------------
       |option 4 - Quit                                |
       -------------------------------------------------
''')
       break
    userinput = input('Enter One of the 4 options: ')

    # This is option 1 and allows the user to input the lastname of a player and get that players info
    if  userinput == '1':
        lastname = input('please enter the players lastname: ').capitalize()+','
        p=0
        catagory()
        for i in list2:
            if i[3] == lastname:
                print('{0:15} | {1:15} | {2:8} | {3:10} | {4:8}|'.format(i[3],i[2],i[4],i[1],i[0]))
                print('_'*len(x))
                p+=1
        if p ==0:
            print('there is no player that goes by that name')
        print(' ')
        loop()
              
      


    # This is option 2 and allows the user to get a players info between a user inputted range
    elif userinput =='2':
        while True:
            try:
                range1 = int(input('please enter the lowest salary range: '))
                range2 = int(input('please enter the highest salary range: '))
                break
            except:
                print('no')
        p=0
        catagory()
        for i in list2:
            if int(i[4].replace(',', '')) >= range1  and int(i[4].replace(',', '')) <= range2:
                print('{0:15} | {1:15} | {2:8} | {3:10} | {4:8}|'.format(i[3],i[2],i[4],i[1],i[0]))
                print('_'*len(x))
        print(' ')
        loop()


    # this is option 3 and asks the user for a team name and supplys all the players in that team
    elif userinput =='3':
        while True:
            teamname = input('please enter the players Team: ').capitalize()
            p=0
            catagory()
            for i in list2:
                if i[0] == teamname:
                    print('{0:15} | {1:15} | {2:8} | {3:10} | {4:8}|'.format(i[3],i[2],i[4],i[1],i[0]))
                    print('_'*len(x))
                    p+=1
            if p ==0:
                print('there is no team that goes by that name')
            break
        print(' ')
        loop()
        
    #this is option 4 and lets the user quit and displays the questions 
    elif userinput =='4':
        n = input('Are you sure you want to quit, theres no going back? yes/no: ')
        if n == 'no':
            assign2(list2)
        elif n == 'yes':
            print('''Okay, you have chosen to quit.
Here are a couple questions about the info,
in order to contine you must first get all these correct''')
            while True:
                try: # this trys the first set of questions to the user
                    position1 = input('Please input the position of a football player: ').capitalize()
                    team1 = input('Please input the team of a football player: ').capitalize()
                    p=0
                    catagory()
                    for i in list2: # this checks to make sure the awnsers are correct
                        if i[1] == position1 and i[0] == team1:
                            print('{0:15} | {1:15} | {2:8} | {3:10} | {4:8}|'.format(i[3],i[2],i[4],i[1],i[0]))
                            print('_'*len(x))
                            p+=1

                    salary1 = int(input('please input the lowest salary from the table: '))
                    salary2 = int(input('please input the highest salary from the data: '))
                    p=0
                    catagory2()
                    for i in list2: # this checks to make sure the awnsers correct again
                        if int(i[4].replace(',', '')) >= salary1  and int(i[4].replace(',', '')) <= salary2:
                            list2.sort(key = lambda i: i[4])
                            print('{0:15} | {1:15} | {2:8} | {3:10} | {4:8}|'.format(i[4],i[3],i[2],i[1],i[0]))
                            print('_'*len(x))
                            p+=1

                        else:
                            print('nope start again')
                            loop()
                    

                except:
                    print('no')

                print('Congratz, you passed. Thats the end of the program. Bye Bye.')
                quit() # quits the program
            
    
try: # this is the beginning of the program and asks the user for the txt file and puts it in a table
    userFile = input("Enter File name(Include file extension txt ect): ") # starts off by getting the user to imput a file
    Inputfile = open(userFile, 'r')
    print('thank you')
    mylines = Inputfile.readlines()
    Inputfile.close()
    list2=[]
    catagory()
    for Inputfile in mylines:
        n = tuple1(Inputfile)
        list2.append(n)
    assign2(list2)




except:
    FileNotFoundError # error handling
    print('File not found')
    
