import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from flight_offer import Offer
from input_process import Getiata
import pandas




# Reading input information such as flight origin and destination and date from data.csv

db = []
data = pandas.read_csv("data.csv")

# Getting IATA code of the cities by Amadeus API
iata = Getiata()
row=[]
for (index,r) in data.iterrows():
    row.append(iata.get_city(r.From))
    row.append(iata.get_city(r.Destination))
    row.append(r.Dates)
    db.append(row)
    row=[]




result = {}


for date in db:

    r_options = Options()
    r_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=r_options)


    driver.get(f"https://aviata.kz/aviax/search/{date[0]}-{date[1]}{date[2]}0001E")

    time.sleep(5)

    # Find all elements with data-component="offer"

    offers = driver.find_elements(By.CSS_SELECTOR, 'div[data-component="offer"]')


    # Loop through the list of found elements and look for 'Air Astana' airline offers
    list = []
    for offer in offers:
        flight_code = offer.get_attribute('data-flight-code')
        cost = int(offer.find_element(By.CSS_SELECTOR, '.text-xl').text.replace(" ","").replace("₸",""))
        airline = offer.find_element(By.CSS_SELECTOR, '.text-sm').text
        times = offer.find_elements(By.CSS_SELECTOR, '.leading-none')

        if (airline == 'Air Astana' and cost<15000):

            # Creating class object 'Offer' for convenient storage and processing
            off = Offer(times[0].text,times[1].text, date[0], date[1], cost, airline)
            list.append(off)

    if list:
        # If offers found it included in the result dictionary
        result[date[2]]=list

    driver.quit()
    time.sleep(5)


# sending an email if offers found for any date frome data.csv

email_text = ""

if bool(result):
    email_text+="Here some offers:"
    for key,values in result.items():
        email_text+=f"___________\n{key}:"
        i = 1
        for offer in values:
            email_text+=f"{i}. {offer.display()}"
            i+=1
        email_text+="___________\n"


    my_email = "akimali.edige@gmail.com"
    password = "nvxgqfelibftsjrd"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="edige.akimali@nu.edu.kz",
            msg=f"Subject:Flight Offer Alert\n\n {email_text}"
        )

