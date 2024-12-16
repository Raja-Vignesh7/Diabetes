# Diabetes Prediction for Women

## Overview
This project is a web application designed to predict the probability of diabetes in women based on various health parameters. It uses a machine learning model to make predictions and visualizes the results with severity levels.

The model achieves an accuracy of **98.39%** and considers features like:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

## Features
- User-friendly interface for inputting health data.
- Dynamic BMI calculation from height and weight.
- Predicts the probability of diabetes and categorizes the severity into three levels:
  - **Green**: No danger (Probability < 0.34)
  - **Orange**: Suggested to take precaution (0.34 ≤ Probability < 0.68)
  - **Red**: Better consult a doctor (0.68 ≤ Probability ≤ 1)
- Visual output using a bar graph to represent prediction severity.

---

## Project Structure
```
project/
|— client/
|   |— pages/
|   |   |— index.html        # Webpage template
|   |— static/
|       |— css/
|       |   |— style.css     # CSS for styling
|       |— js/
|           |— scripts.js    # JavaScript for functionality
|       |— utils/
|           |— diabeties_icon1.png  # Icon
|— server/
|   |— Diabetes.joblib       # Trained ML model
|— app.py                    # Flask server
|— main.py                   # Prediction logic and visualization
```

---

## Installation and Setup

### Prerequisites
- Python 3.7+
- Flask
- joblib
- numpy
- pandas
- matplotlib

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Raja-Vignesh7/Diabetes.git
   cd project/
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000` to access the application.

---

## Usage
1. Enter your health details in the input fields, such as:
   - Name
   - Age
   - Height
   - Weight
   - Blood Pressure
   - Number of Pregnancies
   - Glucose Levels
   - Diabetes Pedigree Function
   - Skin Thickness
   - Insulin

2. Click on the **Submit** button.
3. The application calculates BMI and predicts the probability of diabetes.
4. The output section displays:
   - Probability percentage
   - Severity bar graph with color coding.

---

## Code Explanation

### 1. `app.py`
- Serves the web application using Flask.
- Routes:
  - `/`: Renders the main page.
  - `/get_prob`: Handles POST requests for predictions.
- Dynamically calculates BMI and interacts with the prediction logic in `main.py`.

### 2. `main.py`
- Contains the `Model` class for loading the trained model and making predictions.
- Contains the `image_Result` class for creating visualizations of severity levels based on prediction probability.

### 3. Frontend
- **HTML**: Basic structure for user inputs and displaying results.
- **CSS**: Styling for a clean and responsive user interface.
- **JavaScript**: Handles form submission and AJAX requests to the Flask backend.

---

## Prediction Severity Levels
- **Green**: Probability < 0.34 — "Perfect, no danger"
- **Orange**: 0.34 ≤ Probability < 0.68 — "Suggested to take precaution"
- **Red**: 0.68 ≤ Probability ≤ 1 — "Better consult a doctor"

---

## Future Enhancements
- Include more user-friendly visualizations.
- Add authentication for users.
- Expand the model to include data for men.
- Deploy the application on a cloud platform (e.g., AWS, Heroku).

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgements
- **Scikit-learn**: For machine learning model training.
- **Flask**: For backend development.
- **Matplotlib**: For creating the visualizations.

---

## Contact
For any questions or feedback, feel free to contact **Raja Vignesh** at [rajavigneshgoud2022@gmail.com].

