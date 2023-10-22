# URL Checker

This Python script checks the status of a website by sending HTTP requests and pinging the website to measure round-trip times. It provides real-time ping results and statistics.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Prerequisites

Before using the URL Checker, you need to ensure you have the following installed:
- Python (3.6 or higher)
- Requests library (can be installed using `pip install requests`)

## Usage

1. Clone this repository:
```bash
git clone https://github.com/Freddy155/url-checker.git
```


2. Change into the project directory:
```bash
cd url-checker
```

3. Run the script
```bash
python app.py
```


4. You'll be prompted to enter the website URL you want to check. Simply input the URL, and the script will perform real-time pings and display the results and statistics.

## Features

- Real-time ping results: The script pings the specified website and provides feedback on whether the website is responding successfully or with errors.
- Round-trip time (RTT): The script measures and displays the round-trip time for each ping.
- Statistics: At the end of the pings, the script displays statistics, including the total number of pings, the count of successful pings, the count of error pings, and the success percentage.

