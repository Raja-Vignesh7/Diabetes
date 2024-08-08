from flask import Flask , render_template, jsonify, request
from main import Model , image_Result
import base64
import os

app = Flask(__name__,
            template_folder = os.path.join('..','client','pages'),
            static_folder = os.path.join('..','client','static'))

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/get_prob',methods=['POST'])
def predict_probability():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        array = data.get('array')           
        if not array:
            return jsonify({'error': 'Array not provided'}), 400
        BMI = round(array["Weight"]/((array["Height"]/100)**2),4)
        print(BMI," ",array['Pregnancies'])
        L = [[array["Pregnancies"]	,array["Glucose"]	,array["BloodPressure"]	,array["SkinThickness"],array["Insulin"],BMI,array["DiabetesPedigreeFunction"],array["Age"]	]]
        predicate = Model.Predicit(L)
        print(predicate[0][1])
        image = image_Result.get_image(predicate[0][1])
        img_str = base64.b64encode(image.getvalue()).decode('utf-8')
        return jsonify({'predicate': predicate[0][1] , 'image': img_str})
    except Exception as e:
        print("error: ", str(e))
        return jsonify({'error': str(e)}), 500
    
if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)