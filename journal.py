import csv
import re


class Journal:
    def __init__(self, date, file, journal):
        self.date=date
        self.file=file
        self.journal=journal

    def reading_journal(date, file):
        found=False
        try:
            with open(file, "r") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if row[0]==date:
                        found=True
                        return row[1]
            if found==False:
                return f"There is no Journal for {date}"
        except FileNotFoundError:
            print("Error. File couldnt be found")

    def writing_journal(date, file, journal):
        with open(file, "a", newline='') as file:
            csvreader=csv.writer(file)
            csvreader.writerow([date, journal])
        return "Journal saved."

    def date_verification(date):
        if re.match("^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/(\d{4})$", date):
            return True
        else:
            return False
