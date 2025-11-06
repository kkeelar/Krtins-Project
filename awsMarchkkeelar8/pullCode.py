import imaplib
import email
import re
from bs4 import BeautifulSoup

def fetch_emails():
    # Connect to the IMAP server (for Gmail, use 'imap.gmail.com')
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    # Login to your email account
    mail.login('kkeelar8@gmail.com', 'wqym aqmq dzkn qvfe')

    # Select the mailbox where you want to search for emails (e.g., 'INBOX')
    mail.select('inbox')

    # Search for emails with the specified subject
    result, data = mail.search(None, 'SUBJECT "Your ESPN Account Passcode"')

   # Get the ID of the most recent email with the specified subject
    email_ids = data[0].split()
    if email_ids:
        latest_email_id = email_ids[-1]
    else:
        print("No emails found with the specified subject.")
        return None

    # Fetch the content of the most recent email
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Extract the email content
    email_content = None
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/html":
                email_content = part.get_payload(decode=True).decode()
                break
    else:
        email_content = msg.get_payload(decode=True).decode()

    # Close the connection to the IMAP server
    mail.close()
    mail.logout()

    return email_content


def extract_passcode(email_content):
    # Search for the passcode in the fetched emails
    if email_content:
        soup = BeautifulSoup(email_content, 'html.parser')
        font_tag = soup.find('font', {'style': 'font-size:2em;font-weight: bold;'})
        if font_tag:
            passcode = font_tag.text.strip()
            if len(passcode) == 6:
                return passcode

    return None

def main():
    # Fetch the most recent email with the specified subject
    email_content = fetch_emails()

    # Extract passcode from fetched email content
    passcode = extract_passcode(email_content)

    return (passcode)


if __name__ == "__main__":
    main()
