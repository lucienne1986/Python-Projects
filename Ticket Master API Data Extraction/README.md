# Project Title

Utilizing the Ticketmaster API with a Python Script

## Getting Started

1. Created an account to be able to retrieve the API key from the ticketmaster url viahttps://developer-acct.ticketmaster.com/user/login

2. Retrieve the api code to be able to extract the necessary data from Ticket Master


### Prerequisites

- On python install the following libraries:
    1. csv
    2. ticketpy
    3. json
    4. requests

### Installing

- Run ticketMasterScript.py on Python 3+

After running the script the output will be displayed in the console (this was done for quick testing purposes) and in a CSV file.


### Interview Questions

Question 1 - Explains your script’s logic to someone that is not overly technical. How did you match an event to a state? How did you keep track of each state’s most expensive ticket price?

1. Explain that we need to request (get) data from the web (api) this is called an API request 
2. Explain the purpose of having a database
3. Go though the datamodel to explain how the tables are linked
4. To be able to extract particular data from a database we need parameters e.g. state or event name. These parameters
are passed through the web to return our expected output - these are also known as querystrings
5. If we need to match an event to a state.. 
        a. Search by state e.g. 'GA' 
        b. filter the results to display only the event name
6. To keep track of each state's most expensive ticket price..
        a. Sort ticket prices starting from the highest (i.e. descending), retrieve the first one
        b. Group the prices by state code

Question 2 - Explains how to run the script, including any dependencies that must be downloaded for the script to run.

1. Dependencies required are mainly the libraries used: csv, ticketpy, json and requests. Libraries are installed through the terminal
2. Open the script called ticketMasterScript.py
3. Run the script
4. Open the output.csv file to check for the results


## Bugs
1. Date is not in the future - it is todays date
2. During this task I was refering to data model (on github data-model-ticketMaster) for the table details but the name was not always being accepted.
3. the csv does not reflect the requested outcome of this task
4. the outcome is being listed in just one column, need to extract the exact value and separate under different headings



## References
https://pypi.org/project/ticketpy/
https://developer.ticketmaster.com/products-and-docs/tutorials/
https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/


