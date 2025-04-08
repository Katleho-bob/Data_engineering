Here's a README for your Flask app with Docker Compose configuration:

---

# Time Difference API

This is a Flask-based API that calculates the time difference between pairs of timestamps, returning the absolute difference in seconds. The app supports multiple instances using Docker Compose, where each instance runs with a unique `NODE_ID`.

## Features

- Calculate the absolute difference between pairs of timestamps.
- Support for multiple timestamp pairs in a single request.
- The API response includes a unique `NODE_ID` for each instance.
- Runs as a multi-instance Flask app with Docker Compose.

## Requirements

- Python 3.x
- Flask
- pytz (for timezone support)
- Docker & Docker Compose

## Installation

### 1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

- Install Flask and pytz:
```bash
pip install Flask pytz
```

### 3. Docker Setup

#### Build and run the application using Docker Compose:
```bash
docker-compose up --build
```

This will build the Docker images and start the application on two separate services (`app1` and `app2`), each exposed on different ports (`5001` and `5002`).

### 4. Access the Application
The app will be accessible at:

- `http://localhost:5001` for `app1`
- `http://localhost:5002` for `app2`

## Usage

### API Endpoint

- **POST /time_diff**

    The endpoint accepts a JSON request body that contains an array of timestamp pairs. It returns the absolute difference in seconds between each pair of timestamps, along with the `NODE_ID` of the service that processed the request.

### Request Example

**POST** to `http://localhost:5001/time_diff` (or `5002` for the second instance) with the following JSON body:

```json
{
  "timestamps": [
    ["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"],
    ["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
  ]
}
```

### Response Example

```json
{
  "id": "1",
  "result": [25200, 88200]
}
```

- The `id` field corresponds to the `NODE_ID` for the instance handling the request.
- The `result` field contains the list of time differences (in seconds) for each timestamp pair.

### Error Handling

If the timestamps are not in the correct format or if there is an issue processing the request, the API will return a `400` status with an error message.

### Sample Error Response

```json
{
  "error": "Invalid timestamp format"
}
```

## Functions

- **`time_difference_in_seconds(t1, t2)`**: Calculates the absolute difference in seconds between two timestamps using the format `%a %d %b %Y %H:%M:%S %z`.

## Docker Compose Configuration

This app uses Docker Compose to run two instances of the Flask app (`app1` and `app2`) on different ports. The `NODE_ID` is assigned as an environment variable to each service, and it's included in the response to identify the service that processed the request.

### docker-compose.yml

```yaml
version: '3.8'

services:
  app1:
    build: .
    environment:
      - NODE_ID=1
    ports:
      - "5001:5000"
  app2:
    build: .
    environment:
      - NODE_ID=2
    ports:
      - "5002:5000"
```

- **`app1`** runs on port `5001` and has `NODE_ID=1`.
- **`app2`** runs on port `5002` and has `NODE_ID=2`.

### Running Multiple Instances

You can scale the number of instances by adjusting the `docker-compose.yml` file and using the following command:

```bash
docker-compose up --scale app1=3 --scale app2=2
```

This will start three instances of `app1` and two instances of `app2`, each handling requests independently.

