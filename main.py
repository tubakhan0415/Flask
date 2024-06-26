from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from chat import get_response

app = Flask(__name__)
CORS(app)

@app.route("/")  # Correcting the decorator here
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])  # Added methods parameter to specify POST
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    app.run(host='0.0.0.0', port=port)
   
