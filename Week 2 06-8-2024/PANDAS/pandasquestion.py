import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

# Load the dataset into a Pandas DataFrame and display the first 5 rows to get an idea of the data.
df = pd.read_csv("Week 2 06-8-2024\PANDAS\sports_car_price.csv")
# Use Pandas to clean the dataset by removing any missing or duplicate values, and converting any non-numeric data to numeric data where appropriate.
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["Price (in USD)"] = df["Price (in USD)"].apply(lambda x: x.replace(",", ""))
df.head()


# Function to apply lambda to a column
def apply_lambda(col, l):
    df[col] = df[col].apply(l)


# Function to replace redundant signs in values
def replace_string(col, str1, str2):
    df[col] = df[col].apply(lambda x: str(x).replace(str1, "").replace(str2, ""))


# Apply replacements
replace_string("Horsepower", ",", "+")
replace_string("Torque (lb-ft)", "-", "+")
replace_string("Torque (lb-ft)", ",", "")
replace_string("0-60 MPH Time (seconds)", "<", "+")

df["Electric"] = df["Engine Size (L)"].copy()
apply_lambda("Electric", lambda x: "No" if "Electric" not in str(x) else "Yes")
df["Electric"].unique()

df["Hybrid"] = df["Engine Size (L)"].copy()
apply_lambda("Hybrid", lambda x: "No" if "Hybrid" not in str(x) else "Yes")
df["Hybrid"].unique()

apply_lambda(
    "Engine Size (L)",
    lambda x: x if len(str(x)) == 1 else re.search("\d{1}\.\d{1}", str(x)),
)
apply_lambda("Engine Size (L)", lambda x: x.group() if type(x) == re.Match else x)
replace_string("Engine Size (L)", "-", "")
df["Engine Size (L)"].unique()
replace_string("Horsepower", ",", "+")
replace_string("Torque (lb-ft)", "-", "+")
replace_string("Torque (lb-ft)", ",", "")
replace_string("0-60 MPH Time (seconds)", "<", "+")
df["0-60 MPH Time (seconds)"].unique()
df.iloc[:, 3:8] = df.iloc[:, 3:8].apply(pd.to_numeric, errors="coerce")
df["Engine Size (L)"].isna().sum()
mean = df["Engine Size (L)"].mean()
print(mean)
df["Engine Size (L)"] = df["Engine Size (L)"].fillna(mean)
df["Torque (lb-ft)"].isna().sum()
mean = df["Torque (lb-ft)"].mean()
print(mean)
df["Torque (lb-ft)"] = df["Torque (lb-ft)"].fillna(mean)
df["Engine Size (L)"] = df["Engine Size (L)"].astype(int)
df["Horsepower"] = df["Horsepower"].astype(int)
df["Torque (lb-ft)"] = df["Torque (lb-ft)"].astype(int)
df["0-60 MPH Time (seconds)"] = df["0-60 MPH Time (seconds)"].astype(int)
df["Price (in USD)"] = df["Price (in USD)"].astype(int)
# Use Pandas to explore the dataset by computing summary statistics for each column, such as mean, median, mode, standard deviation, and range.
df.describe()
# Use Pandas to group the dataset by car make and compute the average price for each make.
# Group by 'Car Make' and calculate the average price
average_price = df.groupby("Car Make")["Price (in USD)"].mean()

# Print the result
print(average_price)
# Use Pandas to group the dataset by year and compute the average horsepower for each year.
avg_horsepower = df.groupby("Year")["Horsepower"].mean()
print(avg_horsepower)
# Use Pandas to create a scatter plot of price versus horsepower, and add a linear regression line to the plot.

# Create the scatter plot with regression line
sns.regplot(x="Horsepower", y="Price (in USD)", data=df)

plt.show()

# Use Pandas to create a histogram of the 0-60 MPH times in the dataset, with bins of size 0.5 seconds.
# Use Pandas to filter the dataset to only include cars with a price greater than $500,000,and then sort the resulting dataset by horsepower in descending order.
# Use Pandas to export the cleaned and transformed dataset to a new CSV file.
import pandas as pd
import matplotlib.pyplot as plt

# Histogram of 0-60 MPH times with 0.5 second bins
plt.hist(
    df["0-60 MPH Time (seconds)"],
    bins=np.arange(
        df["0-60 MPH Time (seconds)"].min(),
        df["0-60 MPH Time (seconds)"].max() + 0.5,
        0.5,
    ),
)
plt.xlabel("0-60 MPH Time (seconds)")
plt.ylabel("Frequency")
plt.title("Histogram of 0-60 MPH Times")
plt.show()

# Filter cars with price greater than $500,000 and sort by horsepower
filtered_df = df[df["Price (in USD)"] > 500000].sort_values(
    by="Horsepower", ascending=False
)

# Export filtered and sorted data to a new CSV file
filtered_df.to_csv("high_priced_cars.csv", index=False)
