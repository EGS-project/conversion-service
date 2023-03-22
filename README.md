# install dotenv
```
pip install -r requirements.txt
```

# run template 
```
python3 main.py
```

# .env
Create this file
```
# !!!THIS FILE MUST NOT BE EVER COMMITED!!!
# !!!   MUST BE PRESENT IN .gitignore   !!!

# AUTH VARIABLES
AUTH_CLIENT_ID=MY_CLIENT_ID
AUTH_CLIENT_SECRET=S&$GWCRET

# DATABASE VARIABLES
DATABASE_URL=my_database_url
DATABASE_PORT=6243

# APP VARIABLES
APP_SECRET_KEY=d5444d7a3f6e1bafdf96575
```

### notes
serializing and deserializing- create class to interpret image pre and post sending

possible content needed for image manipulation:
optimize flag
new resolution values: width and height
flag for AA usage
quality in %

conversion service input comes from a message:

in order to create the Image object on the receiver side, only the base64 image data is required, file name and metadata is optional
meaning any service that handles the reception of images only needs to MANDATORILY retrieve the image data and nothing else

meaning that the b64_string field is the only one that will not have a default value
maybe implementing a flag that specifies if any manipulation is to be made regarding the resolution, compression, aliasing
    this would allow for theoretically simpler decisions regarding the processing of an xml message

stomp queue connection functions need to be studied - IMPORTANT
