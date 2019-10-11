import pyrebase


def getdb():
    config = {

        "apiKey": "AIzaSyAbqDTZfoFwP57fClA0pCOgBMpr2uUdltA",
        "authDomain": "bookr-98a0a.firebaseapp.com",
        "databaseURL": "https://bookr-98a0a.firebaseio.com",
        "projectId": "bookr-98a0a",
        "storageBucket": "bookr-98a0a.appspot.com",
        "messagingSenderId": "158777667727",
        "appId": "1:158777667727:web:9ba5b74bb1b3ca96"

    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    return db


if __name__ == "__main__":
    getdb()
