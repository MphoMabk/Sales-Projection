import datetime
import os
import requests

# def Variables():
#     monthlyTarget = 20

#     return monthlyTarget  

def calculateDailyTarget():
    
    os.system("clear")
    monthlyTarget = 20

    api_key = 'MY API_KEY'
    
    response = requests.get(f'https://calendarific.com/api/v2/holidays?api_key={api_key}&country=US&year=2023&month=8')
    data = response.json()

    working_days = data['response']['holidays'][0]['date']['datetime']['day']


    #for now our code can consit work on a 30 days calendar
    dailytarget = monthlyTarget/working_days
    print("Your daily target is ",dailytarget)
    


# def calculateWeeklytarget(monthlyTarget): 

#     #calculates the over 4 weeks
#     weeklytarget = monthlyTarget/4
#     print("Your weekly target is: ",weeklytarget)


#     #we are starting with a new target after a day
#     salesOnTheDay = 1
#     NewMonthlyTarget = monthlyTarget -salesOnTheDay
#     print("your new Traget is: ", NewMonthlyTarget)
    
#     #calculating days left starting from 30 days and 5 days in a week
#     DaysInWeek = 7
#     salesprogress =1
#     dayscomplete = 1


#     projectedMonthlyTarget = monthlyTarget - (salesprogress*dayscomplete)

#     print("your new Projection ",projectedMonthlyTarget)




def main():
    

    while True:
        print("WELCOME TO SAFE PROJECTOR")
        print("1. See Daily Target")
        print("2. See Weekly Target")
        print("2. Sales Forecast")
        print("3. Project Your progress success")
        option = input()
        if option == "1":
            calculateDailyTarget()
        # if option == "2":   
        #     calculateWeeklytarget(monthlyTarget)

main()
