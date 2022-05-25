from app import app

app.secret_key = "super secret key"

if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True)
    app.run()







