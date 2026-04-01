# Import the socket module (used for network connections)
import socket


# This function checks if a specific port is open on the target IP address
def scan_port(target_ip, port):
    # Create a new socket object using IPv4 and TCP
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # Set a timeout (so it doesn't wait forever)
    sock.settimeout(1)  # Set a timeout of 1 second for the connection attempt

    try: 
    
        # Attempt to connect to the target and port
        result = sock.connect_ex((target_ip, port))
    
        # If result is 0, the port is open.
        if result == 0:
            return True 
        else:
            return False 
        
    
    # Handle possible socket errors (like connection issues)
    except socket.error as e:
        print(f"Error scanning port {port} on {target_ip}: {e}")
        return False 
    
    finally:
        # Ensure the socket is always closed after the attempt.
        sock.close()

# Check whether any open ports were found
def get_service_name(port):
    try:
        # Function to resolve a common service name for a port
        return socket.getservbyport(port)
    except OSError:
        # Try to get the service name for the given port
        return "Unknown Service"


# This function is the main entry point of our program
def start_program():
    # Ask the user to enter a target IP address
    target_ip = input("Enter the target IP address: ")

    try:
        # Resolve the user input to an IP address
        resolved_target = socket.gethostbyname(target_ip)
    except socket.gaierror:
        print(f"Error:Unable to resolve {target_ip}. ")
        return
    try:
        #define start and end ports to scan
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
    except ValueError:
        print("Error: Please enter valid port numbers.")
        return
    # Create an empty list to store open ports
    
    # Validate the port numbers (must be between 1 and 65535, and start_port must be less than or equal to end_port)
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: Please enter valid port numbers (1-65535) and ensure the starting port is less than or equal to the ending port.")
        return
    # Return a fallback name if the service is unknown
    if start_port > end_port:
        print("Error: Starting port must be less than or equal to ending port.")
        return
    
    open_ports = []
    
    print(f"\n Target: {target_ip}")
    print(f"Resolved target IP: {resolved_target}")
    print (f"\nScanning {target_ip} from port  {start_port} to {end_port}...\n")

    # Loop through the selected port range
    for port in range(start_port, end_port + 1):
        # Check whether the current port is open
        if scan_port(resolved_target, port):
            # Save the open port in the list
            open_ports.append(port)
    
    # Save the open port in the list
    print("Scan finished.\n")
    
    # Check whether any open ports were found

    if open_ports:
        print("open ports found:")
        for port in open_ports:
            print(f"Port {port} is open.")
    else:
        print("no open ports found")
    
    # run scan
    scan_port(target_ip, port)


# This condition checks if the script is being run directly
# (not imported as a module in another script)
if __name__ == "__main__":
    # Call the main function to start the program
    start_program()


