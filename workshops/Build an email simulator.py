import datetime

class Email: # Represents an email message basically a container for email data
    def __init__(self, sender, receiver, subject, body):  
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False  

    def mark_as_read(self): # Marks the email as read
        self.read = True # Marks the email as read

    def display_full_email(self): # Displays the full email content
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self): # String representation of the email for inbox listing
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
class Inbox: # Manages a collection of emails for a user
    def __init__(self):
        self.emails = []

    def receive_email(self, email): # Adds a new email to the inbox
        self.emails.append(email)

    def list_emails(self): # Lists all emails in the inbox
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):  
            print(f'{i}. {email}')


    def read_email(self, index): # Reads a specific email by index
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index): # Deletes a specific email by index
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
class User: # Represents a user who can send and receive emails
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body): # Sends an email to another user
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self): # Checks and lists emails in the inbox
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index): # Reads a specific email from the inbox
        self.inbox.read_email(index)

    def delete_email(self, index): # Deletes a specific email from the inbox
        self.inbox.delete_email(index)

def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()
if __name__ == '__main__':
    main()