import datetime
import os



def calculateDailyTarget():
    os.system("clear")
    #getting the monthly target from user
    monthlyTarget = int(input("Enter Monthly Target"))

    #for now our code can consit work on a 30 days calender
    #over 4 weeks
    weeklytarget = monthlyTarget/4
    dailytarget = monthlyTarget/30


    #we are starting with a new target after a day
    NewMonthlyTarget = monthlyTarget -salesDoneOnTheDay







    print("Your Monthly Target is", monthlyTarget)
    #get the days they planning to finish project in
    numberOfWorlkingDays = int(input("Enter number of working days"))
    print("This month we have",numberOfWorlkingDays,"working days")

    #calculates the daily target needed
    
    dailyTarget = monthlyTarget/numberOfWorlkingDays
    print("Your Daily Terget is", dailyTarget)
        #gets the number of sales made



    salesDoneOnTheDay = int(input("How much sales did you do today"))
    dailySales =  dailyTarget-salesDoneOnTheDay 
    print("You are running shot of",dailySales,"sales")


    
    numberOfDaysLeft = numberOfWorlkingDays - 1


    #calculate the new monthly target after after a single day
    newMonthlyTarget = monthlyTarget - salesDoneOnTheDay
    print("we have a new monthly target of",newMonthlyTarget,"after the first day")

    #calculates the daily target based on sales still to do
    newDailyTarget = newMonthlyTarget/numberOfDaysLeft
    print("you now have",numberOfDaysLeft,"days to reach", newDailyTarget)

# def calculate


def main():
    

    while True:
        print("WELCOME TO SAFE PROJECTOR")
        print("1. Calculate Daily Target")
        print("2. Sales Forecast")
        print("3. Project Your progress success")
        option = input()
        if option == "1":
            calculateDailyTarget()

main()
