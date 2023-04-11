import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from io import BytesIO
from random import choice


topic = "money"
topic2 = 'power'
topic3 = 'wealth'
topic4 = 'motivation'
topic_list = [topic, topic2, topic3, topic4]

email_sender = "mikepython94@gmail.com"
email_password = "srkagauykuxgdxdv"
email_recipient = 'adenmoriarty25@outlook.com'


def get_quote():
    response = requests.get('https://type.fit/api/quotes')
    quotes = response.json()

    motivational_quotes = [quote for quote in quotes if topic.lower() in quote['text'].lower()
                           or topic2.lower() in quote['text'].lower()
                           or topic3.lower() in quote['text'].lower()
                           or topic4.lower() in quote['text'].lower()]
    motivational_quote = choice(motivational_quotes)

    quote = motivational_quote['text']
    author = motivational_quote['author']

    ready_to_send = MIMEText(f'{quote} - {author}')
    return ready_to_send


def get_image():

    image_url = f"https://source.unsplash.com/random?{choice(topic_list)}"
    response = requests.get(image_url)
    image_data = BytesIO(response.content)
    return image_data


def send_email():

    # attach message
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = f"Daily Inspiration: {topic4.capitalize()}"
    msg.attach(get_quote())

    # attach image
    image = MIMEImage(get_image().read())
    image.add_header('Content-Disposition', 'attachment', filename="inspiration.jpg")
    msg.attach(image)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_recipient, msg.as_string())
        print("Email sent successfully!")


send_email()
