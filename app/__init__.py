from flask import Flask
from .routes import convert_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(convert_bp)

    @app.route('/health')
    def health_check():
        return 'OK', 200

    return app