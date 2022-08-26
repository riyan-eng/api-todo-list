from app import app
import os

if app.config['ENV'] == 'production':
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer((os.environ.get('FLASK_RUN_HOST'), int(os.environ.get('FLASK_RUN_PORT'))), app)
    http_server.serve_forever()
