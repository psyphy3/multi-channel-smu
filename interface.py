import sys
import zmq

def func(msg):
    ip="169.254.183.6"
    port="5555"
    context=zmq.Context()
    sock=zmq.Socket(context,zmq.REQ)
    sock.connect("tcp://"+ip+":"+port)

    sock.send(msg.encode('utf-8'))
    out=sock.recv()
    print(out)

if __name__ == '__main__':
    a = sys.argv[1]
    func(a)