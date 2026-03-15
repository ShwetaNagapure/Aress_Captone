import smtplib
from email.mime.text import MIMEText
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS


def send_email(to_email, subject, body):

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    try:

        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()

        server.login(SMTP_USER, SMTP_PASS)

        server.sendmail(
            SMTP_USER,
            to_email,
            msg.as_string()
        )

        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Email error:", e)