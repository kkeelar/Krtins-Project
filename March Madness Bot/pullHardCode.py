import imaplib
import email
from bs4 import BeautifulSoup

def fetch_emails(emailBase, emailRealPassword):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(f'{emailBase}@gmail.com', emailRealPassword)  # Make sure password has NORMAL spaces




    # Select mailbox (check if successful)
    status, messages = mail.select('[Gmail]/Spam')
    if status != 'OK':
        print("Failed to select mailbox.")
        return None

    # Search for emails
    result, data = mail.search(None, 'SUBJECT "Your one-time passcode for ESPN"')
    if result != 'OK':
        print("No matching emails found.")
        return None
    


    # Get latest email
    email_ids = data[0].split()
    if email_ids:
        latest_email_id = email_ids[-1]
    else:
        print("No emails found with that subject.")
        return None
    


    # Fetch content
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)



    # Extract content
    email_content = None
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                email_content = part.get_payload(decode=True).decode()
                break
    else:
        email_content = msg.get_payload(decode=True).decode()

    
    print ("Step 5")

    mail.close()
    mail.logout()
    return email_content



def extract_passcode(email_content):
    if email_content:
        soup = BeautifulSoup(email_content, 'html.parser')
        # Find all td tags
        td_tags = soup.find_all('td')
        for td in td_tags:
            text = td.get_text(strip=True)
            if len(text) == 6 and text.isdigit():  # Assuming passcode is always 6-digit number
                print (text)
                return text

    return None


def main(emailBase, emailRealPassword):
    # Fetch the most recent email with the specified subject
    email_content = fetch_emails(emailBase, emailRealPassword)

    # Extract passcode from fetched email content
    passcode = extract_passcode(email_content)

    return (passcode)


if __name__ == "__main__":
    main()
