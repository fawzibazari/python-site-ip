
import socket

website = input('Enter the name of any domain')
print(f"\nYou Entered: {website}")
print(f"\n The IP adress of {website} is {socket.gethostbyname(website)}")