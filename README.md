# Simple_SSE_Server
# Bitcoin Price Tracker

This is a simple Flask-based web application that streams real-time Bitcoin prices using Server-Sent Events (SSE). The app fetches the current Bitcoin price in USD from the [CoinGecko API](https://www.coingecko.com/en/api) every 60 seconds and displays it on a webpage with a timestamp.

The application is containerized using Docker, making it easy to deploy and run.

## Features
- **Real-Time Updates**: Streams Bitcoin price updates every minute using SSE.
- **Simple Web Interface**: Displays the current price and last update timestamp.
- **Docker Support**: Packaged in a lightweight Docker container for easy deployment.
- **Error Handling**: Gracefully handles API failures.

## Prerequisites
- **Docker**: Ensure Docker is installed on your system ([Install Docker](https://docs.docker.com/get-docker/)).
- **Git**: To clone the repository ([Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)).
- Internet access to fetch Bitcoin prices from the CoinGecko API.

## Installation and Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/AbdullrahmanGad/Simple_SSE_Server.git
cd Simple_SSE_Server
```

### 2. Build the Docker Image
Build the Docker image using the provided `Dockerfile`:
```bash
docker build -t bitcoin-price-tracker .
```

### 3. Run the Docker Container
Run the container, mapping port 5000 on your host to port 5000 in the container:
```bash
docker run -p 5000:5000 bitcoin-price-tracker
```

### 4. Access the Application
Open your browser and navigate to:
```
http://localhost:5000
```
You should see the Bitcoin Price Tracker webpage displaying the current Bitcoin price and the last update timestamp.

## Project Structure
```
Simple_SSE_Server/
├── Dockerfile        # Docker configuration for the app
├── SSE.py            # Main Flask application (may be named app.py)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

**Note**: If the main application file is `app.py` instead of `SSE.py`, the `Dockerfile` is already configured for `app.py`. If using `SSE.py`, update the `Dockerfile` to:
```dockerfile
COPY SSE.py .
CMD ["python", "SSE.py"]
```

## Dependencies
The app uses the following Python packages (listed in `requirements.txt`):
- `Flask==2.0.1`: Web framework for the server and SSE.
- `requests==2.26.0`: For making HTTP requests to the CoinGecko API.
- `werkzeug==2.0.3`: Compatible version for Flask.

## How It Works
- The Flask app exposes two endpoints:
  - `/`: Serves an HTML page with JavaScript to display Bitcoin prices.
  - `/bitcoin-price-stream`: Streams price updates via SSE every 60 seconds.
- The app queries the CoinGecko API (`https://api.coingecko.com/api/v3/simple/price`) for the current Bitcoin price in USD.
- The webpage uses an `EventSource` to listen for SSE updates and displays the price and timestamp.

## Troubleshooting
- **App not loading**: Ensure the Docker container is running and port 5000 is not blocked. Check container logs:
  ```bash
  docker logs <container_id>
  ```
- **API errors**: Verify internet connectivity, as the app requires access to the CoinGecko API.
- **File name mismatch**: If the app fails to start, confirm whether the main file is `SSE.py` or `app.py` and update the `Dockerfile` accordingly.
- **Dependency issues**: Ensure all dependencies in `requirements.txt` are installed correctly during the Docker build.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [CoinGecko API](https://www.coingecko.com/en/api) for providing free Bitcoin price data.
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework.
