from notes import create_app

if __name__ == "__main__":
    app = create_app('flask.cfg')
    app.run(port=5001)