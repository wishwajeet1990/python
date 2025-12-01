"socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)"


"""
Family :- 

socket.AF_INET → IPv4 (host, port) e.g. ('127.0.0.1', 8080)
socket.AF_INET6 → IPv6 (host, port, flowinfo, scopeid)
socket.AF_UNIX → Unix Domain Sockets (file path, only on Linux/Unix)
socket.AF_BLUETOOTH, AF_CAN, etc. → for special protocols

"""
"""

type

socket.SOCK_STREAM → TCP (connection-oriented, reliable)
socket.SOCK_DGRAM → UDP (connectionless, faster, no reliability)
socket.SOCK_RAW → Raw sockets (low-level access, needs root/admin)
socket.SOCK_SEQPACKET → Sequential packets, reliable but message-oriented

"""

""" 
proto = protocol

Usually 0 (default) → let system decide.
Rarely used directly (e.g., multiple protocols under SOCK_RAW).

"""
"""
fileno

Used to create a socket object from an existing file descriptor.
Normally None (new socket created).
Rare case: when you want to wrap an existing socket.

"""