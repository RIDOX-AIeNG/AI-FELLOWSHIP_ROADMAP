#Days of the week and their activities pairing
#Store the days of the week in a tuple
#Ask the user to input their activities for each days
#append into an empty list
#pritn the weekly activities with their corresponding days
days_of_week = ("Monday", "Tuesday","Wednesday","Thursday" "Friday")
print("Input activity fior each days")

activities = []
for day in days_of_week:
    activity = input(f"What is your activity on {day}? ")
    activities.append(activity)
schedule = {day: activity for day, activity in zip(days_of_week, activities)}
print("\n\t--- Your Weekly Activities Are ---")
for day, activity in schedule.items():
    print(f"\t{day}: {activity}")