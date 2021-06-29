import serial,atexit,sys
global line
global x
print 'hola'
#ser.write('p');
#ser.write('\n');
#target = open("test.csv", 'w')
def exit_handler():
    print 'Closing the file(exit handler)'
    target.close()
    ser.close()
def main(threadname,q):
    ser = serial.Serial('COM15', 38400, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
    ser.flushInput()
    ser.flushOutput()
    #atexit.register(exit_handler)
    while True:
        line = ser.readline()
        if q!=0:
            q.put(line)
        
        #target.write(data_raw)
        #target.write(";\n")
        #print(line)
        #if 'OK' in data_raw:
        #print 'Closing the file'
        #target.close()
        #ser.close()
        #sys.exit(0)
if __name__ == '__main__':
    main('nothread',0)