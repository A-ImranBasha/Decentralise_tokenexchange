import socket
import hashlib
host,port = "127.0.0.1",1234
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
          s.bind((host,port))
          s.listen(5)
          conn,addr = s.accept()
          data = conn.recv(1024)
          msg,signature = data.split(b"||")
          with open("public_key.txt","r") as f:
                  read = f.read()
                  e,d = read.split(" ")
                  f.close()
          signature = signature.decode('utf-8')
          decrypt_sign = pow(int(signature),int(e),int(d))
          msg_hash =int.from_bytes(hashlib.sha512(msg).digest(),byteorder='big')
if msg_hash == decrypt_sign:
      print("Digital Signature successfully verified")
else:
        print("Digital Signature not verified successfully")
