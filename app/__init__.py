from flask import Flask


app = Flask(__name__)
app.secret_key = "super secret key"

from app import views
from app import admin_views