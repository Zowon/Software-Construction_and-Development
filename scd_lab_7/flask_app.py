from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import xml.etree.ElementTree as ET

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK with your service account key
cred = credentials.Certificate('/home/YousafMaaz/scd-lab-be607-firebase-adminsdk-upten-580319a2fb.json')
initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Root Route
@app.route('/')
def home():
    return 'Welcome to the XML to Firestore App!'

# Handle Favicon Request
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Endpoint to receive XML data and store it in Firestore
@app.route('/receive-data', methods=['POST'])
def receive_data():
    try:
        # Parse the XML data from the request
        xml_data = request.data
        root = ET.fromstring(xml_data)

        # Extract user data (name and email)
        user_data = {
            'name': root.find('name').text,
            'email': root.find('email').text
        }

        # Store data in Firestore in the 'users' collection
        doc_ref = db.collection('users').add(user_data)

        # Return a JSON response with the Firestore document ID and user data
        return jsonify({'id': doc_ref[1].id, **user_data}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Test Firestore connectivity
@app.route('/test-firestore', methods=['GET'])
def test_firestore():
    try:
        collections = db.collections()
        collection_names = [collection.id for collection in collections]
        return jsonify({'collections': collection_names})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
