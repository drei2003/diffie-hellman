from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Compute public key
def calculatePublicKey(privateKey, agreedG, agreedPrimeNumber):
    return (agreedG ** privateKey) % agreedPrimeNumber

# Compute shared secret
def calculateSharedSecret(publicKey, privateKey, agreedPrimeNumber):
    return (publicKey ** privateKey) % agreedPrimeNumber

# Create HTTP Server
class RequestHandler(BaseHTTPRequestHandler):
    def send_cors_headers(self):
        # Set the necessary CORS headers
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow all origins
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")  # Allow POST, GET, OPTIONS methods
        self.send_header("Access-Control-Allow-Headers", "Content-Type")  # Allow Content-Type header

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_cors_headers()  # Add CORS headers
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())

    def do_POST(self):
        if self.path == "/compute":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(post_data)

            # Extract form values
            alicePrivateKey = int(data["alicePrivateKey"])
            bobPrivateKey = int(data["bobPrivateKey"])
            agreedG = int(data["agreedG"])
            agreedPrimeNumber = int(data["agreedPrimeNumber"])

            # Validate prime number
            if agreedG >= agreedPrimeNumber or not is_prime(agreedPrimeNumber):
                response = {"message": "Invalid Prime Number (P must be prime and greater than G)"}
            else:
                # Calculate keys and shared secrets
                alicePublicKey = calculatePublicKey(alicePrivateKey, agreedG, agreedPrimeNumber)
                bobPublicKey = calculatePublicKey(bobPrivateKey, agreedG, agreedPrimeNumber)
                aliceSharedSecret = calculateSharedSecret(bobPublicKey, alicePrivateKey, agreedPrimeNumber)
                bobSharedSecret = calculateSharedSecret(alicePublicKey, bobPrivateKey, agreedPrimeNumber)

                if aliceSharedSecret == bobSharedSecret:
                    response = {
                        "sharedSecret": aliceSharedSecret,
                        "alicePrivateKey": alicePrivateKey,
                        "bobPrivateKey": bobPrivateKey,
                        "alicePublicKey": alicePublicKey,
                        "bobPublicKey": bobPublicKey
                        }
                else:
                    response = {"message" : "Shared secret mismatch!"}

            # Send JSON response
            self.send_response(200)
            self.send_cors_headers()  # Add CORS headers
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_OPTIONS(self):
        # Handle the OPTIONS request for CORS preflight
        self.send_response(200)
        self.send_cors_headers()  # Add CORS headers
        self.end_headers()

# Run server
PORT = 8080
server = HTTPServer(("localhost", PORT), RequestHandler)
print(f"Server running at http://localhost:{PORT}")
server.serve_forever()
