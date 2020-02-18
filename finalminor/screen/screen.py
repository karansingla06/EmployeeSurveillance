import pyscreenshot
import flask
from StringIO import StringIO
 
app = flask.Flask(__name__)
 
@app.route('/screen.png')
def serve_pil_image():
    img_io = StringIO()
    pyscreenshot.grab().save(img_io, 'PNG', quality=50)
    img_io.seek(0)
    return flask.send_file(img_io, mimetype='image/png')
 
@app.route('/')
def serve_img():
    return flask.render_template('screen.html')
 
if __name__ == "__main__":
    app.run(host= '192.168.43.150', debug=True,port=8080)
