# Partial order planning

print("Start")
order_one = ["Left sock","Right sock"]
order_two = ["Left shoe","Right shoe"]
plan = []

print("What will you wear first")
option = int(input("1. Left sock or 2. Right sock: "))
if option == 1 or option == 2:
  plan.append(order_one[option-1])
  plan.append(order_two[option-1])
else:
  pass

for i in [*order_one, *order_two]:
  if i not in plan:
    plan.append(i)

print(f"Partial order plan for the same is: {plan}")
