
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
 "name": "Ray",
  "mail": "ray2000227@gmail.com",
  "lab": 579
}

doc_ref = db.collection("資管").document("Ray")
doc_ref.set(doc)
