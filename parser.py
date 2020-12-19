# Script by Ryal O'Neil ryal.oneil@wsu.edu
# Check https://github.com/warior4356/zoom-attendance for updates

import os, glob, sys

attendance_time = {}
attendance_any = {}
attendance_full = {}
dates = []
names = {}

if not len(sys.argv) == 3:
    print("Please format with: parser.py <path to input directory> <time to attend>")
    exit(0)

folder_path = sys.argv[1]
attend_time = int(sys.argv[2])

for filename in glob.glob(os.path.join(folder_path, '*.csv')):
    local_attend = {}
    date = ""
    attend_file = open(filename, "r", encoding='utf-8-sig')
    first_skipped = False
    for line in attend_file:
        if not first_skipped:
            first_skipped = True
            continue

        words = line.split(',')

        if not date:
            date = words[2].split()[0]
            dates.append(date)

        if not words[1] in names.keys():
            names[words[1]] = words[0]

        if not words[1] in local_attend.keys():
            local_attend[words[1]] = int(words[4])
        else:
            local_attend[words[1]] = int(words[4]) + int(local_attend[words[1]])

    for email in local_attend.keys():
        if not email in attendance_time.keys():
            attendance_time[email] = {}

        if not "total" in attendance_time[email].keys():
            attendance_time[email]["total"] = local_attend[email]
        else:
            attendance_time[email]["total"] = local_attend[email] + attendance_time[email]["total"]

        attendance_time[email][date] = local_attend[email]

        if not email in attendance_any.keys():
            attendance_any[email] = {}

        if not "total" in attendance_any[email].keys():
            attendance_any[email]["total"] = 1
        else:
            attendance_any[email]["total"] = 1 + attendance_any[email]["total"]

        attendance_any[email][date] = True


        if local_attend[email] >= attend_time:
            if not email in attendance_full.keys():
                attendance_full[email] = {}

            if not "total" in attendance_full[email].keys():
                attendance_full[email]["total"] = 1
            else:
                attendance_full[email]["total"] = 1 + attendance_full[email]["total"]

            attendance_full[email][date] = True

outfile_time = open("attendance_time.csv", "w")
outfile_any = open("attendance_any.csv", "w")
outfile_full = open("attendance_full.csv", "w")

header = "Name,Email,Total"

for date in dates:
    header = header + "," + date

outfile_time.write(header + "\n")
outfile_any.write(header + "\n")
outfile_full.write(header + "\n")

for email in attendance_time:
    line = names[email] + "," + email +"," + str(attendance_time[email]["total"])
    for date in dates:
        if date in attendance_time[email].keys():
            line = line + "," + str(attendance_time[email][date])
        else:
            line = line + ","

    outfile_time.write(line + "\n")

for email in attendance_any:
    line = names[email] + "," + email +"," + str(attendance_any[email]["total"])
    for date in dates:
        if date in attendance_any[email].keys():
            line = line + "," + str(attendance_any[email][date])
        else:
            line = line + ","

    outfile_any.write(line + "\n")

for email in attendance_full:
    line = names[email] + "," + email +"," + str(attendance_full[email]["total"])
    for date in dates:
        if date in attendance_full[email].keys():
            line = line + "," + str(attendance_full[email][date])
        else:
            line = line + ","

    outfile_full.write(line + "\n")