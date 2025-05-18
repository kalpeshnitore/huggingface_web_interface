from flask import Flask
from app.routes import init_routes

app = Flask(__name__, template_folder='app/templates')
app.config['SECRET_KEY'] = 'your-secret-key-here'

# रूट्स इनिशियलाइज करा
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)