TCP

How to establish a TCP connection?Edit

When computer A wants to connect to computer B via TCP, the following path is followed:

    Computer A sends a TCP SYN chronize message to computer B
    Computer B sends a TCP SYN + ACK nowledgment message that it has received computer A's request
    Computer A sends TCP ACK message to computer B
    Computer B receives an ACK "TCP connection is ESTABLISHED "

As a result of this method, called the three-time handshake , the TCP connection is opened.

It helps to find the delta of the elapsed time by calculating the epoch time of the talk time only between the psh-ack True and ack True ones.

CP is a connection-based protocol, two computers start to exchange data after performing a triple handshake (3-way handshake)
The given data is processed with incoming psh-ack after 3-way handshake
