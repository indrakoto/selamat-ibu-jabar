from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('ta_rf.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', jumlah_prediksi=0)

@app.route('/predict', methods=['POST'])
def predict():

    jumlah, umur_kematian, ibu = [x for x in request.form.values()]

    data = []

    data.append(int(umur_kematian))
    data.append(int(ibu))
    
    #print(data)
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)
    
    if umur_kematian == '1':
        usia = '< 20 TAHUN'
    elif umur_kematian == '2':
        usia = '20 - 34 TAHUN'
    else:
        usia = '>= 35 TAHUN'

    if ibu == '1':
        kategori = 'IBU HAMIL'
    elif ibu == '2':
        kategori = 'IBU HAMIL'
    else:
        kategori = 'IBU NIFAS'
        
    jumlah_prediksi = 0
    
    if(int(jumlah) > output):
        jumlah_prediksi = "Jumlah Ibu Selamat = " + str(int(jumlah) - output)
    #else:
    #    jumlah_prediksi = 0
    

    return render_template('index.html', hasil=jumlah_prediksi, jumlah=jumlah, usia=usia, kategori=kategori)


if __name__ == '__main__':
    app.run(debug=True)