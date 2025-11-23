import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\r\OneDrive\Desktop\Coding\Projects\Netflix project\Netflix dataset.csv")

#print(df.head())

#Genre Analysis
genre_counts=df["genre"].value_counts()
most_common_genre = genre_counts.index[0]
print("The most common genre is:",most_common_genre)
#print(genre_counts)

#Rating Analysis
rating_count=df["rating"].value_counts()
most_common_rating=rating_count.index[0]
print("The most common rating is:",most_common_rating)
#print(rating_count)

#Duratin analysis
print("The average duration:",np.mean(df["duration"]))
print("The longest duration:",np.max(df["duration"]))
print("The shortest duration:",np.min(df["duration"]))

sort_movie_duration=np.sort(df["duration"])
print("The duration in sorted manner:\n",sort_movie_duration)

print("The movies greater than 100 minutes:\n")
for movie in df[df["duration"] > 100]["title"]:
    print(movie)

#Analyzing movies by genre and rating
sns.set_style("whitegrid")
fig ,axs=plt.subplots(1,3,figsize=(20,5))

sns.countplot(data=df,x="rating",palette="Set1",ax=axs[0])
sns.despine()
axs[0].set_title("Count Plot (Number of movies by rating)")

axs[1].pie(rating_count,labels=rating_count.index,autopct="%1.1f%%",explode=[0.1,0,0,0,0,0],shadow=True,startangle=90)
axs[1].set_title("Pie Chart (Rating Distribution)")

sns.kdeplot(data=df,x="duration",hue="rating",palette="Set1",ax=axs[2],fill=True,alpha=0.5)
sns.despine()
axs[2].set_title("KDE plot of durations")

plt.suptitle("Netflix / Movies Dataset Analysis", fontsize=16, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("multiplots1.png")
plt.show()



