from flask import Flask, render_template, request, jsonify
import json
import pprint

json_path = "./symptom.json"
with open(json_path,"r") as file:
  data = json.load(file)

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('prac.html', data=data)

@app.route("/store_symptoms", methods=["POST"])
def store_symptoms():
    selected_symptoms = request.form.getlist("symptoms[]")
    # Here you can add code to store the selected symptoms
    return jsonify({"selected_symptoms": selected_symptoms})
if __name__ == "__main__":
  app.run(debug=True)
