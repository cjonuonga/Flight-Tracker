# Import necessary libraries
from flask import Flask, render_template, url_for, redirect, request  # Flask web framework components
import requests  # For making HTTP requests to the flight API
import json  # For JSON parsing
import os  # For accessing environment variables
import logging  # For logging (though not currently used in the code)

# Initialize Flask application
app = Flask(__name__)

# Define the route for the home page that accepts both GET and POST methods
@app.route('/', methods = ['GET', 'POST'])
def info():
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Extract form data for flight filtering criteria
        dep_ar = request.form['dep_ar']     # Departure airport
        arr_ar = request.form['arr_ar']     # Arrival airport
        fl_iata = request.form['fl_iata']   # Flight IATA code
        
        # Retrieve API key from environment variables (for security)
        API_KEY = os.environ.get("FLIGHT_API_KEY")
        
        # Make API request to fetch flight data
        api_result = requests.get(f'http://api.aviationstack.com/v1/flights?access_key={API_KEY}')
        
        # Parse JSON response into Python dictionary
        flight_data = api_result.json()
        print(flight_data)  # Debug print of API response
        
        # Check if the API request was successful
        if api_result.status_code != 200:
            print("Error fetching data from API")
            return render_template("index.html", error="Error fetching data from API")
        
        # Initialize empty list to store matching flight information
        items = []
        
        # Loop through all flights in the API response
        for i in flight_data['data']:
            # Extract relevant flight details from the API response
            departure = i['departure']['airport']     # Departure airport name
            airline = i['airline']['name']            # Airline name
            dep_term = i['departure']['terminal']     # Departure terminal
            dep_gate = i['departure']['gate']         # Departure gate
            depest_t = i['departure']['estimated']    # Estimated departure time
            arrival = i['arrival']['airport']         # Arrival airport name
            arr_term = i['arrival']['terminal']       # Arrival terminal
            arr_gate = i['arrival']['gate']           # Arrival gate
            arrest_t = i['arrival']['estimated']      # Estimated arrival time
            flight_iata = i['flight']['iata']         # Flight IATA code
            
            # Filter flights based on user input criteria
            # Add flight to results if departure airport matches
            if dep_ar == departure:
                items.append({
                    'departure': departure, 
                    'arrival': arrival, 
                    'flight_iata': flight_iata, 
                    'dep_term': dep_term, 
                    'dep_gate': dep_gate, 
                    'depest_t': depest_t, 
                    'arr_term': arr_term, 
                    'arr_gate': arr_gate, 
                    'arrest_t': arrest_t, 
                    'airline': airline
                })
            
            # Add flight to results if arrival airport matches
            if arr_ar == arrival:
                items.append({
                    'departure': departure, 
                    'arrival': arrival, 
                    'flight_iata': flight_iata, 
                    'dep_term': dep_term, 
                    'dep_gate': dep_gate, 
                    'depest_t': depest_t, 
                    'arr_term': arr_term, 
                    'arr_gate': arr_gate, 
                    'arrest_t': arrest_t, 
                    'airline': airline
                })
            
            # Add flight to results if flight IATA code matches
            if fl_iata == flight_iata:
                items.append({
                    'departure': departure, 
                    'arrival': arrival, 
                    'flight_iata': flight_iata, 
                    'dep_term': dep_term, 
                    'dep_gate': dep_gate, 
                    'depest_t': depest_t, 
                    'arr_term': arr_term, 
                    'arr_gate': arr_gate, 
                    'arrest_t': arrest_t, 
                    'airline': airline
                })
        
        # Render results template with the filtered flight data
        return render_template("voila.html", items=items)
    
    # If request method is GET, render the initial search form
    return render_template("index.html")

# Run the Flask application if this file is executed directly
if __name__=="__main__":
    app.run(debug=True)  # Enable debug mode for development


    

