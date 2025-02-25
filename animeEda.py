import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r"F:\Downloads\anime.csv")
df.info()
print(df.head())
print(df.columns)
print(df.info())


Distribution of Anime Types: 

df_counts = df['type'].value_counts()

plt.bar(df_counts.index, df_counts.values)
plt.xticks(rotation=90)
plt.xlabel("Anime Type")
plt.ylabel("Count")
plt.title("Anime Type Distribution")
plt.show()

top Rated Anime

top_rated_anime = df.nlargest(10, "rating")
plt.figure(figsize = (12, 6))
sns.barplot(x = top_rated_anime['rating'], y = top_rated_anime['name'])
plt.xlabel("Average Rating")
plt.ylabel("Anime Name")
plt.title("Top 10 Highest Rated Anime")
plt.show()



Plot distribution of anime ratings

plt.figure(figsize=(12, 6))
sns.histplot(df["rating"], bins=30, kde=True, color="blue")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.title("Distribution of Anime Ratings")

plt.show()


Top 10 Most Popular Anime (by number of members)
top_popular_anime = df.nlargest(10, "members")
plt.figure(figsize=(12, 6))
sns.barplot(x=top_popular_anime["members"], y=top_popular_anime["name"])
plt.xlabel("Number of Members")
plt.ylabel("Anime Name")
plt.title("Top 10 Most Popular Anime by Member Count")
plt.show()


print(df.isnull().sum())
df['genre'].fillna('Unknown', inplace=True)
df['type'].fillna('Unknown', inplace=True)

df['genre'] = df['genre'].fillna(df['genre'].mode())
df['type'] = df['type']. fillna(df['type'].mode())

print(df.isnull().sum())

df['rating'] = df['rating']. fillna(df['rating'].median())
print(df.isnull().sum())



df['genre'] = df['genre'].astype(str)


plt.scatter(df['genre'], df['members'])
plt.xlabel("Genre")
plt.ylabel("Members")
plt.xticks(rotation=90)  # Rotate labels for better visibility if many genres
plt.show()



# Convert categorical data to numeric where necessary for correlation
anime_numeric_df = df.copy()

# Convert 'type' to numerical codes
anime_numeric_df["type"] = anime_numeric_df["type"].astype("category").cat.codes

# Convert 'episodes' to numeric (handling "Unknown" values)
anime_numeric_df["episodes"] = pd.to_numeric(anime_numeric_df["episodes"], errors="coerce")

# Selecting numeric columns for correlation
numeric_columns = ["type", "episodes", "rating", "members"]
correlation_matrix = anime_numeric_df[numeric_columns].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Anime Dataset")

# Show plot
plt.show()





