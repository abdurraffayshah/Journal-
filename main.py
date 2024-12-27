from journal import Journal
import sys
from tabulate import tabulate
from pyfiglet import Figlet

def main():
    title()
    menu()
    tries = 3
    while tries > 0:
        user = input("Input: ").lower()
        if user == "w":
            date = input("Date (D/M/Y): ")
            if Journal.date_verification(date)==True:
                journal = input("Journal: ")
                print(Journal.writing_journal(date, "journal.csv", journal))
                sys.exit()
            else:
                print("Please enter a valid date")
                tries-=1
        elif user == "r":
            read_date = input("Please input the date of the journal you would like to read (D/M/Y): ")
            journal=Journal.reading_journal(read_date, "journal.csv")
            print(journal)
            sys.exit()
        elif user == "e":
            sys.exit("See You Later")
        else:
            print("Please input something valid")
            tries -= 1
            if tries == 0:
                print("Too many invalid attempts. Exiting the program.")


def title():
    figlet=Figlet()
    font = "slant"
    figlet.setFont(font=font)
    rendered_title=figlet.renderText("Journal")
    print(rendered_title)

def menu():
    data={"OPTIONS":["Write", "Read", "Exit"],
          "KEYS":["W", "R", "E"]}
    print(tabulate(data, headers="keys", tablefmt="double_grid"))


if __name__=="__main__":
    main()
