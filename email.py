# First we create an inbox list which will store emails and their messages as dictionaries
outlook_inbox = []

outlook_outbox = []
# Then we create an Email object that represents a single email
class Email():

    def __init__(self,from_address,email_contents,has_been_read = False,is_spam = False):
        self.has_been_read = has_been_read
        self.email_contents = email_contents
        self.is_spam = is_spam
        self.from_address = from_address
        
    def mark_as_read(self,read):
        self.has_been_read = read
    
    def mark_as_spam(self,spam):
        self.is_spam = spam

    

def add_email(email,contents):
    new_mail = Email(from_address = email,email_contents = contents)
    outlook_inbox.append(new_mail)
    return new_mail

def send_mail(email,contents):
    new_mail = Email(from_address = email,email_contents = contents)
    outlook_outbox.append(new_mail)
    return new_mail

def get_count():
    return f'The number of messages in the inbox are {len(outlook_inbox)}.'

def get_email():
    index = int(input("Please enter the index of the email you would like to see.\n"))
    while index not in range(len(outlook_inbox)):
        index = int(input("You did not enter a valid number.Please enter the index of the email you would like to see.\n"))
    else:
        outlook_inbox[index].has_been_read = True
        print(f''' The email from {outlook_inbox[index].from_address} are as follows:
        {outlook_inbox[index].email_contents}.''')


def get_unread_emails():
    return [{i.from_address,i.email_contents} for i in outlook_inbox if i.has_been_read == False]

def get_spam_emails():
    return [{i.from_address,i.email_contents}for i in outlook_inbox if i.is_spam == True]

def delete():
    index = int(input("Please enter the index of the email you would like to see.\n"))
    while index not in range(len(outlook_inbox)):
        index = int(input("You did not enter a valid number.Please enter the index of the email you would like to see.\n"))
    else:
        print(f''' The email from {outlook_inbox[index].from_address} is as follows: 
        {outlook_inbox[index].email_contents}.''')
        ask = input("Would you like to delete this email?Yes or No\n").lower()
        if ask == "yes":
            del outlook_inbox[index]

# -------------------------- Emails
mail1 = add_email('zafarhassan1@live.co.uk','hello how are you?')
mail2 = add_email('zafarhassan2@live.co.uk','hello how are you?')
mail3 = add_email('zafarhassan3@live.co.uk','hello how are you?')


user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/delete/quit?\n")
    if user_choice == "read":
        print(get_count())
        get_email()
        choice2 = input("Would you like to see the rest of the unread mails?yes or no\n").lower()
        if choice2 == "yes":
            print(get_unread_emails())
    elif user_choice == "mark spam":
        
        index1 = int(input("Please enter the index of the email you would like to mark as spam.\n"))
        while index1 not in range(len(outlook_inbox)):
            index1 = int(input("You did not enter a valid number.Please enter the index of the email you would like to see.\n"))
        else:
            outlook_inbox[index1].is_spam = True
            input3 =  input("Would you like to see the spam emails? yes or no\n").lower()
            if input3 == "yes":
                print(get_spam_emails())

    elif user_choice == "send":
        email = input("please enter your email address.\n")
        contents = input("please enter the email.\n")
        new_send_mail = send_mail(email,contents)
        print(f''' Please see the outbox below:
        {[{i.from_address,i.email_contents} for i in outlook_outbox]}''')

    elif user_choice == "delete":
        delete()
        print(f''' Please see the remaining inbox below:
        {[{i.from_address,i.email_contents} for i in outlook_inbox]}''')
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
