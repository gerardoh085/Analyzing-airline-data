import airlines
import pandas as pd
import matplotlib.pyplot as plt

data = airlines.get_airports()

'''
Question 2:
Which flight code has, on average, been cancelled the most?
'''

cancelled_dict = {}
cancelled_list = []
cancelled_set = set()

for i in range(len(data)):
    item = data[i]["Airport"]["Code"]
    if item not in cancelled_set:
        cancelled_set.add(item)
        cancelled_dict = {"Code": item, "Cancelled": 0,
                          "Avg": 0, "Counter": 0}
        cancelled_list.append(cancelled_dict)


for i in range(len(data)):
    for j in range(len(cancelled_list)):
        if data[i]["Airport"]["Code"] == cancelled_list[j]["Code"]:
            cancelled_list[j]["Cancelled"] += data[i]["Statistics"]["Flights"]["Cancelled"]
            cancelled_list[j]["Counter"] += 1
            cancelled_list[j]["Avg"] = (
                cancelled_list[j]["Cancelled"] / cancelled_list[j]["Counter"])


maxVal_list = [(cancelled_list[i]["Avg"]) for i in range(len(cancelled_list))]
maxVal = max(maxVal_list)
airlineCode = cancelled_list[maxVal_list.index(maxVal)]["Code"]

print(f"{airlineCode}, {maxVal}")

code_list = [(li["Code"]) for li in cancelled_list]

x_axis = code_list
y_axis = maxVal_list


plt.plot(x_axis, y_axis)

plt.title("Average Cancellations Per Airport Code")
plt.ylabel("Average Cancellations")
# plt.xlabel("Airport Code")
plt.xticks(rotation=90)
plt.show()
