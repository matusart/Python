
with open("AdventOfCode2024\Puzzle2\Input2.txt", "r") as file:
  input_data = file.readlines()

a = []
for line in input_data:
  # loop goes until end of the line. Than goes to the next line.
  for x in line.split():
    newInt = int(x)
    #here the integer is added to the list a
    a.append(newInt)  
  print(a)
  a.clear()


  # I have to go through the 
  # a.append(int(line.split()[0].strip()))

  #zmien dane na integers
  #wyczysc spacje
  #Sprawdz czy dane sa wzrastajace czy malejace

