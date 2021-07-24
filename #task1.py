#task1

#write on file

my_file = open("numbers.txt","w")
my_file.write ( "numbers (4)")
my_file.numbers =("3,45,83,21""\n")
my_file.close()


#reading from file
with open("numbers.txt","r") as myfile:
data = myfile.read().replace('\n',',')
myfile.close()

#Appending to a file

my_file =open("numbers.txt","a")
my_file.write("where has it gone?")
my_file.close()
