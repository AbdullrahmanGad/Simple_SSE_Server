import time  # For time-related functions (sleep, timestamps)
import json  # For encoding data as JSON
import requests  # For making HTTP requests to external APIs
from flask import Flask, Response  # For creating a web server and streaming responses
import os

app = Flask(__name__)

# Function to fetch the current Bitcoin price from CoinGecko API
def get_bitcoin_price():
    """Fetch the current Bitcoin price from CoinGecko API"""
    try:
        # Make a GET request to the CoinGecko API for Bitcoin price in USD
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        data = response.json()  # Parse the JSON response
        return data['bitcoin']['usd']  # Return the price in USD
    except Exception as e:
        # Print error if fetching fails
        print(f"Error fetching Bitcoin price: {e}")
        return None

# Define a route for Server-Sent Events (SSE) to stream Bitcoin price updates
@app.route('/bitcoin-price-stream')
def bitcoin_price_stream():
    def event_stream():
        while True:
            # Get the current Bitcoin price
            price = get_bitcoin_price()
            
            if price:
                # Format the data as a JSON string with price and timestamp
                data = json.dumps({"price": price, "timestamp": time.time()})
                # Yield the data in SSE format
                yield f"data: {data}\n\n"
            
            # Wait for 1 minute (60 seconds) before the next update
            time.sleep(60)
    
    # Return a streaming response with the correct MIME type for SSE
    return Response(event_stream(), mimetype="text/event-stream")

# Define the root route to serve the HTML page
@app.route('/')
def index():
    """Serve a simple HTML page that connects to the SSE endpoint"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bitcoin Price Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            #price { font-size: 2em; font-weight: bold; }
            #timestamp { color: gray; font-size: 0.8em; }
        </style>
    </head>
    <body>
        <h1>Bitcoin Price Tracker</h1>
        <div id="price">Loading...</div>
        <div id="timestamp"></div>
        
        <script>
            // Create an EventSource to connect to the SSE endpoint
            const evtSource = new EventSource('/bitcoin-price-stream');
            
            // When a message is received, update the price and timestamp
            evtSource.onmessage = function(event) {
                const data = JSON.parse(event.data);
                document.getElementById('price').textContent = '$' + data.price.toLocaleString();
                
                const date = new Date(data.timestamp * 1000);
                document.getElementById('timestamp').textContent = 'Last updated: ' + date.toLocaleString();
            };
            
            // Handle connection errors
            evtSource.onerror = function() {
                document.getElementById('price').textContent = 'Error connecting to server';
                evtSource.close();
            };
        </script>
    </body>
    </html>
    """

# Run the Flask app in debug mode if this script is executed directly
if __name__ == '__main__':
    import os
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    

