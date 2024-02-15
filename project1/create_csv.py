import csv
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('es_ES')  # Set the locale to Spanish

def format_phone_number(phone_number):
    # Format the phone number to match the desired format: +34 ### ### ###
    return f"+34 {phone_number[:3]} {phone_number[3:6]} {phone_number[6:9]}"

def generate_random_client():
    name = fake.name()
    email = fake.email()
    phone_number = format_phone_number(fake.phone_number())
    
    # Generate random last payment date within the past year
    last_payment_date = (datetime.now() - timedelta(days=fake.random_int(1, 365))).strftime('%Y-%m-%d')
    
    # Randomly select payment period
    payment_periods = ["monthly", "quarterly", "annually"]
    payment_period = random.choice(payment_periods)
    
    # Calculate next payment date based on payment period
    if payment_period == "monthly":
        next_payment_date = (datetime.strptime(last_payment_date, '%Y-%m-%d') + timedelta(days=30)).strftime('%Y-%m-%d')
    elif payment_period == "quarterly":
        next_payment_date = (datetime.strptime(last_payment_date, '%Y-%m-%d') + timedelta(days=90)).strftime('%Y-%m-%d')
    elif payment_period == "annually":
        next_payment_date = (datetime.strptime(last_payment_date, '%Y-%m-%d') + timedelta(days=365)).strftime('%Y-%m-%d')
    else:
        raise ValueError("Invalid payment period")

    return [name, email, phone_number, last_payment_date, next_payment_date, payment_period]

def create_csv(filename, num_clients):
    header = ["Name", "Email", "Phone Number", "Last Payment", "Next Payment", "Payment Period"]
    rows = [header]

    for _ in range(num_clients):
        client_data = generate_random_client()
        rows.append(client_data)

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)

if __name__ == "__main__":
    output_filename = "client_information.csv"
    num_clients_to_generate = 100

    create_csv(output_filename, num_clients_to_generate)
   
