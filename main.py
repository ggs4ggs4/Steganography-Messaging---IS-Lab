import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate('firebase.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

# As an admin, the app has access to read and write all data, regradless of Security Rules
db=firestore.client()
for i in db.collection("user_public").get():
    print(i.id, i.to_dict())