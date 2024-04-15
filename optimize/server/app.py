from flask import Flask, jsonify
from flask_cors import CORS
import CalculationGA
import CalculationBox

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

CalculationGA = CalculationGA.main()

@app.route('/GA', methods=['GET'])
def calculat_GA():
    return jsonify(CalculationGA)

CalculationBox = CalculationBox.main()

@app.route('/Box', methods=['GET'])
def calculat_Box():
    return jsonify(CalculationBox)

if __name__ == '__main__':
    app.run()