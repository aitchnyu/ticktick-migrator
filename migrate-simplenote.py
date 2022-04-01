import csv
import sys
import json
from zipfile import ZipFile


def main():  # pragma: no cover
    input_file = sys.argv[1]
    with ZipFile(input_file) as myzip:
        with myzip.open("source/notes.json") as myfile:
            raw_notes = json.load(myfile)["activeNotes"]
    raw_notes = sorted(raw_notes, key=lambda x: x["lastModified"], reverse=True)
    out = []
    id = 1
    for raw_note in raw_notes:
        title, content = raw_note["content"].split("\n", 1)
        title = title.replace("\r", "")
        content = content.replace("\r", "")
        id += 1
        out.append(
            {
                "Folder Name": "",
                "List Name": "Imported Notes",
                "Title": title,
                "Tags": "",
                "Content": content,
                "Is Check list": "N",
                "Start Date": "",
                "Due Date": "",
                "Reminder": "",
                "Repeat": "",
                "Priority": "0",
                "Status": "0",
                "Created Time": raw_note["lastModified"],
                "Completed Time": "",
                "Order": "0",
                "Timezone": "Asia/Calcutta",
                "Is All Day": "",
                "Is Floating": "false",
                "Column Name": "",
                "Column Order": "",
                "View Mode": "list",
                "taskId": str(id),
                "parentId": "",
            }
        )
    with open("ticktick-from-simplenote.csv", mode="w") as csv_file:
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
    print(f'Wrote {len(out)} notes to ticktick-from-simplenote.csv')


if __name__ == "__main__":  # pragma: no cover
    main()
