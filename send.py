import socket
import numpy as np
import cv2 as cv


addr = ("127.0.0.1", 65534)
buf = 512
width = 640
height = 480
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
code = 'start'
code = ('start' + (buf - len(code)) * 'a').encode('utf-8')


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            s.sendto(code, addr)
            data = frame.tostring()
            for i in range(0, len(data), buf):
                s.sendto(data[i:i+buf], addr)
            # cv.imshow('send', frame)
            # if cv.waitKey(1) & 0xFF == ord('q'):
                # break
        else:
            break
    # s.close()
    # cap.release()
    # cv.destroyAllWindows()
