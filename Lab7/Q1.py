# Read the given "diabetes.csv" into a pandas data frame. Write a menu-driven program to calculate and print the following,

# 1. Find the probability of diabetes given the dataset. Also, calculate the probability of diabetes given


# a) Age above 50


# b) Age between 40 and 50


# c) Age between 30 and 40


# d) Age less than 30

import pandas as pd

df = pd.read_csv("diabetes.csv")

def main():
    print("1. Probability of diabetes given the dataset")
    print("2. Probability of diabetes given age above 50")
    print("3. Probability of diabetes given age between 40 and 50")
    print("4. Probability of diabetes given age between 30 and 40")
    print("5. Probability of diabetes given age less than 30")
    print("6. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            total = len(df)
            diabetes = len(df[df["Outcome"] == 1])
            print("Probability of diabetes given the dataset: ", round(diabetes / total, 3))
        elif choice == 2:
            total = len(df[df["Age"] > 50])
            diabetes = len(df[(df["Age"] > 50) & (df["Outcome"] == 1)])
            print("Probability of diabetes given age above 50: ", round(diabetes / total, 3))
        elif choice == 3:
            total = len(df[(df["Age"] > 40) & (df["Age"] < 50)])
            diabetes = len(df[(df["Age"] > 40) & (df["Age"] < 50) & (df["Outcome"] == 1)])
            print("Probability of diabetes given age between 40 and 50: ", round(diabetes / total, 3))
        elif choice == 4:
            total = len(df[(df["Age"] > 30) & (df["Age"] < 40)])
            diabetes = len(df[(df["Age"] > 30) & (df["Age"] < 40) & (df["Outcome"] == 1)])
            print("Probability of diabetes given age between 30 and 40: ", round(diabetes / total, 3))
        elif choice == 5:
            total = len(df[df["Age"] < 30])
            diabetes = len(df[(df["Age"] < 30) & (df["Outcome"] == 1)])
            print("Probability of diabetes given age less than 30: ", round(diabetes / total, 3))
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()