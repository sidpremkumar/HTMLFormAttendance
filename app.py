import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime, time

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Flask information
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Google Sheets API
# TODO: Enter relevent information here:
client_id = ""
client_secret = ""

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# TODO: Create your own client secret
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
# TODO: Enter your own workbook name
sheet = client.open("").sheet1

# Attendence post requeset
@app.route('/submit', methods= ['POST'])
def create():
    # Get information from the form
    labnumber = request.form['labnumber']
    username = request.form['username']
    secret = request.form['secret']

    # Convert the inputs to ints
    labnumber = int(labnumber)
    secret = int(secret)

    ret = "Uh Oh, something went wrong."
    # Extract all of the values
    data = sheet.get_all_records()

    # Variable to keep track of if we found the user
    found = False

    # Find the row corresponding to the username
    for x in range(len(data)):
        if data[x]['Username '] == username:
            row = x + 2
            found = True
            break
    # Create a datetime object
    d = datetime.now()
    # If we were able to find the user
    if found == True:
        # The secret depends on the lab
        if labnumber == 0:
          ret = "Invalid secret"
        elif labnumber == 1:
            ret = "Invalid secret"
        elif labnumber == 2:
            ret = "Invalid secret"
        elif labnumber == 3:
            # Assign the correct Lab timings:
            section1 = d.replace(hour=14, minute=50, second=0,  day=14, month=2)
            section2 = d.replace(hour=16, minute=25, second=0,  day=14, month=2)
            section3 = d.replace(hour=9, minute=55, second=0,  day=15, month=2)
            section4 = d.replace(hour=11, minute=0, second=0,  day=15, month=2)

            if (secret == 4892  and d < section1):
                # If the secret matches update the row
                sheet.update_cell(row, 5, "1")
                ret = "Your attendence has been taken"
            elif (secret == 4394 and d < section2):
                # If the secret matches update the row
                sheet.update_cell(row, 5, "1")
                ret = "Your attendence has been taken"
            elif (secret == 3038 and d < section3):
                # If the secret matches update the row
                sheet.update_cell(row, 5, "1")
                ret = "Your attendence has been taken"
            elif (secret == 3904 and d < section4):
                # If the secret matches update the row
                sheet.update_cell(row, 5, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 4:
            if secret == 3038 or secret == 3028 or secret == 3719 or secret == 3918:
                # If the secret matches update the row
                sheet.update_cell(row, 6, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 5:
            if secret == 3271 or secret == 5792 or secret == 9347 or secret == 3920:
                # If the secret matches update the row
                sheet.update_cell(row, 7, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        if labnumber == 6:
            if secret == 3490 or secret == 9802 or secret == 2028 or secret == 3920:
                # If the secret matches update the row
                sheet.update_cell(row, 8, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 7:
            if secret == 3402 or secret == 4393 or secret == 3928 or secret == 9282:
                # If the secret matches update the row
                sheet.update_cell(row, 9, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 8:
            if secret == 9282 or secret == 3928 or secret == 9292 or secret == 7020:
                # If the secret matches update the row
                sheet.update_cell(row, 10, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 9:
            if secret == 3092 or secret == 3829 or secret == 2928 or secret == 9201:
                # If the secret matches update the row
                sheet.update_cell(row, 11, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 10:
            if secret == 3028 or secret == 1092 or secret == 3928 or secret == 1029:
                # If the secret matches update the row
                sheet.update_cell(row, 12, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 11:
            if secret == 2029 or secret == 1019 or secret == 2029 or secret == 1010:
                # If the secret matches update the row
                sheet.update_cell(row, 13, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 12:
            if secret == 3910 or secret == 1039 or secret == 3819 or secret == 9102:
                # If the secret matches update the row
                sheet.update_cell(row, 14, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
        elif labnumber == 13:
            if secret == 8192 or secret == 8201 or secret == 8192 or secret == 3910:
                # If the secret matches update the row
                sheet.update_cell(row, 15, "1")
                ret = "Your attendence has been taken"
            else:
                ret = "Invalid secret"
    # Else state that we could not find the username
    else:
        ret = "Could not find username"

    return(jsonify({"response":ret}))
