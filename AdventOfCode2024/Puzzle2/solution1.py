
with open("AdventOfCode2024\Puzzle2\Input2.txt", "r") as file:
  input_data = file.readlines()

a = []
b=0

NumberOfPasses = 0
for line in input_data:
  # loop goes until end of the line. Than goes to the next line.
  for x in line.split():
    newInt = int(x)
    #here the integer is added to the list a
    a.append(newInt)  
    #now I need to find a way how to check if numbers are increasing or not.
    #lets take first number and compare with the second one in a list
    #IF is it bigger yes is the second bigger than third and so on
    #IF is it smaller than second one check the difference
    # if a[0] > a[1] && a[0] - a[1] <= 3

  LenghtOfAnArray = len(a)-1
  while b != LenghtOfAnArray:
    b+=1
    y=0
    z=1
    
  
    while a[y]>a[z] and a[y] - a[z] <= 3 and z!= LenghtOfAnArray:
      y+=1
      z+=1
      
      if z==LenghtOfAnArray and a[y]>a[z]:
        NumberOfPasses += 1
        continue

  
  
# problem tutaj polega na tym ze ja patrze na element za elementem nie biorac pod uwage jaki warunek byl 
#spelniony poprzednio. Nie wiem jak napisac warunek zeby sprawdzic czy poprzedni element byl malejacy czy rosnacy?

# while warunek rosnacy jest spelniony kontynuuj do konca listy i NumberOfPasses +1
# jesli warunek w trakcie jest przerwany wyczysc liste a i pobierz kolejny raport
    print(a[y],a[z])
    while a[y]<a[z] and a[z] - a[y] <= 3 and z!= LenghtOfAnArray:
      y+=1
      z+=1
      print(a[y],a[z])
      if z==LenghtOfAnArray and a[y]<a[z] :
        NumberOfPasses += 1
        continue
    break

  a.clear()
  b=0
  

print(NumberOfPasses)
 

