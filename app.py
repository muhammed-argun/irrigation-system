from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__,
            static_folder='assets',  # Burada assets dizini statik dosya klasörü olarak belirleniyor
            static_url_path='/assets')  # Yani statik dosyalara /assets/ yoluyla erişilecek

# Geçici veri saklama (veritabanı olmadığında)
data = {"soil_moisture": "Dry", "water_pump": "OFF"}

@app.route('/')
def home():
    return render_template('index.html')

# Statik dosyaların erişilebileceği yer
@app.route('/assets/<path:filename>')
def download_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'assets'), filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
