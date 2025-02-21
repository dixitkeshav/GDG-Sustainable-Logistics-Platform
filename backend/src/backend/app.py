from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from routes.auth import auth_bp 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    # Register Blueprints
    from routes.auth import auth_bp
    from routes.shipment_routes import shipment_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(shipment_bp, url_prefix='/shipment')

    return app

if __name__ == "__main__":
    app = create_app()
    print(app.url_map)  # Debug routes
    app.run(debug=True)
