from flask import Flask, render_template
from auth.routes import auth as auth_blueprint
from inventory.routes import inventory as inventory_blueprint


def create_app():
    app = Flask(__name__)

    # Set debug mode
    app.config['DEBUG'] = True

    # Register blueprints
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(inventory_blueprint, url_prefix='/inventory')

    # Root route
    @app.route('/')
    def home():
        return render_template('index.html')  # Render the index.html template

    return app
