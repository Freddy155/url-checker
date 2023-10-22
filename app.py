import requests
import subprocess
from urllib.parse import urlparse

# Get the user's input for the website URL
url = input("Enter the website URL you want to check: ")

# Parse the URL to extract the hostname
parsed_url = urlparse(url)
hostname = parsed_url.netloc

# Define the number of pings
num_pings = 10

# Create a function to check the URL status
def check_url_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Success"
        else:
            return "Error"
    except requests.exceptions.RequestException as e:
        return "Error"

# Perform the pings and store the results
ping_results = []
success_count = 0
error_count = 0

print("Real-time Ping Results:")
for i in range(num_pings):
    response = check_url_status(url)

    # Get the round-trip time using the ping command
    try:
        ping_output = subprocess.check_output(["ping", "-c", "1", hostname], universal_newlines=True)
        lines = ping_output.split('\n')
        if len(lines) > 1:
            time_info = lines[-2].split('=')[1].split()
            if len(time_info) > 1:
                round_trip_time = time_info[1]
            else:
                round_trip_time = "N/A"
        else:
            round_trip_time = "N/A"
    except subprocess.CalledProcessError:
        round_trip_time = "N/A"

    ping_results.append((response, round_trip_time))
    
    # Update success and error counts
    if response == "Success":
        success_count += 1
    else:
        error_count += 1

    # Display the result without "ms"
    print(f"Ping {i + 1}: Result: {response}, RTT: {round_trip_time}")
    
# Calculate and display statistics
success_percentage = (success_count / num_pings) * 100

print("\nPing Statistics:")
print(f"URL: {url}")
print(f"Total Pings: {num_pings}")
print(f"Success Count: {success_count}")
print(f"Error Count: {error_count}")
print(f"Success Percentage: {success_percentage:.2f}%")
