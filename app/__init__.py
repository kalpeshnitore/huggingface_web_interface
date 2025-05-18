# पॅकेज इनिशियलायझेशन
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    with app.app_context():
        from . import routes
        routes.init_routes(app)
    
    return app