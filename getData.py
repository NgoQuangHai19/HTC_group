class RS485:

    def __init__(self, portName):
        self.ser = serial.Serial(port=portName, baudrate=9600)

    def readData(self):
        bytesToRead = self.ser.inWaiting()
        if bytesToRead > 0:
            out = self.ser.read(bytesToRead)
            data_array = [b for b in out]
            if len(data_array) >= 7:
                array_size = len(data_array)
                value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
                return value
            else:
                return -1
        return 0

    def writeData(self, data):
        self.ser.write(data)


class AdafruitIO:

    def __init__(self, AIO_USERNAME, AIO_KEY):
        self.client = MQTTClient(AIO_USERNAME, AIO_KEY)
        self.client.on_connect = self.connected
        self.client.on_message = self.message
        self.client.on_disconnect = self.disconnected
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()

    def connected(self):
        print("E ket noi thanh cong Adafruit roi do ...")
        self.client.subscribe(AIO_FEED_ID)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Sub Successful ...")

    def disconnected(self, client):
        print("DISCONECT ...")
        sys.exit(1)

    def message(self, client, feed_id, payload):
        print("Data come")
        print("Turn relay 1:" + payload)
        if feed_id == AIO_FEED_ID[3]:
            print("Data Temp :" + payload)

    def publish(self, feed_id, payload):
        self.client.publish(feed_id, payload)