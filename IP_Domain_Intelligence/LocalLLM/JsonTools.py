import json
from collections import Counter

def LJasonTOArray(filePath:str):
    # Load JSON file
    with open(filePath, 'r',encoding='utf-8') as f:
        data = json.load(f)
    Alerts = data['Alert']
    return Alerts

def CountUnique(Json,columnName:str) :
    columnData = [jsondata[columnName] for jsondata in Json]
    column_counts = Counter(columnData)
    print("{columnName} counts:")
    for column, count in column_counts.items():
        print(f"{columnName}: {column}-> {count} item(s)")
        
def filter_by_field(data_list, field, value):
    return [item for item in data_list if item.get(field) == value]

def OpenOne(filePath:str):
    alerts = LJasonTOArray(filePath)
    top_one = alerts[0]
    return top_one

def OpenIndex(filePath:str,index:int=0):
    alerts = LJasonTOArray(filePath)
    one_alerts = alerts[index]
    return one_alerts


# Access the array of alrets
# alerts = LJasonTOArray('JsonF.json')

# # top_ten = alerts[:10]
# # for A in top_ten:
# #     print(f"- {A['type']} : ({A['description']})")
# # CountUnique(alerts,'type')

# AttacksAndCompromises = filter_by_field(alerts,"type","AttacksAndCompromises")

# top_ten = AttacksAndCompromises[:10]
# for A in top_ten:
#     print(f"- {A['type']} : ({A['description']})")
# CountUnique(AttacksAndCompromises,'type')

# # list = []
# # for All in alerts :
# #     list.append(All['type'])
# # print("Unique type:", set(list)