import datetime
import os


def calculateDailyTarget():
    os.system("clear")
    #getting the monthly target from user
    monthlyTarget = 20

    #for now our code can consit work on a 30 days calender
    #over 4 weeks
    weeklytarget = monthlyTarget/4
    dailytarget = monthlyTarget/30

    print("Your weekly target is: ",weeklytarget)
    print("Your daily target is ",dailytarget)

    #we are starting with a new target after a day
    salesOnTheDay = 1
    NewMonthlyTarget = monthlyTarget -salesOnTheDay
    print("your new Traget is: ", NewMonthlyTarget)
    
    #calculating days left starting from 30 days and 5 days in a week
    DaysInWeek = 7
    salesprogress =1
    dayscomplete = 1


    projectedMonthlyTarget = monthlyTarget - (salesprogress*dayscomplete)

    print("your new Projection ",projectedMonthlyTarget)

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
