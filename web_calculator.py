#!/usr/bin/env python3
"""
Web-based Calculator using Python's built-in HTTP server
"""

import http.server
import socketserver
import webbrowser
import threading
import time
from urllib.parse import parse_qs, urlparse
import json

class CalculatorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/calculator':
            self.send_calculator_page()
        elif self.path.startswith('/calculate'):
            self.handle_calculation()
        else:
            super().do_GET()
    
    def send_calculator_page(self):
        """Send the calculator HTML page"""
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .calculator {
            background: #000;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            width: 300px;
        }
        
        .display {
            background: #000;
            color: white;
            font-size: 2.5em;
            text-align: right;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }
        
        .btn {
            border: none;
            border-radius: 50%;
            font-size: 1.5em;
            font-weight: bold;
            height: 60px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .btn:hover {
            transform: scale(1.05);
        }
        
        .btn:active {
            transform: scale(0.95);
        }
        
        .btn-number {
            background: #505050;
            color: white;
        }
        
        .btn-operator {
            background: #FF9500;
            color: white;
        }
        
        .btn-function {
            background: #A6A6A6;
            color: black;
        }
        
        .btn-zero {
            grid-column: span 2;
            border-radius: 30px;
        }
        
        .title {
            text-align: center;
            color: white;
            margin-bottom: 20px;
            font-size: 1.5em;
        }
    </style>
</head>
<body>
    <div>
        <h1 class="title">Web Calculator</h1>
        <p style="text-align: center; color: white; font-size: 0.9em; margin-bottom: 10px;">v1.0.1 - Security Update (setuptools>=78.1.1)</p>
        <div class="calculator">
            <div class="display" id="display">0</div>
            <div class="buttons">
                <button class="btn btn-function" onclick="clearAll()">C</button>
                <button class="btn btn-function" onclick="toggleSign()">±</button>
                <button class="btn btn-function" onclick="percent()">%</button>
                <button class="btn btn-operator" onclick="setOperator('÷')">÷</button>
                
                <button class="btn btn-number" onclick="inputNumber('7')">7</button>
                <button class="btn btn-number" onclick="inputNumber('8')">8</button>
                <button class="btn btn-number" onclick="inputNumber('9')">9</button>
                <button class="btn btn-operator" onclick="setOperator('×')">×</button>
                
                <button class="btn btn-number" onclick="inputNumber('4')">4</button>
                <button class="btn btn-number" onclick="inputNumber('5')">5</button>
                <button class="btn btn-number" onclick="inputNumber('6')">6</button>
                <button class="btn btn-operator" onclick="setOperator('-')">-</button>
                
                <button class="btn btn-number" onclick="inputNumber('1')">1</button>
                <button class="btn btn-number" onclick="inputNumber('2')">2</button>
                <button class="btn btn-number" onclick="inputNumber('3')">3</button>
                <button class="btn btn-operator" onclick="setOperator('+')">+</button>
                
                <button class="btn btn-number btn-zero" onclick="inputNumber('0')">0</button>
                <button class="btn btn-number" onclick="inputDecimal()">.</button>
                <button class="btn btn-operator" onclick="calculate()">=</button>
            </div>
        </div>
    </div>
    
    <script>
        let currentInput = '0';
        let previousInput = '';
        let operator = '';
        let waitingForOperand = false;
        
        function updateDisplay() {
            const display = document.getElementById('display');
            display.textContent = currentInput;
        }
        
        function inputNumber(num) {
            if (waitingForOperand) {
                currentInput = num;
                waitingForOperand = false;
            } else {
                currentInput = currentInput === '0' ? num : currentInput + num;
            }
            updateDisplay();
        }
        
        function inputDecimal() {
            if (waitingForOperand) {
                currentInput = '0.';
                waitingForOperand = false;
            } else if (currentInput.indexOf('.') === -1) {
                currentInput += '.';
            }
            updateDisplay();
        }
        
        function setOperator(nextOperator) {
            const inputValue = parseFloat(currentInput);
            
            if (previousInput === '') {
                previousInput = inputValue;
            } else if (operator) {
                const result = performCalculation();
                currentInput = String(result);
                previousInput = result;
                updateDisplay();
            }
            
            waitingForOperand = true;
            operator = nextOperator;
        }
        
        function calculate() {
            const inputValue = parseFloat(currentInput);
            
            if (previousInput !== '' && operator) {
                const result = performCalculation();
                currentInput = String(result);
                previousInput = '';
                operator = '';
                waitingForOperand = true;
                updateDisplay();
            }
        }
        
        function performCalculation() {
            const prev = parseFloat(previousInput);
            const current = parseFloat(currentInput);
            
            switch (operator) {
                case '+':
                    return prev + current;
                case '-':
                    return prev - current;
                case '×':
                    return prev * current;
                case '÷':
                    if (current === 0) {
                        alert('Cannot divide by zero!');
                        return prev;
                    }
                    return prev / current;
                default:
                    return current;
            }
        }
        
        function clearAll() {
            currentInput = '0';
            previousInput = '';
            operator = '';
            waitingForOperand = false;
            updateDisplay();
        }
        
        function toggleSign() {
            if (currentInput !== '0') {
                currentInput = currentInput.startsWith('-') ? 
                    currentInput.slice(1) : '-' + currentInput;
                updateDisplay();
            }
        }
        
        function percent() {
            currentInput = String(parseFloat(currentInput) / 100);
            updateDisplay();
        }
        
        // Keyboard support
        document.addEventListener('keydown', function(event) {
            const key = event.key;
            
            if ('0123456789'.includes(key)) {
                inputNumber(key);
            } else if (key === '.') {
                inputDecimal();
            } else if (key === '+') {
                setOperator('+');
            } else if (key === '-') {
                setOperator('-');
            } else if (key === '*') {
                setOperator('×');
            } else if (key === '/') {
                event.preventDefault();
                setOperator('÷');
            } else if (key === 'Enter' || key === '=') {
                calculate();
            } else if (key === 'Escape' || key === 'c' || key === 'C') {
                clearAll();
            }
        });
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())
    
    def handle_calculation(self):
        """Handle calculation requests"""
        # This method can be extended for server-side calculations if needed
        pass

def start_server(port=8000, host="0.0.0.0"):
    """Start the web server"""
    with socketserver.TCPServer((host, port), CalculatorHandler) as httpd:
        print(f"Calculator server running at http://{host}:{port}")
        print(f"Access the calculator at http://localhost:{port}")
        print("Press Ctrl+C to stop the server")
        
        # Only open browser if not in container (check for DISPLAY env var)
        import os
        if os.environ.get('DISPLAY') and not os.environ.get('CONTAINER'):
            def open_browser():
                time.sleep(1)
                webbrowser.open(f'http://localhost:{port}')
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.shutdown()

if __name__ == "__main__":
    start_server()

