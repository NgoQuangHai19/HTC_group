input = ["0C0600050001"]
def modbusCrc(msg:str) -> int:
    crc = 0xFFFF
    for n in range(len(msg)):
        crc ^= msg[n]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

for turn in input:
    c2 = [int(turn[i:i + 2], 16) for i in range(0, len(turn), 2)]
    msg = bytes.fromhex(turn)
    crc = modbusCrc(msg)
    #print("0x%16X"%(crc))
    ba = crc.to_bytes(2, byteorder='little')
    c2.append(ba[0])
    c2.append(ba[1])

    #Result
    #print(turn)
    print(c2)
    print()
    #print("[%02X,%02X]"%(ba[0], ba[1]))