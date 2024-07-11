The project tracks youth tariffs of the "Air Astana" airline through Aviata.kz.

- Pandas is used for reading and processing input data such as origin and destination and date is read from a 'data.csv' file. 

input_process.py : 
- It sends HTTP post request to the Amadeus API and acquire 'access token' using API_key and API_secret.
- get_city method finds IATA codes of the airport with HTTP GET request. 

- Selenium's Webdriver parses dates and prices.

- If there are flights by "Air Astana" and their cost is less than from certain amount (youth tarrifs generally cost little less than 16.000 tenge) it will send these offers via email using SMTP.


<p>Data Parsing process</p>

![ScreenRecording2024-07-09at14 22 21-ezgif com-video-to-gif-converter](https://github.com/Akim-Edige/flight-offer-tracker/assets/115921160/ace6a3e0-975d-4bf2-a6dd-4f95966954fb)


<p>After parsing, email is send automatically</p>

![ScreenRecording2024-07-09at14 22 212-ezgif com-video-to-gif-converter](https://github.com/Akim-Edige/flight-offer-tracker/assets/115921160/c88720cb-4d14-4b90-a2c5-676701b8a14f)






