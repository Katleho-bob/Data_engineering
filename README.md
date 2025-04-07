# Data_engineering
# Time Difference API

This project is a simple web service that calculates the absolute difference in seconds between two timestamps, considering time zones.

## Prerequisites

- Python 3.6 or higher
- Flask (for the web service)
- Docker (for containerizing the app)
- Postman (for testing the API)
- Docker Compose (if you want to use multi-container setups)

## Setup

### Step 1: Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/Katleho-bob/Data_engineering.git

 
### For Testing
curl --location 'http://localhost:5001/time_diff' \
--header 'Content-Type: application/json' \
--data '{
  "timestamps": [
    ["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"],
    ["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
  ]
}
