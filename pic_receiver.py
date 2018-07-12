import os
from flask import Flask
from flask import request
from flask import send_from_directory
import time
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/countme/<input_str>')
def count_me(input_str):
    with open('/home/ubuntu/flaskapp/data/received_string.txt', 'w') as f:
        f.write(input_str + '\n')

    return input_str[::-1]


@app.route("/pic_upload", methods=['POST'])
def upload_pic():
    start_time = time.time()
    upload_file = request.files['file']
    file_name = secure_filename(upload_file.filename)

    if upload_file:
        file_path = os.path.join('/home/ubuntu/flaskapp/data/', file_name)
        upload_file.save(file_path)
        print "success"
        print('file saved to %s' % file_path)
        duration = time.time() - start_time
        print('duration:[%.0fms]' % (duration*1000))
        return 'success'
    else:
        return 'failed'


@app.route("/pic_download/<filename>", methods=['GET'])
def download_pic(filename):
    return send_from_directory('/home/ubuntu/flaskapp/data/', filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
