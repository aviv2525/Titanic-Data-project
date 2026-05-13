import pandas as pd

df = pd.read_csv("titanic.csv")

# 1 :
female_count = len(df[df['sex'] == 'female'])
print(female_count)

# 2 :
male_count = len(df[df['sex'] == 'male'])
print(male_count)

# 3 :
young_count = len(df[df['age'] < 18])
print(young_count)

# 4 :
female_survived = len(df[(df['sex'] == 'female') & (df['survived'] == 1)])
female_survival_rate = (female_survived / female_count) * 100
print(female_survival_rate)

# 5 :
male_survived = len(df[(df['sex'] == 'male') & (df['survived'] == 1)])
male_survival_rate = (male_survived / male_count) * 100
print(male_survival_rate)

# 6 :
young_survived = len(df[(df['age'] < 18) & (df['survived'] == 1)])
young_survival_rate = (young_survived / young_count) * 100
print(young_survival_rate)


print(f"Number of females: {female_count}")
print(f"Number of males: {male_count}")
print(f"Number of young passengers: {young_count}")
print(f"Female survival rate: {female_survival_rate:.2f}%")
print(f"Male survival rate: {male_survival_rate:.2f}%")
print(f"Young survival rate: {young_survival_rate:.2f}%")
