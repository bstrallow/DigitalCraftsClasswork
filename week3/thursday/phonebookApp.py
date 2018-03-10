from phonebook import *
thisPhonebook = phonebook()
def runApp():
    whatDo = int(raw_input("""
    Electronic Phone Book
    =====================
    1. Look up an entry.
    2. Create an entry.
    3. Delete an entry.
    4. List all entries.
    5. Exit
    """))
    if whatDo == 1:
        name = raw_input("Enter the name of the person you want to call: ")
        print "..."
        thisPhonebook.lookUp(name)
        appContinue()
    elif whatDo == 2:
        name = raw_input("Enter the name for this new entry: ")
        number = raw_input("Enter the number associated with that name: ")
        print "..."
        thisPhonebook.setEntry(name, number)
        appContinue()
    elif whatDo == 3:
        name = raw_input("Enter the name of the entry you wish to delete: ")
        print "..."
        thisPhonebook.deleteEntry(name)
        appContinue()
    elif whatDo == 4:
        print "Phonebook Entries: \n"
        thisPhonebook.listAll()
        appContinue()
    else:
        print "Thank you, have a nice day."
def appContinue():
    keepGoing = raw_input("Would you like to continue? y/n \n")
    if keepGoing == 'y':
        runApp()
    else:
        print "Thank you, have a nice day."
runApp()