# python-port-scanner

## Python Port Scanner

### Introduction

This project is my ****first self-built cybersecurity tool****.

The goal of this project is to strengthen and deepen my understanding of ****Python programming, networking concepts, and practical security tooling****.

I created this tool to ****apply my theoretical knowledge in a practical way**** and to improve my ability to build real-world security-related scripts from scratch.

This project is part of my learning journey in cybersecurity and penetration testing.

### Project Goal

The objective of this project was to build a ****basic TCP port scanner in Python**** that can:

- accept a target IP address or hostname
- resolve hostnames to IP addresses
- scan a user-defined port range
- detect open ports
- display common service names
- validate user input
- present results clearly in the terminal

The main purpose was to ****translate learned concepts into a working tool**** and strengthen my technical understanding through implementation.

- --

### Why I Built This Project

This is the ****first custom tool I have developed on my own**** as part of my cybersecurity learning path.

I built this project to:

- deepen my Python knowledge
- improve my understanding of sockets and TCP connections
- practice writing structured and modular code
- apply cybersecurity concepts in a hands-on way
- strengthen problem-solving and debugging skills

This project helped me move from learning theory to building a real functional tool.

### Features

- target IP / hostname input
- hostname resolution
- custom port range scanning
- TCP open port detection
- common service name resolution
- input validation
- error handling
- clear terminal output

### Technologies Used

- Python
- Visual Studio Code
- Terminal / CLI
- Python `socket` module
- --

### Project Structure

python-port-scanner/

├──main.py

└── README.md

### Development Process

### Step 1: Project Setup

Created the initial project structure and verified that Python runs correctly.

### Key Code

```python
def main():
		print("Python Port Scanner Project Started")
```

### Step 2: User Input

Added user input for the target IP address.

### Key Code

```python
target = input("Enter target IP address: ")
```

### Step 3: Single Port Scanning

Implemented the first socket-based TCP port scan.

### Key Code

```python
result = sock.connect_ex((target,port))
return result == 0
```

This step introduced the core scanning logic by checking whether a specific port is open.

### Step 4: Multiple Port Scanning

Extended the scanner to scan multiple ports using a loop.

### Key Code

```python
for port in range(1,101):
		scan_port(target, port)
```

This allowed automated scanning of multiple ports.

### Step 5: Result Management

Introduced structured result storage using a list.

### Key Code

```python
open_ports.append(port)
```

This improved the output structure and readability.

### Step 6: Hostname Resolution

Added hostname support and automatic IP resolution.

### Key Code

```python
resolved_target = socket.gethostbyname(user_target)
```

This allows scanning both IP addresses and hostnames.

### Step 7: Custom Port Range

Added dynamic user-defined port range input.

Key Code

```python
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
```

This significantly improved tool flexibility.

### Step 8: Service Name Detection

Added detection of common service names for open ports.

### Key Code

```python
service_name = socket.getservbyport(port)
```

This provides additional context for detected open ports.

Example:

- 22 → ssh
- 80 → http
- 443 → https

### Step 9: Input Validation

Implemented input validation for invalid ports and ranges.

### Key Code

```python
if start_port < 1 or end_port > 65535:
```

```python
if start_port > end_port:
```

This improved reliability and robustness.

### Step 10: Finalization

Reviewed, cleaned, and finalized the project structure and documentation.

**## How to Run**

Run the script from the terminal:

python main.py

Example:

Enter target IP address or hostname: localhost

Enter start port: 1

Enter end port: 100

## Learning Outcome**

#### This project significantly improved my understanding of:

- Python functions
- exception handling
- modular code structure
- socket programming
- TCP communication
- port scanning logic
- user input validation

Most importantly, it helped me apply my knowledge in practice and build my first real cybersecurity tool.

## ## Future Improvements

#### Possible future upgrades include:

- multithreaded scanning
- faster scan performance
- UDP scanning
- banner grabbing
- export results to file
- scanning multiple targets

## ## Final Note

This project represents an important milestone in my cybersecurity learning journey as it is the first practical security tool I developed myself.

It reflects my effort to continuously improve my technical skills and convert learned knowledge into hands-on implementation.
