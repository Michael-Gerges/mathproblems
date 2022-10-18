
import pyautogui, cv2
import numpy as np
from flask import render_template, flash, redirect, url_for, Response

from flask import Flask
app = Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        #img = pyautogui.screenshot()
        #frame = np.array(img)
        ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

#def gen_frames():  
#    camera = cv2.VideoCapture(0)
#    while True:
#        success, frame = camera.read()  # read the camera frame
#        
#        if not success:
#            break
#        else:
#            ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
#            frame = buffer.tobytes()
#            yield (b'--frame\r\n'
#                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
#




@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')







'''
<form action = "uploader" method = "POST" enctype = "multipart/form-data">  # 	No characters are encoded. This value is required when you are using forms that have a file upload control
<input name=file type="file">
<input type="submit" value="Submit">
</form>
'''

def camonscreen():
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        cv2.imshow("img", img)   
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()


def screen_recording():
    SCREEN_SIZE = pyautogui.size()[0], pyautogui.size()[1]
    #fourcc = cv2.VideoWriter_fourcc(*"XVID")
    #out = cv2.VideoWriter(r"desktop\output_screen1901080.avi", fourcc, 20.0, (SCREEN_SIZE))
    #starting = (datetime.datetime.now().second)
    while True: # or for i in range(200):
        img = pyautogui.screenshot()
        frame = np.array(img)
    #    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #    out.write(frame)
        cv2.imshow("img", frame) 
    #    ending = (datetime.datetime.now().second)
    #    if ending - starting > 9:  ### get 10 seconds 
    #       break
        if cv2.waitKey(1) == ord("q"):
            break



@app.route('/')
def index():
     return render_template('camera.html')


if __name__ == '__main__':
   app.run(host='192.168.1.179',port=80, debug=True)
   pass