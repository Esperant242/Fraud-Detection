from flask import Flask

app = Flask(__name__)

# Charger les routes
from app import routes