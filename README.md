# Port-Scaner
This project is a basic Port Scanner written in Python using the socket library. It allows the user to check whether common network ports on a target machine are open or closed.
Simple Python Port Scanner:--
--------------------------------

This project is a basic Port Scanner written in Python using the socket
library.
It allows the user to check whether common network ports on a target
machine are open or closed.

Features:--
------------

-   Scans common ports like 21, 22, 23, 25, 53, 80, 110, 443
-   Uses TCP connection attempts to detect port status
-   Simple and beginner-friendly code
-   Timeout mechanism to avoid long delays

How It Works:--
----------------

1.  The user enters the target IP address.
2.  The program loops through a predefined list of common ports.
3.  For each port, it attempts a connection using socket.connect_ex().
4.  If the result is 0, the port is OPEN; otherwise, it is CLOSED.

How to Run:--
-------------

1.  Install Python on your system (if not already installed).
2.  Save the Python file as port_scanner.py.
3.  Open your terminal or command prompt.
4.  Navigate to the folder containing the file.
5.  Run the script using:

    python port_scanner.py

Example Output:--
-----------------

    Enter the target IP address: 192.168.1.1

    Scanning ports on 192.168.1.1...

    Port 21 is CLOSED
    Port 22 is OPEN
    Port 23 is CLOSED
    Port 25 is CLOSED
    Port 53 is OPEN
    Port 80 is OPEN
    Port 110 is CLOSED
    Port 443 is OPEN

    Scan complete.


