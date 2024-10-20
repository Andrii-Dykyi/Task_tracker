from pydantic import EmailStr


async def send_notification_email(to: EmailStr, subject: str, body: str):
    print(f"Notification email is being sent to {to}")
    print(f"Subject: {subject}\n{body}")
