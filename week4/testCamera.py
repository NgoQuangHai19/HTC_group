import cv2
import numpy as np
import requests

def display_camera(ip, port):
    # Tạo URL để truy cập video từ camera
    url = "http://" + ip + ":" + str(port) + "/video"

    # Mở kết nối đến camera thông qua URL
    stream = requests.get(url, stream=True)

    # Đọc dữ liệu video từ camera
    bytes_data = bytes()
    for chunk in stream.iter_content(chunk_size=1024):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')
        b = bytes_data.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]
            # Hiển thị video từ dữ liệu nhận được
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Đóng kết nối và giải phóng tài nguyên
    stream.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Nhập IP và cổng của camera thứ nhất
    ip1 = "10.128.54.58"
    port = 4747

    # Nhập IP và cổng của camera thứ hai
    ip2 = "10.128.91.182"  

    while True:
        print("Nhập số 1 để hiển thị camera thứ nhất.")
        print("Nhập số 2 để hiển thị camera thứ hai.")
        print("Nhập 'q' để thoát.")
        choice = input("Nhập lựa chọn: ")

        if choice == '1':
            display_camera(ip1, port)
        elif choice == '2':
            display_camera(ip2, port)
        elif choice.lower() == 'q':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
