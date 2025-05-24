from flask import Flask, request, jsonify, render_template
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

app = Flask(__name__)

# 🏠 Homepage (key generation + signing)
@app.route('/')
def index():
    return render_template('index.html')

# 🔍 Verification page
@app.route('/verify-tab')
def verify_tab():
    return render_template('verify.html')

# 🔑 Generate a new key pair (private + public)
@app.route('/generate_keys')
def generate_keys():
    # Create a private key (used for signing)
    private_key = ec.generate_private_key(ec.SECP256R1())
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()

    # Get the public key (used for verifying)
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    # Send both to the frontend
    return jsonify({
        'private_key': private_pem,
        'public_key': public_pem
    })

# ✍️ Sign a message using private key
@app.route('/sign', methods=['POST'])
def sign_message():
    data = request.get_json()
    message = data['message']
    private_pem = data['private_key']

    # Load the private key from the text
    private_key = serialization.load_pem_private_key(
        private_pem.encode(),
        password=None
    )

    # Sign the message
    signature = private_key.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )

    # Send back the signature in hex format
    return jsonify({ 'signature': signature.hex() })

# ✅ Verify the signature using the public key
@app.route('/verify', methods=['POST'])
def verify_signature():
    data = request.get_json()
    message = data['message']
    signature = bytes.fromhex(data['signature'])
    public_pem = data['public_key']

    # Load the public key from the text
    public_key = serialization.load_pem_public_key(public_pem.encode())

    # Try verifying the signature
    try:
        public_key.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return jsonify({ 'valid': True })
    except InvalidSignature:
        return jsonify({ 'valid': False })

# 🟢 Start the server
if __name__ == '__main__':
    app.run(debug=True)