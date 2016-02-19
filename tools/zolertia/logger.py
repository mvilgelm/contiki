import datetime
import serial
import sys

def get_mote_serial(dev_number):
    '''
    returns a serial handler for the usb device with a given number
    '''
    return serial.Serial("/dev/ttyUSB%s" % dev_number, timeout=None, baudrate=115200)

def log_serial(ser, out_file):
    '''
    logs reading from the serial handler into the output file,
    together with the timestampt for every line
    '''
    f = open(out_file, "w")

    try:
        while True:
            line = ser.readline()
            #print(str(datetime.datetime.now().time())+'\t'+line.decode("utf-8").split('\n')[0])
            f.write(str(datetime.datetime.now().time())+'\t'+line.decode("utf-8").split('\n')[0]+'\n')
    except KeyboardInterrupt:
        print('--- cleaning up')
        f.close()
        raise




if __name__=='__main__':

    if len(sys.argv)!=3:
        print("Usage: %s DEVICE_NUMBER OUTPUT_FILE" % sys.argv[0])
        exit()

    dev_num = sys.argv[1]
    out_file = sys.argv[2]

    ser = get_mote_serial(dev_num)

    log_serial(ser, out_file)