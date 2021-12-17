#!/usr/bin/python3
import time
import requests

# API key for accessing Google Distance Matric API
api_key =  '' #Add your API Key from Google distance Matric API. 
base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

origin = 'Ohio'
destination= 'New York'
estimated_time=''
alarm_time=''


# Function to get traffic and historic data based commute time
def get_data():
    try:
        # Make request to get best guess duration between specified two points
        r1 = requests.get(base_url+'origins={}&destinations={}&departure_time={}&traffic_model={}&key={}'.format(origin, destination, time_in_seconds_UTC(), 'best_guess', api_key))
        r1= r1.json()['rows'][0]['elements'][0] # Convert the response to JSON
        best_guess_duration = r1['duration_in_traffic']['text']
        print("Best"+best_guess_duration)
        print(type(best_guess_duration))    
        # Make request to get worst case duration between specified two points
        #r2 = requests.get(base_url+'origins={}&destinations={}&departure_time={}&traffic_model={}&key={}'.format(origin, destination, time_in_seconds_UTC(), 'pessimistic', api_key))
        #r2 = r2.json()['rows'][0]['elements'][0] # Convert the response to JSON
        #pessimistic_duration = r2['duration_in_traffic']['text']
        #print("Worst"+ pessimistic_duration)
        #print('Estimated Drive Time' + best_guess_duration, 'PSMT: ' + pessimistic_duration, human_readable_time()) # Pass the results to display function
    except requests.exceptions.RequestException as e:
        # Print time when exception happened and exception meyyssage
        print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
        print(e)
        print('Error, check console', 'Trying again...') # Update LCD with error message
    return best_guess_duration
def get_estimate_time():
    r1 = requests.get(base_url+'origins={}&destinations={}&departure_time={}&traffic_model={}&key={}'.format(origin, destination, time_in_seconds_UTC(), 'best_guess', api_key))
    r1= r1.json()['rows'][0]['elements'][0] # Convert the response to JSON
    best_guess_duration = r1['duration_in_traffic']['text']
    print("Best"+best_guess_duration)
    print(type(best_guess_duration))    
    estimated_time=best_guess_duration
    return estimated_time    
def time_in_seconds_UTC():
    return int(round(time.time()))

def human_readable_time():
    return time.strftime("%d %b %Y %I:%M %P", time.localtime())
def set_alarm():
    global origin
    origin=input("Enter your Origin: ")
    print(origin)
    global destination
    destination=input("Enter your Destination: ")
    print(destination)
    estimated_time=get_estimate_time()
    print("estimated_time "+estimated_time)
    alarm_time=input("Please set your alarm accordingly in format HH:MM")
    print(alarm_time)
    return estimated_time,alarm_time
def job():
    print("Alarm " +human_readable_time())

def main():
    
    estimated_time,alarm_time=set_alarm()
    while True:

        updated_time=get_data()
#all times are string change them to compare
        if estimated_time>updated_time:
            final_time=abs(estimated_time-updated_time)
            alarm_time=alarm_time-updated_time
        elif updated_time>estimated_time:
            final_time=updated_time-estimated_time
            alarm_time=alarm_time+updated_time
        job(alarm_time)
    #get_data() # Gets and displays data on LCD
    #time.sleep(60) # Wait for 1 minute
main()
# Keep the program running and update LCD every 1 minute
