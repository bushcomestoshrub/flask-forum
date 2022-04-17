from application import app, db


def run_app():
    db.create_all()
    app.run()
