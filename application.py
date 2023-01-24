from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
df = pd.read_csv('Cleaned_Car_Data.csv')

@app.route('/')
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    year = sorted(df['year'].unique(), reverse = True)
    fuel_type = sorted(df['fuel_type'].unique())
    return render_template('index.html', companies = companies, car_models = car_models, years = year, fuel_type = fuel_type)

if __name__ == "__main__":
    app.run(debug = True)