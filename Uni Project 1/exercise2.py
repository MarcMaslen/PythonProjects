
import math # imports the maths module
# defines the input and output of the read and write function
def tuple1(line):
    n = line.split() #this splits each of the data from the txt file and makes them there own word
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
    a=['Name','Latitude','Longitude','Number of citizens']
    catagory = ('{0:18} {1:18} |{2:17} |{3:11} |'.format(a[0],a[3],a[1],a[2],))
    print('-'*len(catagory))
    print(catagory)
    print('-'*len(catagory))


# this is my main function that runs my code
def assign2(list2):
    for n in list2:
        x = ('{0:6} n. citizens: {1:18} | {2:15} | {3:10} |'.format(n[0],n[3],n[1],n[2],))
        print(x)
        print('_'*len(x))
    print('')

    while True:
       print('''This is the table of data from diffrent citys, choose one of the following 4 options
       -----------------------------------------------------------
       |option A - Choose a city by a name(e.g rome)             |
       -----------------------------------------------------------
       |option B - Choose a city by population                   |
       -----------------------------------------------------------
       |option C - Choose a city within a 10km range form coords |
       -----------------------------------------------------------
       |option D - Quit                                          |
       -----------------------------------------------------------
''')
       break
    userinput = input('Enter One of the 4 options: ').capitalize()

    # this is option 1 where it allows for the user to ask for a city name and supply the users with the city name and info
    if userinput == 'A':
        cityname = input('please enter the city name: ').capitalize()
        p=0
        catagory()
        for i in list2:
            if i[0] == cityname:
                print('{0:6} n. citizens: {1:18} | {2:15} | {3:10} |'.format(i[0],i[3],i[1],i[2],))
                print('_'*len(x))
                p+=1
        if p ==0:
            print('there is no city that goes by that name')
        print(' ')
        loop()


    # This is option 2 and asks the user for the lowest and highest populated ares they want to know
    elif userinput =='B':
        while True:
            try:
                range1 = int(input('please enter the lowest population: '))
                range2 = int(input('please enter the higest population: '))
                break
            except:
                print('no')
        p=0
        catagory()
        for i in list2:
            if int(i[3])>= range1  and int(i[3])<= range2:
                print('{0:15} | {1:15} | {2:8} | {3:10} |'.format(i[0],i[3],i[1],i[2]))
                print('_'*len(x))
                p+=1
        print(' ')
        loop()

    # this is option 3 and asks the user to get a city within 10km of there cords
    elif userinput =='C':
        while True:
            try:
                lat = int(input('please enter the your latitude: '))
                long = int(input('please enter the your longitude: '))
                break
            except:
                print('no')
        p=0
        catagory()
        for i in list2:
            b=int(i[1])
            b2=int(i[2])
            latlist= []
            longlist=[]
            for j in range(b-10,b+11):
                latlist.append(j)
            for j in range(b2-10,b2+11):
                longlist.append(j)

            if lat in latlist and long in longlist:
                print('{0:15} | {1:15} | {2:8} | {3:10} |'.format(i[0],i[3],i[1],i[2]))
                print('_'*len(x))
                p=1
            print(' ')
        loop()


   # this is option 4 and allows the user to see the distance between 2 citys
    elif userinput =='D':
        while True:
            try:
                city1 = input('Please enter the city name: ').capitalize()
                city2 = input('Please enter the second city name: ').capitalize()
                break
            except:
                print('thats not a city name')
                loop()

        
        catagory()
        for i in list2:
            if i[0] == city1:
                print('{0:15} | {1:19} | {2:16} | {3:10} |'.format(i[0],i[3],i[1],i[2]))
                print('_'*len(x))
                latitude1 = int(i[1])
                longitude1 = int(i[2])
            if i[0] == city2:
                print('{0:15} | {1:19} | {2:16} | {3:10} |'.format(i[0],i[3],i[1],i[2]))
                print('_'*len(x))
                latitude2 = int(i[1])
                longitude2 = int (i[2])
                distance = math.sqrt(((latitude1-latitude2)**2)+((longitude1-longitude2)**2))
                print(distance,'km apart')
                loop()
    

#this is the beginning of the program and asks the user for the txt file and puts it in a table
try:
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
