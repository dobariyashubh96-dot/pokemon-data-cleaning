import pandas as pd


"""
Pokemon Dataset - Data Cleaning Project
Author: [Dobariya Shubh]
"""


# Load the dataset
df= pd.read_csv(r"C:\Users\dobar\Documents\CODING\Coding projects\learning\pokemon_data.csv")

# step 1: see what we have 
print(df.shape)            #* how many rows and columns
print(df.head(5))           #* see the first 5 rows of the dataset
print(df.isnull().sum())   #* which columns have missing values? 

# step 2: fix the missing values
df["Type 2"] = df["Type 2"].fillna("None")  #* fill missing values in "Type 2" column with "None"


# step 3: rename the column
df = df.rename(columns={"#": "pokedex_id"})

#step 4: add a new column
df["Total_stats"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]

# fix the names of the pokemon by removing "Mega " from the name if it exists
def fix_name(name):
    if "Mega " in name:
        clean = name.split("Mega ")[1]
        return clean
    return name
df["Name"] = df["Name"].apply(fix_name)
print(df.head(10))  #* see the first 5 rows of the cleaned dataset


#step 5: save the cleaned dataset
df.to_csv(r"C:\Users\dobar\Documents\CODING\Coding projects\learning\pokemon_data_cleaned.csv", index=False)
print("Data cleaning completed and saved to pokemon_data_cleaned.csv in the learning folder.")
