def tupleMaker(x):#same as ex1
    index =x.strip("\n").split(" ")
    tupleMaker=(index[0],index[1],index[2],index[3])#assigns tuple position to var
    return tupleMaker#returns assignments

def fileOpener(tuple):
        print("{place:30}{population:12}{distance:15}".format(place=tuple[0],population=tuple[1],distance=tuple[2))#used for formatting throughout program
print("Type the file name you're searching for")
w = input()#used in open file line
data = []#used with func1 and fucn2 file opener

try:
    with open(w,"r")as file:#will try to open and read file input from w above
        for i in file.readlines():#index through elements of file using readlines            
            data.append(tupleMaker(i))#appends elements to mylist above then runsu them through func 1 to tuple them
            
    for i in data:
            fileOpener(i)
def main():
    choice = input("""
 A: View cities in population range 
 B: View cities in 10km radius of coords
 C: Distance between 2 cities
 Q: Quit
  enter your choice: """)
    
    if choice == "A" or choice =="a":
        None
    elif choice == "B" or choice =="b":
        None
    elif choice=="C" or choice=="c":
        None
    elif choice=="Q" or choice=="q":
        exit()
    else:
        print("Select A,B or C.")
        print("try again")
