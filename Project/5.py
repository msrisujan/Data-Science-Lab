import pandas as pd
import random as rd

# df1 = pd.read_csv('Dataset_Yes.csv')
# df2 = pd.read_csv('Dataset_No.csv')

# df = pd.concat([df1, df2], ignore_index=True)

#add duplicates and null values
df=pd.read_csv('Dataset_Final4.csv')
# cgpas=[]
#generate random cgpas 
# for i in range(len(df)):
#     cgpas.append(round(rd.uniform(5,10),2))
# df['CGPA']=cgpas
# column_to_move=df.pop('CGPA')
# df.insert(5,'CGPA',column_to_move)
# df.drop('CGPA', axis=1, inplace=True)
#print matching values
# for i in range(len(df)):
#     for j in range(len(df)):
#         if(i==j):
#             continue
#         else:
#             if(df['Roll No'][i]==df['Roll No'][j]):
#                 print(df['Roll No'][i])
# count = 0
# for i in range(len(df)):
#     if df['Height'][i] >=170  and df['Height'][i] < 186:
#         count += 1
# print(count)

# count1 = 0
# count2 = 0
for i in range(len(df)):
    df['BMI'][i] = round(df['Weight'][i]/(df['Height'][i]/100)**2,2)
    # if count2 <= 150:
    #     if df['Height'][i] >= 55 and df['Height'][i] < 75:
    #         df['Height'][i] -= 2
    #         df['BMI'][i] = round(df['Weight'][i]/(df['Height'][i]/100)**2,2)
    #         count2 += 1

shuffle_df = df.sample(frac=1)

shuffle_df.to_csv('Dataset_Final4.csv', index=False)