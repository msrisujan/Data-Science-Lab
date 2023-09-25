# Find the probability of diabetes with a glucose level of more than 120 + blood pressure of more than 90 + skin thickness of more than 30 + insulin above 150 + BMI above 25.

import pandas as pd

df = pd.read_csv("diabetes.csv")

def main():
    total = len(df[(df["Glucose"] > 120) & (df["BloodPressure"] > 90) & (df["SkinThickness"] > 30) & (df["Insulin"] > 150) & (df["BMI"] > 25)])
    diabetes = len(df[(df["Glucose"] > 120) & (df["BloodPressure"] > 90) & (df["SkinThickness"] > 30) & (df["Insulin"] > 150) & (df["BMI"] > 25) & (df["Outcome"] == 1)])
    print("Probability of diabetes with...: ", round(diabetes / total, 3))

if __name__ == "__main__":
    main()