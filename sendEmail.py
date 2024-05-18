import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from a .env file located in the same directory as this script.

# Environment variables for sensitive information
GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')


def send_emails(to_list, subject, text, file_path=None , file_path2=None):
    successful_emails = []
    failed_emails = []

    for to in to_list:
        server = None
        try:
            # Set up the SMTP server
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            
                
            # Read the HTML file with explicit encoding
            with open('./email_template.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Create a MIMEMultipart message
            msg = MIMEMultipart()
            msg['From'] = DEFAULT_FROM_EMAIL
            msg['To'] = to['emailAddress']
            msg['Subject'] = subject

            # Add text and HTML to the message
            msg.attach(MIMEText(f'<p style="font-size: 22px; color:blue; direction:rtl">{text}</p>', 'html'))
            # Attach the HTML content as the email body
            msg.attach(MIMEText(html_content, 'html'))

            # Attach a file if path is provided
            if file_path:
                with open(file_path, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                    msg.attach(part)
                    
            # Attach a file if path is provided
            if file_path2:
                with open(file_path2, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path2)}')
                    msg.attach(part)

            # Send the email
            server.send_message(msg)
            successful_emails.append(to)
            print(f'Email sent successfully to {to}!')
        except Exception as e:
            print(f'Error occurred while sending email to {to}: {e}')
            failed_emails.append(to)
        finally:
            if server:
                server.quit()

    return successful_emails, failed_emails


