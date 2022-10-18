from firebase import Firebase
config = {
  'apiKey': "AIzaSyCtdY9w1rhXYB4rpRLJ3Gh_oSwlMmPtMO8",
  'authDomain': "steganography-messaging.firebaseapp.com",
  'projectId': "steganography-messaging",
  'storageBucket': "steganography-messaging.appspot.com",
  'messagingSenderId': "263877255888",
  'appId': "1:263877255888:web:ce3171ca7a50df913874d5",

};
database=Firebase(config)
print(database)
