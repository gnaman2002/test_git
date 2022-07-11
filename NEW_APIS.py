from flask import Flask, request, Response
from flask import send_file
from PIL import Image
import numpy as np
import os
app = Flask(__name__)


@app.route('/licenseplateblur')  # Single Api
def LP():
    print ("Welcome to License Plate Detection")
    resp = Response(status=200, content_type='application/json')

    image = request.files['file']  # Single image path

    try:

        if request.content_type != None:
            if request.content_type.startswith('multipart/form-data'):
                if 'file' in request.files.keys():
                    if (image.filename.endswith('.jpg')):
                        # results = model.detect_licenseplates(image)
                        # img=io.imread(image)
                        img = Image.open(image)
                        # img = np.asarray(img)
                        # print('image-array', img)
                        img.save("result_bw.jpg")

                        return send_file('/home/ceinfo/PycharmProjects/pythonProject6/result_bw.jpg', mimetype='image/gif')
                    else:
                        resp.status_code = 400
                        return resp
                else:
                    resp.status_code = 400
                    return resp
            else:
                resp.status_code = 400
                return resp
        else:
            resp.status_code = 400
            return resp
    except Exception as e:
        # logger.error(msg=str(e), status_code=500)
        resp.status_code = 500
        return resp
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=False)
