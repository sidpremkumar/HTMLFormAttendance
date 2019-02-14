# HTML Form Attendance

This framework was created as a way to take attendance for a discussion/lab section of CS 112 at BU. You can learn more about it [here](http://sidpremkumar.com/htmlformattendance.html).

## Set up:
You need to change the following in app.py:

1.
```# Google Sheets API
# TODO: Enter relevent information here:
client_id = ""
client_secret = "" ```

2.
```# TODO: Create your own client secret
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)```

3.
```# TODO: Enter your own workbook name
sheet = client.open("").sheet1````

You need to change the following in attendance.html

1.
```// TODO: Enter API information here (i.e. link of where its hosted '.../takeAttendance')
ret = $.post("", {labnumber:labnumber, secret:secret, username:username}).done(function(data){```

## Use:

You can see a verity of implementations inside app.py. There are currently 2 ways of implementing the attendance tracking:
1. Set up a 'secret' and make them valid and take them away as needed:
*```if (secret == 4892  and d < section1):
          # If the secret matches update the row
          sheet.update_cell(row, 5, "1")```
    After ```


2.
