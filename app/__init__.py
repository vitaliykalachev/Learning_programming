from flask import Flask


app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

app.config.from_object("config.DevelopmentConfig")
app.secret_key = "\xf3\xc4]B'\xc7\x915f\x818\xc4N8Ak&\xba\x18}\xfe\x0b\xf3\xd0"

from app import views
from app import admin_views