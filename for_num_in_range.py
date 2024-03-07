gems = int(input('How many days did you collect gems? '))

for num in range(gems):
    days = int(input('Enter the number of gems collected on day 1: '))
    days += 1
    Total = days * gems
    Average = Total / gems
print("Total gems collected: ", Total)
print("Average gems collected per day: ", Average)