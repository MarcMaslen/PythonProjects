try:
    userFile = input("Enter File name(Include file extension txt ect): ") # starts off by getting the user to imput a file
    Inputfile = open(userFile, 'r')
    print('Thank you')
    with Inputfile as f:
        for line in f: # reads the file
            for ex1_sample_data_Input in line.split(): # this takes the txt file and splits it
                  xlist = []# create a list
                  for i in line.split():
                      xlist.append(i)

       
                
              
            print('____________________________________________________')
            print(xlist[3], '|', xlist[2], '|', xlist[4], '|', xlist[1], '|', xlist[0])
          
except:
    FileNotFoundError
    print('File could not be found')
