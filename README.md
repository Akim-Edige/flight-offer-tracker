The project tracks youth tariffs of the "Air Astana" airline through Aviata.kz.

- Pandas is used for reading and processing input data such as origin and destination and date is read from a 'data.csv' file. 

input_process.py :
- 
- Finds IATA codes of the airports using the Amadeus API with HTTP GET requests. 
This API requires first to send HTTP post request to get 'access token' which is acquired by API_key and API_secret.

- Selenium's Webdriver parses dates and prices, sending offers via email using SMTP.


<p>Data Parsing process</p>




