# -----------------------------
# IMPORT LIBRARIES
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# -----------------------------
# LOAD EXCEL DATASET
# -----------------------------
df = pd.read_excel("indian_movies_full_1000.xlsx")

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Convert numeric columns
df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce')
df['No_of_Votes'] = pd.to_numeric(df['No_of_Votes'], errors='coerce')
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

# Clean Runtime column (e.g., "150 min" -> 150)
df['Runtime'] = df['Runtime'].astype(str).str.replace("min", "").str.strip()
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')

# Drop rows with missing important values
df = df.dropna(subset=['IMDB_Rating', 'Genre', 'Released_Year'])


# -----------------------------
# 1. GENRE DISTRIBUTION
# -----------------------------
plt.figure(figsize=(12,6))
df['Genre'].value_counts().head(15).plot(kind='bar', color='skyblue')
plt.title("Top Genres in Indian Movies")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 2. IMDB RATINGS DISTRIBUTION
# -----------------------------
plt.figure(figsize=(10,5))
sns.histplot(df['IMDB_Rating'], bins=20, kde=True)
plt.title("IMDb Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 3. MOVIES RELEASED PER YEAR
# -----------------------------
yearly = df['Released_Year'].value_counts().sort_index()

plt.figure(figsize=(12,5))
plt.plot(yearly.index, yearly.values, marker='o')
plt.title("Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# -----------------------------
# 4. TOP DIRECTORS BY MOVIE COUNT
# -----------------------------
plt.figure(figsize=(12,6))
df['Director'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Directors (Most Movies Made)")
plt.xlabel("Director")
plt.ylabel("Movie Count")
plt.xticks(rotation=40)
plt.show()

# -----------------------------
# 5. TOP ACTORS BY AVERAGE RATING
# -----------------------------
actors = df.groupby('Star1')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
actors.plot(kind='bar', color='green')
plt.title("Top 10 Lead Actors (Avg IMDb Rating)")
plt.xlabel("Actor")
plt.ylabel("Average Rating")
plt.xticks(rotation=40)
plt.show()

# -----------------------------
# 6. RATING vs GROSS COLLECTION
# -----------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='IMDB_Rating', y='Gross', size='No_of_Votes', hue='No_of_Votes', legend=False)
plt.title("IMDb Rating vs Gross Earnings")
plt.xlabel("Rating")
plt.ylabel("Gross Collection (₹)")
plt.show()

# -----------------------------
# 7. CORRELATION HEATMAP
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df[['IMDB_Rating','No_of_Votes','Gross','Runtime']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("All visualizations generated successfully!")
