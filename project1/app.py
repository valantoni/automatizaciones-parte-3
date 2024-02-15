import csv
from datetime import datetime
from project1.send_email import send_email
from project1.send_sms import send_sms

csv_filename = 'clients_information.csv'
sender = 'Company Name'

with open(csv_filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            current_date = datetime.now().strftime('%Y-%m-%d')
            next_payment_date = row['Next Payment']
            last_payment_date = row['Last Payment']

            if next_payment_date < current_date:
                
                client_name = row['Name']
                client_email = row['Email']
                client_phone_number = row['Phone Number']
                payment_period = row['Payment Period']

                sms_message = f"Hola {client_name}, su pago ha expirado. Por favor, acceda a la plataforma y realice su pago {payment_period} lo antes posible."
                
                # Send SMS
                send_sms(sms_message,client_phone_number)
                # Send Email
                send_email(sender,client_email,last_payment_date,next_payment_date,client_name)