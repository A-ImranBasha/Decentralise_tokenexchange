import socket
from Crypto.PublicKey import RSA
import hashlib
host,port = "127.0.0.1",1234
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
      s.connect((host,port))
      data = "Hello World".encode('utf-8')
      keyPair = RSA.generate(1024)
      hash = int.from_bytes(hashlib.sha512(data).digest(),byteorder='big')
      signature = pow(hash,keyPair.d,keyPair.n)
      msg_to_send = data + b"||" + str(signature).encode('utf-8')
      with open("public_key.txt","w") as f:
           f.write(f"{keyPair.e} {keyPair.n}")
           s.sendall(msg_to_send)
