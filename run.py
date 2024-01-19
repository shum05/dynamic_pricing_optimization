from app import app
import os

app.secret_key = os.urandom(24)

#app.secret_key = 'your_secret_key_here'

if __name__ == '__main__':
    app.run(debug=True)
