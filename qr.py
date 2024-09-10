import pyzbar.pyzbar as py
import cv2
import numpy
import webbrowser

def scan():
    cap = cv2.VideoCapture(0)
    last_data = None  # this variable is declared to store the last scanned qr code

    while True:
        ret,frame = cap.read()
        
        if not ret:
            print("failed to capture frame")
            break

        decoded = py.decode(frame)
        
        for j in decoded:
            current_data = j.data.decode("utf-8")
            
            if current_data != last_data:  # this is activated if new qr is detected
                print(f"Scanned QR code: {current_data}")
                last_data = current_data  # this updates the last qrcode
                
                # this function opens the scanned qr in web-browser
                webbrowser.open(current_data)
                
                cap.release()  # this releases the camera
                cv2.destroyAllWindows()  # this closes the windows
                return  # this exits the function after scanning the qr code once

        cv2.imshow("qrcode", frame)

        # it waits for 5 ms and checks if the q key is pressed, if q is pressed the loop is exited manually 
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

scan() #calling the function 
