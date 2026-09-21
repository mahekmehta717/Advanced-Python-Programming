import re


def find_emails(text):
    # Pattern for matching email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find all email addresses in the text
    emails = re.findall(pattern, text)

    return emails


# Get input from the user
text = input("Enter a text: ")

# Find and display email addresses
emails = find_emails(text)

print("Email addresses found:", emails)
