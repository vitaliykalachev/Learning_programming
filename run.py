from app import app
import os
# app.secret_key = "super secret key"
SECRET_KEY = os.getenv('SECRET_KEY', 'Optional default value')

if __name__ == "__main__":
    # app.secret_key = "super secret key"
    app.run(debug=True)
    app.run()







