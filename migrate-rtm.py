import datetime
import csv
import sys
import typing
import json
from zipfile import ZipFile


def main():  # pragma: no cover
    input_file = sys.argv[1]
    with open(input_file, mode="r") as json_file:
        raw_tasks = json.load(json_file)["tasks"]

    def to_time_string(timestamp):
        if not timestamp:
            return ""
        timestamp = timestamp / 1000
        return datetime.datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%dT%H:%M:%S+0000"
        )

    out = []
    id = 1
    for raw_task in raw_tasks:
        if "repeat" in raw_task and "date_completed" not in raw_task:
            a, b, *wkst = raw_task["repeat"].split(";")
            repeat = a + ";" + b
        else:
            repeat = ""
        out.append(
            {
                "Folder Name": "",
                "List Name": "Imported Tasks",
                "Title": raw_task["name"],
                "Tags": "",
                "Content": "",
                "Is Check list": "N",
                "Start Date": to_time_string(raw_task.get("date_due")),
                "Due Date": to_time_string(raw_task.get("date_due")),
                "Reminder": "",
                "Repeat": repeat,
                "Priority": "0",
                "Status": "1"
                if "date_completed" in raw_task
                else 0,  # 0 is incomplete, 1 is complete, 2 is archived
                "Created Time": to_time_string(raw_task.get("date_created")),
                "Completed Time": to_time_string(raw_task.get("date_completed")),
                "Order": "0",
                "Timezone": "Asia/Kolkata",
                "Is All Day": "true",
                "Is Floating": "false",
                "Column Name": "",
                "Column Order": "",
                "View Mode": "list",
                "taskId": str(id),
                "parentId": "",
            }
        )
    with open("ticktick-from-rtm.csv", mode="w") as csv_file:
        csv_file.writelines(
            [
                "Date: 2022-03-14+0000\n",
                "Version: 7.0\n",
                "Status:\n0 Normal\n1 Completed\n2 Archived\n",
            ]
        )
        fieldnames = [
            "Folder Name",
            "List Name",
            "Title",
            "Tags",
            "Content",
            "Is Check list",
            "Start Date",
            "Due Date",
            "Reminder",
            "Repeat",
            "Priority",
            "Status",
            "Created Time",
            "Completed Time",
            "Order",
            "Timezone",
            "Is All Day",
            "Is Floating",
            "Column Name",
            "Column Order",
            "View Mode",
            "taskId",
            "parentId",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in out:
            writer.writerow(row)
    print(f'Wrote {len(out)} tasks to ticktick-from-rtm.csv')


if __name__ == "__main__":
    main()
