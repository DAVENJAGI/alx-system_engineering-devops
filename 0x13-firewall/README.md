This is a directory containing files about firewall.
*We are using the UFW, uncomplicated firewall, to configure our servers

Task 1
=======
In the file 0-block_all_incoming_traffic_but, we are blocking all other connections but the port 22(SSH), a port that allows for the communication and logging in using the SSH protocol, port443(HTTPS SSL), that allows HyperText Transfer Protocol and Secure Socket Layer, and port 80(HTTP), ie, HyperText Transfer Protocol, ie, unsecure one.

* NB, port 22 should always be open for connection or else you wont be able to log in to your server once you log out.
