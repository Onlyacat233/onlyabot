import socket as sk

def connect(addr, msg: str):
    try:

        sk.setdefaulttimeout(3)
        socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        socket.connect(addr)
        socket.send(msg.encode("utf-8"))
        resp = socket.recv(1024).decode("u8")
        socket.close()
        return resp
    except sk.timeout:
        return "error"