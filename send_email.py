import smtplib
import ssl

# Define a function to send an email with a given message
def sendEmail(message):
    smtp_server = "smtp.gmail.com"  # SMTP server for Gmail
    port = 587  # Port for TLS (Transport Layer Security) connection
    sender_email = "your-email-here"  # Replace with the sender's email address
    password = "enter-your-password"  # Replace with the sender's email password
    receiver_email = "your-email-here"  # Replace with the recipient's email address

    context = ssl.create_default_context()  # Create a secure SSL/TLS context

    try:
        server = smtplib.SMTP(smtp_server, port)  # Create an SMTP server connection
        server.ehlo()  # Identify yourself to the SMTP server
        server.starttls(context=context)  # Upgrade the connection to use TLS
        server.ehlo()  # Reidentify after the TLS handshake
        server.login(sender_email, password)  # Login to the sender's email account
        server.sendmail(sender_email, receiver_email, message)  # Send the email

    except Exception as e:
        print(e)  # Print any exceptions or errors that occur during the process

    finally:
        server.quit()  # Ensure that the SMTP server connection is properly closed
