from flask import Flask, render_template, url_for, redirect, request
import requests 
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def info():

    if request.method == "POST":
        dep_ar = request.form['dep_ar']
        arr_ar = request.form['arr_ar']
        fl_num = request.form['fl_num']
    

    


        api_result = requests.get('http://api.aviationstack.com/v1/flights?access_key=###')


        flight_data = api_result.json()
        #flight_info = flight_data['data']

        items=[]
        for i in flight_data['data']:
            departure = i['departure']['airport']
            airline = i['airline']['name']
            dep_term = i['departure']['terminal']
            dep_gate = i['departure']['gate']
            depest_t = i['departure']['estimated']
            arrival = i['arrival']['airport']
            arr_term = i['arrival']['terminal']
            arr_gate = i['arrival']['gate']
            arrest_t = i['arrival']['estimated']
            flight_number = i['flight']['number']

            
            
            if dep_ar == departure:
                items.append({'departure' : departure, 'arrival' : arrival, 'flight_number' : flight_number, 'dep_term' : dep_term, 'dep_gate' : dep_gate, 'depest_t' : depest_t, 'arr_term' : arr_term, 'arr_gate' : arr_gate, 'arrest_t' : arrest_t, 'airline' : airline})
                
            if arr_ar == arrival:
                items.append({'departure' : departure, 'arrival' : arrival, 'flight_number' : flight_number, 'dep_term' : dep_term, 'dep_gate' : dep_gate, 'depest_t' : depest_t, 'arr_term' : arr_term, 'arr_gate' : arr_gate, 'arrest_t' : arrest_t, 'airline' : airline})
            
            if fl_num == flight_number:
                items.append({'departure' : departure, 'arrival' : arrival, 'flight_number' : flight_number, 'dep_term' : dep_term, 'dep_gate' : dep_gate, 'depest_t' : depest_t, 'arr_term' : arr_term, 'arr_gate' : arr_gate, 'arrest_t' : arrest_t, 'airline' : airline})
                
          
        
        return render_template("voila.html", items=items)

    
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)


    

