# HTML Form Attendance

This framework was created as a way to take attendance for a discussion/lab section of CS 112 at BU. You can learn more about it [here](http://sidpremkumar.com/htmlformattendance.html).

## Set up:
You need to change the following in app.py:
1. Place your client_secret.json
  *	```
  	# TODO: Create your own client secret
	  creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', 			scope)
    ```

2. Open the corret workbook
 * ```
  	# TODO: Enter your own workbook name
 	  sheet = client.open("").sheet1
   ```

You need to change the following in attendance.html

1. You need to enter the correct API callback id. Currently in app.py is it set to be '/submit'
  * ```
    // TODO: Enter API information here (i.e. link of where itshosted 	'.../takeAttendance')
	  ret = $.post("", {labnumber:labnumber, secret:secret, 	username:username}).done(function(data){
    ```

Finally you need to set up a correctly formatted Google Doc. You can check [here](https://docs.google.com/spreadsheets/d/1C44g0BIyvtRYvx0jLonkiUMso8dzFOKcQUGUU_AxFw8/edit?usp=sharing) for a template. The API is currenlty set to mark '1' in the row and column to indicate their attendance. This can be changed easily in the API.
## Use:

You can see a verity of implementations inside app.py. There are currently 2 ways of implementing the attendance tracking:
1. Set up a 'secret' and make them valid and take them away as needed:
  * Before:
	   * ```
        if secret == 1234 or secret == 1234 or secret == 1234 or secret == 1234:
                    # If the secret matches update the row
                    sheet.update_cell(row, 6, "1")
                    ret = "Your attendence has been taken"
                else:
                    ret = "Invalid secret"
       ```
  * After:
  	* ```
      ret = "Invalid secret"
      ```


2. Make the 'secret' expire after a set time using Pythons datetime.
	* ```
    # Assign the correct Lab timings:
      section1 = d.replace(hour=14, minute=50, second=0,  day=14, month=2)
      section2 = d.replace(hour=16, minute=25, second=0,  day=14, month=2)
      section3 = d.replace(hour=9, minute=55, second=0,  day=15, month=2)
      section4 = d.replace(hour=11, minute=0, second=0,  day=15, month=2)

      if (secret == 1234  and d < section1):
          # If the secret matches update the row
          sheet.update_cell(row, 5, "1")
          ret = "Your attendence has been taken"
      elif (secret == 1234 and d < section2):
          # If the secret matches update the row
          sheet.update_cell(row, 5, "1")
          ret = "Your attendence has been taken"
      elif (secret == 1234 and d < section3):
          # If the secret matches update the row
          sheet.update_cell(row, 5, "1")
          ret = "Your attendence has been taken"
      elif (secret == 1234 and d < section4):
          # If the secret matches update the row
          sheet.update_cell(row, 5, "1")
          ret = "Your attendence has been taken"
      else:
          ret = "Invalid secret"
    ```
