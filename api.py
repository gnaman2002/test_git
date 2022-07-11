# import traceback
from flask import Flask, send_file

from PIL import Image


app = Flask(__name__)





col = Image.open("/home/ceinfo/PycharmProjects/pythonProject6/archive1/images/train/disgust/299.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
bw.save("result_bw.png")




@app.route('/licenseplateblur')  # Single Api
def LP():

    return send_file('/home/ceinfo/PycharmProjects/pythonProject6/result_bw.png', mimetype='image/jpg')



if __name__ == '__main__':
    app.run()