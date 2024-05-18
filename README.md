## Project Title: Email Sender for Job Recruiting

This script is designed to send messages to a list of emails, specifically created for sending emails to lists of job recruiting contacts.

## Features

- Send messages to a list of email addresses.
- Filter and validate email addresses to ensure they are legally compliant.
- Automate the distribution of recruiting messages to potential job candidates.

## Installation

Ensure you have Python 3.x installed on your PC. Follow these steps:

1. Clone or fork the repository:

git clone https://github.com/matlin100/send_email_for_all_jobs_list.git

2. Install the required Python packages:

pip install python-dotenv email-validator

## Setup

1. Create an `.env` file to store your email and password:

GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password

### Steps to Create an App Password

1. **Navigate to Google Security Settings**:
   - Access your Google Account security settings by visiting [Google Security Settings](https://myaccount.google.com/security).

2. **Enable 2-Step Verification**:
   - If not already enabled, turn on 2-Step Verification to add an additional layer of security to your account.

3. **Generate a New App Password**:
   - Return to the Security page, scroll down to find the “App passwords” section, and generate a new password. This is necessary if you are using 2-Step Verification.

4. **Update Your .env File**:
   - Insert the generated password into your `.env` file under the variable `GMAIL_APP_PASSWORD`.

Please ensure to keep your app passwords secure and never share them publicly.

### Setup Email List

1. Create a `data.json` file in the `./data` directory (`./data/data.json`).
2. In `data.json`, put your email list in the following structure:
```json
[
    {"emailAddress": "email1@example.com"},
    {"emailAddress": "email2@example.com"}
    ...
]

```
### Add CV PDF to Email

If you want to send a CV PDF file:
- Add your CV to the `./data` folder.
- Rename it appropriately (typically to `CV.pdf`) to ensure consistency and easy identification. The path should then be `./data/CV.pdf`. to CV.pdf > ./data/CV.
## run
run the main file and it will send the emails to all
it will print the list of successful emails 
and unsuccessful emails 
### helpers 
if needed you can import from the helpers folder function to check if email is valid and remove duplicate emails 


