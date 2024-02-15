import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

def send_email (sender,client_name,to_email,payment_date,next_payment_date):
    
    load_dotenv()
    title = "Recordatorio de pago"
    msg = MIMEMultipart()

    #Alternative css

    css_style_alternative = """
        <style>
            /* Add your custom styles here */
            body {
                font-family: Arial, sans-serif;
                background-color: #222222;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                text-align: center;
                margin-bottom: 20px;
            }
            .header img {
                max-width: 200px;
                height: auto;
            }
            .content {
                background-color: #333333;
                padding: 30px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            .content h1 {
                color: #ffffff;
                font-size: 24px;
                margin-bottom: 20px;
            }
            .content p {
                color: #cccccc;
                font-size: 16px;
                line-height: 1.5;
            }
            .cta-button {
                display: inline-block;
                background-color: #007bff;
                color: #ffffff;
                text-decoration: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                margin-top: 20px;
            }
        </style>
    """

    html_mensaje= f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            /* Add your custom styles here */
        {css_style_alternative}
        </style>
    </head>
    <body>
        <div style="background-color: #f2f2f2; padding: 20px;">
            <h1 style="text-align: center;">{title}</h1>
            <hr>
            <p>Hola {client_name}, </p>
                
           El proposito de este email es recordarle que tiene un pago pendiente en nuestra plataforma. Su último pago fue el día {payment_date} y su pago debió ser realizado el día {next_payment_date}. Si ya ha realizado el pago, por favor ignore este mensaje. Si no ha realizado el pago, por favor hágalo lo antes posible. Si tiene alguna duda, puede contactar con nosotros a través de este email o llamando al 555-555-555.
                
            <hr>
            <p>Saludos,</p>
            <p>{sender}</p>
        </div>
    </body>
    </html>
    """

    # Attach the HTML content to the email
    msg.attach(MIMEText(html_mensaje, 'html'))
       
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv("EMAIL")
    smtp_password = os.getenv("PASSWORD")

    # Email configuration
    sender_email = sender
    subject = f'Recordatorio de pago'
    msg['From'] = sender_email
    msg['Subject'] = subject

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        # Send the email
        msg['To'] = to_email
        server.sendmail(sender_email, to_email, msg.as_string())            

        server.quit()

    except smtplib.SMTPException as e:
        raise ValueError(e + "Error sending email") # let raise the error

