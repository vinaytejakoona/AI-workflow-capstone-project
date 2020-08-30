from flask import Flask
app = Flask(__name__)
from model import model_predict,model_train
import json

@app.route('/predict/<country>/<year/<month>/<day>')
def predict(country,year,month,day):
    out = model_predict(country,year,month,day)
    return json.dumps(out)

@app.route('/train')
def predict(country,year,month,day):
    model_train()
    return "model trained"
