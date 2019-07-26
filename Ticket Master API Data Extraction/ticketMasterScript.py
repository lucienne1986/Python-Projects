#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:13:31 2019

@author: lucienne
"""

#UtilizingtheTicketmasterAPI,writeaPythonscriptthat:
#
#a. Accepts a date range in the future and Ticketmaster API Key as parameters 
#b. Pulls all ​events​ in the United States with the classificationName “Musician”
#within the specified date range
#c. Segments the events pulled above by US State and generates a CSV that
#contains:
#    
#i. The state name
#ii. The musician(s) with the most events in the state
#iii. The venue with the most events in the state
#iv. The most expensive ticket price of any event in the state
#v. The event name of the event with the most expensive ticket price 
#vi. The musician(s) of the event with the most expensive ticket price

###notes on the Ticket API



##the following libraries need to installed via the termainal 
import csv
import datetime
#this is the library used to be able to extract data from the ticketmaster api
import ticketpy

#using the API key extracted during the initial registration phase
tm_client = ticketpy.ApiClient('clgynUwwtpmipM9LAjrG3dc4OkFYmWig')

#creating a querystring to look for musicians who will be playing on a future date
#searching through the EVENTS table
pages = tm_client.events.find(
        classification_Name=('Musician'),   
        #this is todays day.. needs to be changed to the future
        start_date_time = '2019-07-26T20:00:00Z'
    )
 
#for testing purposes to print on console
for event in pages:
    print(event)


print("opening csv")
#### Write API Results to CSV
with open('output.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    #these are headings to the output table
    writer.writerow(['State', 'Musician_with_the_most_events', 'Venue_with_the_most_events', 'Most_Expensive_Ticket_price', 'event_name_of_the_event_with_the_most_expensive_ticket_price', 'The_musician(s)_of_the_event_with_the_most_expensive_ticket_price'])
    #all the events for today are being stored in  a csv file
    for event in pages:
         writer.writerow([event])

print("Done searching")




