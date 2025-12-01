# close() → no parameters, destroys the socket.
# shutdown() → takes parameters to half-close the connection.
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

sock.shutdown(socket.SHUT_RD)       # No More Read / half close
sock.shutdown(socket.SHUT_WR)       #No More Write /Half Close
sock.shutdown(socket.SHUT_RDWR)     #Close for read write both
sock.close()                        #Close fully 

