def remove_duplicate_emails(email_list):
    # Create an empty list to store unique emails
    unique_emails = []
    # Create an empty set to store encountered email addresses
    seen = set()

    # Iterate through each dictionary in the list
    for item in email_list:
        # Extract the email address from the dictionary
        email = item['emailAddress']
        # Check if the email has already been encountered
        if email not in seen:
            # If not, add it to the unique emails list and mark it as seen
            unique_emails.append(item)
            seen.add(email)

    # Return the list of dictionaries with unique email addresses
    return unique_emails

