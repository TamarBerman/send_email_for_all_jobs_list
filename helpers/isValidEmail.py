import json
from email_validator import validate_email, EmailNotValidError

# Define the path to your JSON file
file_path = '../data/data.json'

# Open the file and load the data with json.load
with open(file_path, 'r') as file:
    email_data = json.load(file)


# Function to filter invalid emails using the email_validator library
def filter_invalid_emails(email_data):
    valid_emails = []
    invalid_emails = []

    for item in email_data:
        # Corrected line: apply 'replace' on item["emailAddress"] instead of 'item'
        cleaned_email = item["emailAddress"].replace('\u200f', '')\
            .replace(',', '')\
            .replace('\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 ', '')\
            .replace('\xa0', '')\
            .replace('\\u200', '')\
            .replace('\u200e', 'e')
        try:
            # Validate and normalize the email
            valid = validate_email(cleaned_email)
            email = valid.email  # normalized form
            valid_emails.append({"emailAddress": email})
        except EmailNotValidError as e:
            # Email is not valid, add it to the list of invalid emails
            invalid_emails.append(cleaned_email)  # Use cleaned_email, not cleaned_email["emailAddress"]

    print(f"valid emails {len(valid_emails)} : {valid_emails}")
    print(f"invalid emails {len(invalid_emails)}: {invalid_emails}")
    return valid_emails, invalid_emails


