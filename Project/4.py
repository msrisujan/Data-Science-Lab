import pandas as pd
import random as rd

df = pd.read_csv('Dataset_rol_1.csv')
name = list(df['Name'])
rollno = list(df['Roll No'])
degree = list(df['Degree'])
gender = list(df['Gender'])
sem = list(df['Sem'])
age = list(df['Age'])
gym = list(df['Gym/badminton'])

dataset = {
    'Name': [],
    'Roll No': [],
    'Degree': [],
    'Gender': [],
    'Sem': [],
    'Age': [],
    'Height': [],
    'Weight': [],
    'BMI': [],
    'Gym/badminton': [],
}

# fit male height range is 168-175
# fit male weight range is 68-80
# fit female height range is 162-170
# fit female weight range is 58-70

# count number of 1's in sem
# count = 0
# for i in range(len(sem)):
#     seme = str(sem[i])
#     if seme == "7":
#         count += 1
# print(count)

# for students in sem 3, for random 50% of them, assign fit height and weight
count1 = 0
count2 = 0
count3 = 0
for i in range(len(rollno)):
    seme = str(sem[i])
    gendere = str(gender[i])
    if seme == "3":
        if count1 <= 89:
            if gendere == "Male":
                height = rd.randint(168, 175)
                weight = rd.randint(68, 80)
            else:
                height = rd.randint(162, 170)
                weight = rd.randint(58, 70)
        else:
            if gendere == "Male":
                height1 = rd.randint(158,167)
                height2 = rd.randint(176, 185)
                height = rd.choice([height1, height2])
                weight1 = rd.randint(50, 67)
                weight2 = rd.randint(81, 100)
                if height == height1:
                    weight = weight1
                else:
                    weight = weight2
        bmi = round(weight / ((height / 100) ** 2), 2)
        dataset['Name'].append(name[i])
        dataset['Roll No'].append(rollno[i])
        dataset['Degree'].append(degree[i])
        dataset['Gender'].append(gender[i])
        dataset['Sem'].append(sem[i])
        dataset['Age'].append(age[i])
        dataset['Height'].append(height)
        dataset['Weight'].append(weight)
        dataset['BMI'].append(bmi)
        dataset['Gym/badminton'].append(gym[i])
        count1 += 1
    elif seme == "5":
        if count1 <= 40:
            if gendere == "Male":
                height = rd.randint(168, 175)
                weight = rd.randint(68, 80)
            else:
                height = rd.randint(162, 170)
                weight = rd.randint(58, 70)
        else:
            if gendere == "Male":
                height1 = rd.randint(158,167)
                height2 = rd.randint(176, 185)
                height = rd.choice([height1, height2])
                weight1 = rd.randint(50, 67)
                weight2 = rd.randint(81, 100)
                if height == height1:
                    weight = weight1
                else:
                    weight = weight2
        bmi = round(weight / ((height / 100) ** 2), 2)
        dataset['Name'].append(name[i])
        dataset['Roll No'].append(rollno[i])
        dataset['Degree'].append(degree[i])
        dataset['Gender'].append(gender[i])
        dataset['Sem'].append(sem[i])
        dataset['Age'].append(age[i])
        dataset['Height'].append(height)
        dataset['Weight'].append(weight)
        dataset['BMI'].append(bmi)
        dataset['Gym/badminton'].append(gym[i])
        count2 += 1
    elif seme == "7":
        if count1 <= 74:
            if gendere == "Male":
                height = rd.randint(168, 175)
                weight = rd.randint(68, 80)
            else:
                height = rd.randint(162, 170)
                weight = rd.randint(58, 70)
        else:
            if gendere == "Male":
                height1 = rd.randint(158,167)
                height2 = rd.randint(176, 185)
                height = rd.choice([height1, height2])
                weight1 = rd.randint(50, 67)
                weight2 = rd.randint(81, 100)
                if height == height1:
                    weight = weight1
                else:
                    weight = weight2
        bmi = round(weight / ((height / 100) ** 2), 2)

        height = rd.randint(168, 175)
        weight = rd.randint(68, 80)
        bmi = round(weight / ((height / 100) ** 2), 2)
        dataset['Name'].append(name[i])
        dataset['Roll No'].append(rollno[i])
        dataset['Degree'].append(degree[i])
        dataset['Gender'].append(gender[i])
        dataset['Sem'].append(sem[i])
        dataset['Age'].append(age[i])
        dataset['Height'].append(height)
        dataset['Weight'].append(weight)
        dataset['BMI'].append(bmi)
        dataset['Gym/badminton'].append(gym[i])
        count3 += 1

df = pd.DataFrame(dataset)
df.to_csv('Dataset_No.csv', index=False)


