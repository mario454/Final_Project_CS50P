import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user import User

SENDER = "pyp982744@gmail.com"  #email of sender
PASSWORD = ""  # App password

def OTP(receive, message = "otp"):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()   # Adding TLS security

    server.login(SENDER, PASSWORD)

    msg = MIMEMultipart()
    msg["From"] = SENDER
    msg["To"] = receive
    # Get OTP as random number
    otp = ''.join([str(random.randint(0,9)) for _ in range(6)])

    if message == "otp":

        msg["Subject"] = "Verification Code"

        body="""
            <html>
                <body>
                    <h2 style="display:inline;">Your OTP: <h1 style="display: inline; color:red; margin-left: 10px;"> """ + otp + """ </h1></h2>
                </body>
            </html>
        """
    else:
        msg["Subject"] = "Bought things"

        body="""
        <html>
            <body>
                <h1> Thank you for visit us 😊</h1>
                <h2> Total price: """ + str(message[-1][1]) +""" $</h2>
                <h3 style="margin-top:30px;"> Bye, """ + User.username +""" </h3>
            </body>
        </html>
         """


    msg.attach(MIMEText(body, "html"))

    # Send email
    server.sendmail(SENDER, receive, msg.as_string())
    server.quit()

    return otp

# Verify received otp from user
def verify_otp(received_otp, generated_otp):
    return received_otp == generated_otp
