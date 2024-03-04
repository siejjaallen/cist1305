# Siejja Allen
# 2/28/24
# Lab 5-4 The Bottle Return Program

#the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        totalBottles = getBottles ()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles, totalPayout)
        endProgram= input('Do you want to end the program? (Enter yes or no): ')

#this function will get the number of bottles returned
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1

    while counter <=7:
        todayBottles = int(input('Enter number of bottles for today:'))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1
    return totalBottles
    
#this function will calculate the total payout
def calcPayout (totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout

#this function will display the information
def printInfo(totalBottles, totalPayout):
    print ('The total number of bottles collected is', totalBottles)
    print ('The total paid out is $', totalPayout)

 #calling main
main ()