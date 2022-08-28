
def getText():
    Text = "Hello.  So this is a live demo that we are trying to give very we are going to show how the platform detects various insights can do transcription in real-time and also the different topics of discussions, which would be generated after the call is over, and they will be an email that will be sent to the inbox.  So that is the idea.  So I am going to do a quick conversation.  I would say where I will demonstrate all of this great catching up.  Thanks for calling good to hear.  From you.  And I would love to hear more about what you have to offer?  I will set up a time and appointment probably sometime tomorrow evening where we can go over the documents that you are providing.  I love all the plants.  I just need to discuss with my family in terms of which one will we go forward with it?  It very excited to hear from you and the discount and look forward to talking sharply.  I have a quick question though.  Is there basically website?  Where I can go to and look at all these details myself.  It will be very helpful.  Can you also share the quotation to me on email so that I can go ahead and talk about it with my other kind of folks in the family? Thanks a lot.  Thanks for calling good catching up.  Talk soon."
    return Text
    
class Event:
    def __init__(self, date, time, name, email, number, user):
        self._date = date
        self._time = time
        self._name = name
        self._email = email
        self._number = number
        self.user = user

    def date(self):
        return self._date

    def time(self):
        return self._time

    def name(self):
        return self._name

    def email(self):
        return self._email

    def number(self):
        return self._number

    def user(self):
        return self._user

def processText(Text):
    Text = str(Text)
    Text = Text.lower()
    user = findUser()
    date = findDate(Text)
    time = findTime(Text)
    name = findName()
    email = findEmail(Text)
    number = findNumber(Text)
    event = Event(date, time, name, email, number, user)
    return event

def findUser():
    pass

def findDate(Text):
    date = ""
    listMonths = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    for item in listMonths:
        index = Text.find(item)
        if index != -1:
            index = index + len(item) - 1
            for i in range(9):
                digit = Text[index + i]
                if digit.isDigit():
                    date += digit
                else:
                    date = ""
            if date == "":
                index = index - len(item) - 8
                for i in range(9):
                    digit = Text[index + i]
                if digit.isDigit() or digit == ",":
                    date += digit
                    return item + " " + date
                else:
                    date = noDate()
            else:
                return item + " " + date
        else:
            date = noDate()
    return item + " " + date

def noDate():
    err_msg = "No date detected, please enter a date with the full month name"
    new_text = "*this should be the new text that gets inputted into the code*"
    return findDate(new_text)

def findTime(Text):
    moreColons = True
    lastInd = 0
    while moreColons == True:
        index = Text.find(":", lastInd)
        if index != -1:
            time = Text[index-2:index+2]
            for i in time:
                if i.isDigit() or i == ":":
                    pass
                else:
                    time = noTime()
                return time
        else:
            moreColons = False
            time = noTime()
    return time

def noTime():
    err_msg = "No time detected, please enter a time in the format XX:XX (24 hour time)"
    new_text = "*this should be the new text that gets inputted into the code*"
    return findTime(new_text)

def findName():
    pass

def findEmail(Text):
    Text = Text.split()
    for item in Text:
        if Text.find("@") == True:
            if item[-4] == ".com":
                return item
    return noEmail()

def noEmail():
    err_msg = "No email detected, please enter a valid email"
    new_text = "*this should be the new text that gets inputted into the code*"
    return findEmail(new_text)

def findNumber():
    Text = Text.split()
    for item in Text:
        if len(item) >= 10:
            for i in item:
                if i.isDigit():
                    pass
                else:
                    return noNumber()
            return item
    return noNumber()

def noNumber():
    err_msg = "No phone number detected, please enter a valid number"
    new_text = "*this should be the new text that gets inputted into the code*"
    return findNumber(new_text)

def submitEvent(event):
    pass

def main():
    event = processText(getText)
    submitEvent(event)

main()
