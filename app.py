import csv
import datetime
import random
import json

freetimes = []

tasks = []
with open('./tasks.json') as f:
    tasks = json.load(f)

for task in tasks:
    print("")

today = datetime.date.today()
a_week_later = today + datetime.timedelta(days=7)
while today <= a_week_later:
    if today.weekday == 5 or today.weekday == 6:  # 休日は4ポモドーロ多い

        freetimes.append({
            "date": today,
            "time": "10:00",
            "endtime": "10:25",
            "task": []
        })
        freetimes.append({
            "date": today,
            "time": "10:30",
            "endtime": "10:55",
            "task": []
        })
        freetimes.append({
            "date": today,
            "time": "11:00",
            "endtime": "11:25",
            "task": []
        })
        freetimes.append({
            "date": today,
            "time": "11:30",
            "endtime": "11:55",
            "task": []
        })

    freetimes.append({
        "date": today,
        "time": "21:00",
        "endtime": "21:25",
        "task": []
    })
    freetimes.append({
        "date": today,
        "time": "21:30",
        "endtime": "21:55",
        "task": []
    })
    freetimes.append({
        "date": today,
        "time": "22:00",
        "endtime": "22:25",
        "task": []
    })
    freetimes.append({
        "date": today,
        "time": "22:30",
        "endtime": "22:55",
        "task": []
    })

    today = today + datetime.timedelta(days=1)

random_tasks = random.sample(tasks, len(tasks))

i = 0
for freetime in freetimes:
    if len(random_tasks) <= i:
        random_tasks = random.sample(tasks, len(tasks))
        i = 0

    print("freetime", freetime)
    print("random_tasks_i", random_tasks[i])
    freetime["task"].append(random_tasks[i])

    i += 1

rows = []
for freetime in freetimes:
    print(freetime)

    rows.append({
        "Subject": freetime["task"][0]["title"],
        "Start Date": freetime["date"],
        "Start Time": freetime["time"],
        "End Date": freetime["date"],
        "End Time": freetime["endtime"],
    })

with open('./test.csv', 'w') as f:
    writer = csv.DictWriter(
        f, ['Subject', 'Start Date', 'Start Time', "End Date", 'End Time'])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
