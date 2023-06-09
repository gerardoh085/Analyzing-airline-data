'''
Author: Gerardo Hernandez Macoto
Project: Analyzing airline data
'''

import matplotlib.pyplot as plt
import airlines
import numpy as np

data = airlines.get_airports()

structure = ''' 
    Airport: dict
        Code: str
        Name: str
    Time: dict
        Label: str
        Month: int
        Month Name: str
        Year: int
    Statistics: dict
        # of Delays: dict 
            Carrier: int
            Late Aircraft: int
            National Aviation System: int
            Security: int
            Weather: int
        Carriers: dict
            Names: str
            Total: int 
        Flights: dict
            Cancelled: int
            Delayed: int
            Diverted: int
            On Time: int
            Total: int
        Minutes Delayed: dict
            Carrier: int
            Late Aircraft: int
            National Aviation System: int
            Security: int
            Total: int
            Weather: int
'''


'''
Question 1:
Which airport has the highest average number of flight delays?
'''


newdict = {}
newlist = []
newset = set()


for i in range(len(data)):
    item = data[i]["Airport"]["Code"]
    if item not in newset:
        newset.add(item)
        newdict = {"Code": item, "Delay": 0,
                   "Counter": 0, "Avg": 0}
        newlist.append(newdict)


for i in range(len(data)):
    for j in range(len(newlist)):
        if data[i]["Airport"]["Code"] == newlist[j]["Code"]:
            delay = data[i]["Statistics"]["Flights"]["Delayed"]
            newlist[j]["Delay"] += delay
            newlist[j]["Counter"] += 1
            newlist[j]["Avg"] = newlist[j]["Delay"] / newlist[j]["Counter"]


# get the list of avg delays
res_avg_delay_list = [newlist[i]["Avg"] for i in range(len(newlist))]
# get the max in the list
res_avg = max(res_avg_delay_list)
# get the airport code
airport_code = newlist[res_avg_delay_list.index(res_avg)]["Code"]

print("The result:")
print(f"{airport_code}, {res_avg}")
