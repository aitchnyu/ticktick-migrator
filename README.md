# Simplenote and Remember The Milk to TickTick migrator

This is a quick and dirty script to migrate Simplenote notes as notes in TickTick and Remember The Milk tasks as TickTick tasks. This needs only the python stdlib. 

## Migrating Simplenote notes

Test with example file at

```shell
$ python3 migrate-simplenote.py example-export-simplenote.zip
Wrote 2 notes to ticktick-from-simplenote.csv
```

Export your notes from
![Exporting Simplenote](docs/export-simplenote.png?raw=true "Exporting Simplenote")

Run above command with exported zip file and you will get ticktick-from-simplenote.csv which can be imported.

Import into TickTick
![Importing in TickTick](docs/import-ticktick.png?raw=true "Importing in TickTick")

They will show up in a new list called *Imported Notes*. Edit and change its type to *Notes List*. Select all notes with Shift+Click and *Convert to Note*. This could not be automated. Then change sorting to *By Modified Time*.

The creation and modification times will be current time, but order will be correct.

Clean up the extra folder and list.

## Migrating Remember The Milk Tasks

Test with example file at

```shell
(venv) jesvin@jesvin-Inspiron-5559:~/dev/ticktick-migrator$ python3 migrate-rtm.py example-export-rememberthemilk.json
Wrote 5 tasks to ticktick-from-rtm.csv
```

Export your notes from
![Exporting RTM](docs/export-rtm.png?raw=true "Exporting RTM")

Run above command with exported json file and you will get ticktick-from-rtm.csv which can be imported.

Import into TickTick as described previously.