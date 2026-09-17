meal_cost = float(input("Enter the meal cost: ").strip())
tip_percentage = float(input("Enter the tip percentage: ").strip())
num_people = int(input("Enter the number of people: ").strip())

answer_alt = (meal_cost * (1 + (tip_percentage/100))/num_people)
main_answer = round(answer_alt, 2)

print(f"Each person pays: {main_answer:.2f} RMB")