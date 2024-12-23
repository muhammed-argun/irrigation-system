from flask import Flask, render_template, request, jsonify
import os
from flask import Flask

app = Flask(__name__)

# Geçici veri saklama (veritabanı olmadığında)
data = {"soil_moisture": "Dry", "water_pump": "OFF"}

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/update', methods=['POST'])
def update_data():
    global data
    data['soil_moisture'] = request.json.get('soil_moisture', data['soil_moisture'])
    data['water_pump'] = request.json.get('water_pump', data['water_pump'])
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
