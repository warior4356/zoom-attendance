# Zoom Attendance
 
This script will take a folder of csv files from Zoom meeting usage Reports and aggregate them into a set of attendance documents

Note: Don't choose the "Export with meeting data" option.

Attendance Time - Collection of how long each member attended each meeting

Attendance Any - Meetings that the member attended for any length of time

Attendance Full - Meetings the member attended for <minimum time> (All times are in minutes)

eg
```
$ python parser.py <path to reports folder> <minimum time>
```
