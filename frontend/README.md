# Diffie-Hellman Frontend

This project provides a frontend interface for the Diffie-Hellman key exchange implementation in Python. It allows users to input their private keys, the agreed generator, and the prime number, and then calculates the shared secret.

## Project Structure

```
diffie-hellman-frontend
├── public
│   └── index.html        # Main HTML document
├── src
│   ├── app.js           # JavaScript code for user interactions
│   └── styles.css       # CSS styles for the application
├── package.json          # npm configuration file
└── README.md             # Project documentation
```

## Getting Started

To set up the project, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd diffie-hellman-frontend
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the application**:
   ```
   npm start
   ```

4. **Open your browser** and navigate to `http://localhost:3000` (or the specified port) to access the application.

## Usage

- Enter Alice's and Bob's private keys.
- Input the agreed generator and prime number.
- Click the button to calculate the shared secret.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.