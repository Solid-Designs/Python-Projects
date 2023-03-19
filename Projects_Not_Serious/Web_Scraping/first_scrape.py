import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib

# Define the URL to scrape
url = 'https://finance.yahoo.com/quote/%5EGSPC/components?p=%5EGSPC'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the stock data
table = soup.find('table', {'class': 'W(100%) M(0)'})
rows = table.find_all('tr')

# Create an empty list to hold the stock data
data = []

# Loop through the rows of the table and extract the stock data
for row in rows[1:]:
    cells = row.find_all('td')
    symbol = cells[0].text.strip()
    price = float(cells[1].text.strip().replace(',', ''))
    change = float(cells[2].text.strip().replace(',', ''))
    percent_change = float(cells[3].text.strip().replace('%', '')) / 100
    data.append({'Symbol': symbol, 'Price': price, 'Change': change, 'Percent Change': percent_change})

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the daily returns for each stock
df['Daily Return'] = df['Percent Change'] + 1

# Find the top-performing stocks of the day
top_stocks = df.nlargest(5, 'Daily Return')

# Define the email content
subject = 'Top-performing stocks of the day'
body = top_stocks.to_string()

# Define the email addresses and credentials
sender_email = 'your_email@gmail.com'
sender_password = 'your_email_password'
receiver_email = 'recipient_email@gmail.com'

# Create the email message
message = f'Subject: {subject}\n\n{body}'

# Send the email using Gmail's SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, message)
