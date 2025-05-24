# 🖊️ Digital Signature Web App

A simple and educational web application to demonstrate **Digital Signature Algorithm (ECDSA)** using Python and JavaScript.

🌐 **Live Demo**: [https://sehaton.pythonanywhere.com/](https://sehaton.pythonanywhere.com/)

---

## 📸 Features

- 🔐 **Key Pair Generation** – Generate public and private keys.
- ✍️ **Message Signing** – Use the private key to create a digital signature.
- ✅ **Signature Verification** – Verify the authenticity of a message using the public key and signature.
- 🧠 Designed to be simple and beginner-friendly – great for learning how digital signatures work!

---

## 🛠️ Technologies Used

### 👨‍💻 Frontend
- **HTML5**
- **CSS3**
- **JavaScript (Vanilla)** – For handling user interactions and API calls.

### 🐍 Backend
- **Python 3**
- **Flask** – Lightweight web framework to handle backend logic and routing.
- **cryptography** – Secure Python library for cryptographic operations.

---

## 📦 Python Libraries

| Library        | Purpose                                  |
|----------------|-------------------------------------------|
| `flask`        | Web framework for creating the backend   |
| `cryptography` | Handling key generation, signing, and verifying with ECDSA |

Install them via:

```bash
pip install flask cryptography
