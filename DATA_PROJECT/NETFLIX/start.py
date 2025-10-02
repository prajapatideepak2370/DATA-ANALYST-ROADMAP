import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(
    r"C:\Users\praja\Downloads\Basicpy\DATA_PROJECT\NETFLIX\Netflix Shows.csv",
    encoding="latin1"
)

df = pd.DataFrame(df)

# print(df.head())
# print(df.describe())
# print(df.isnull().sum())

# print(df.columns.tolist())
df.columns = df.columns.str.strip()

df.dropna(subset=[
    'title',
    'rating',
    'ratingDescription',
    'release year',
    'user rating score',
    'user rating size'  # no space at the end
], inplace=True)
# print(df.info())

type_count = df['title'].value_counts()
plt.figure(figsize=((6,2)))
plt.bar(type_count.index, type_count.values, color='blue')
plt.xlabel('Title')
plt.ylabel('Count')
plt.title('Netflix Show Count by Title')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

type_rating = df['rating'].value_counts()
plt.figure(figsize=((8,6)))
plt.pie(type_rating, labels=type_rating.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Netflix Shows by Rating')
plt.axis('equal') 
plt.legend(title='Ratings', loc='upper left')
plt.tight_layout()
plt.savefig('netflix_shows_by_rating.png', dpi=300, bbox_inches='tight')
# plt.show()

release_year_count = df['release year'].value_counts().sort_index()
plt.figure(figsize=((10,5)))
plt.scatter(release_year_count.index, release_year_count.values, color='green')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows Released')
plt.title('Number of Netflix Shows Released by Year')
plt.legend(title='Release Year', loc='upper left')
plt.tight_layout()
plt.savefig('netflix_shows_by_release_year.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()