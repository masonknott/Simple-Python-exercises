def tupleMaker(x):
    index =x.strip("\n").split(" ")
    tupleMaker=(index[0],index[1],index[2],index[3],index[4])#assigns tuple position to var
    return tupleMaker#returns assignments

#file opening and position assigning function
def fileOpener(tuple):
        print("{fn:30}{money:12}{role:15}{club}".format(club=tuple[0],role=tuple[1],fn=tuple[3]+", "+tuple[2],money=tuple[4]))#used for formatting throughout program
print("Type the file name you're searching for")
w = input()#used in open file line
data = []#used with func1 and fucn2 file opener

try:
    with open(w,"r")as file:#will try to open and read file input from w above
        for i in file.readlines():#index through elements of file using readlines            
            data.append(tupleMaker(i))#appends elements to mylist above then runsu them through func 1 to tuple them
            
    for i in data:
            fileOpener(i)
except:#if file is wrong
    print("Wrong file name. Terminating...")#terminate then exit
    exit()
#file opening and position assigning function


#player name serach function
def nameSearch():#look for player name capital or non caps
    cond = False
    a = "Search for a last name this can be upper case or lower case \n"
    print(a)
    b=input().lower()#lowers user input to match lowered name below

    for element in data:#interlinking the function with func2(func2 includes func 1 also)
        if element[3].lower() == b:#index position 3 is set as name in the fileOpener(func2) function, lowers name
            fileOpener(element)#
            cond = True
            
    if cond ==  False:#
        print("Last name not found.... enter a new name to try")#if name not found prompts another attempt
#player name serach function


#team name finding function
def teamName():#look for football team name in tuple position
    cond = False #
    print("Enter the name of the team you are searching for. ")
    x=input()#input for searching for team name
    
    for ele in data:
        if x.lower()==ele[0].lower():#lowers input to match it with team name at position 0
            cond = True
            print("{0}, {1}".format(ele[3],ele[2]))#formatting via index positions
            
    if cond == False:
        print("Team name not found \n")
##team name finding function

#moneysorting function
def money(x):#positions money on table via index
    b = x[4]#index pos 4(5)
    return int(b.replace(",",""))#replaces index pos 4 withmoney
#moneysorting function

#simple menu program that in corporates the other functions via choice selection
def main():
    choice = input("""
 A: Full details of player with last name
 B: All player with salary in particular range
 C: All player of certain team
 Q: Quit
  enter your choice: """)
    
    if choice == "A" or choice =="a":
        nameSearch()##calls func upon input being A or a
    elif choice == "B" or choice =="b":#calls func upon input being B or b
        None#not working
    elif choice=="C" or choice=="c":
        teamName()#calls func upon input being C or c
    elif choice=="Q" or choice=="q":#calls func upon input being Q or q
        exit()
    else:
        print("Select A,B or C.")
        print("try again")

while True:#creates repeating menu until
        main()

