#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:17:45 2024

@author: user
"""
import pandas as pd
"""
Question 1
-------------------------------------------------------------------------------
"""
# Load the dataset
file_path = 'movie_dataset.csv'  # Replace with the path to your dataset
movies = pd.read_csv(file_path)

# Find the movie with the highest rating
highest_rated_movie = movies.loc[movies['Rating'].idxmax()]

# Display the title and rating of the highest-rated movie
print("\nQuestion 1")
print(f"Highest Rated Movie: {highest_rated_movie['Title']}")
print(f"Rating: {highest_rated_movie['Rating']}")
print("-------------------------------------------------------------------------------")

"""
Question 2
-------------------------------------------------------------------------------
"""
#Cleaning the data for missing values (NaN)
cleaned_movies_data = movies.dropna()

#Calculating the average revenue, 
average_revenue = cleaned_movies_data['Revenue (Millions)'].mean()

# Display the average revenue
print("\nQuestion 2")
print(f"Average Revenue: {average_revenue:.2f} Million")
print("-------------------------------------------------------------------------------")

"""
Question 3
-------------------------------------------------------------------------------
"""
#Filter movies from 2015 to 2017
filtered_data = cleaned_movies_data[(cleaned_movies_data['Year'] >= 2015) & (cleaned_movies_data['Year'] <= 2017)]

#Calculate the average revenue
average_revenue = filtered_data['Revenue (Millions)'].mean()

print("\nQuestion 3")
print(f"\nAverage Revenue (2015 - 2017) :  {average_revenue:.2f} Million")
print("-------------------------------------------------------------------------------")

"""
Question 4
-------------------------------------------------------------------------------
"""
movies_2016 = movies[(movies['Year'] == 2016)]
number_2016_movies = movies_2016['Year']

print("\nQuestion 4")
print(f"Number of movies released in 2016 : {len(number_2016_movies)}")
print("-------------------------------------------------------------------------------")

"""
Question 5
-------------------------------------------------------------------------------
"""
movies_dir_Nolan = movies[(movies['Director'] == "Christopher Nolan" )]
number_of_movies_Nolan = len(movies_dir_Nolan['Director'])

print("\nQuestion 5")
print(f"Number of movies directed by Christopher Nolan : {number_of_movies_Nolan}")
print("-------------------------------------------------------------------------------")


"""
Question 6
-------------------------------------------------------------------------------
"""
movies_atl_rating_8 = movies[(movies['Rating'] >= 8.0)]
number_of_movies_atl_rating_8 = len(movies_atl_rating_8['Rating'])

print("\nQuestion 6")
print(f"Number of movies with a rating of at least 8.0: {number_of_movies_atl_rating_8}")
print("-------------------------------------------------------------------------------")


"""
Question 7
-------------------------------------------------------------------------------
"""
movies_dir_Nolan = movies[(movies['Director'] == "Christopher Nolan" )]
median_of_movies_Nolan = movies_dir_Nolan['Rating'].median()

print("\nQuestion 7")
print(f"Median of movies directed by Christopher Nolan : {median_of_movies_Nolan}")
print("-------------------------------------------------------------------------------")


"""
Question 8
-------------------------------------------------------------------------------
"""
movies_by_year = movies.groupby('Year')['Rating'].mean()
highest_average_rated_movie = movies_by_year.idxmax()

print(highest_average_rated_movie)

print("\nQuestion 8")
print(f"The year of the highest average movie rating : {movies_by_year.idxmax()}")
print(f"Average rating: {movies_by_year.max()}")
print("-------------------------------------------------------------------------------")

"""
Question 9
-------------------------------------------------------------------------------
"""
movies_2006 = movies[(movies['Year'] == 2006)]
number_2006_movies = len(movies_2006['Year'])
print(number_2006_movies)


movies_2016 = movies[(movies['Year'] == 2016)]
number_2016_movies = len(movies_2016['Year'])


Percentage_increase = (number_2016_movies - number_2006_movies)/number_2006_movies *100

print("\nQuestion 9")
print(f"The percentage increase in number of movies made between 2006 and 2016 : {Percentage_increase} ")
print("-------------------------------------------------------------------------------")


"""
Question 10
-------------------------------------------------------------------------------
"""

names = []

for actors_block in movies['Actors']:
    names += actors_block.split(', ')

most_occuring = max(names, key=names.count)

print("\nQuestion 10")
print(f"The most occurring actors: {most_occuring}")

"""
Question 11
-------------------------------------------------------------------------------
"""

genres = []

for genres_block in movies['Genre']:
    genres += genres_block.split(',')

unduplicated_genres = list(dict.fromkeys(genres))

number_of_unique_genres = len(unduplicated_genres)

print("\nQuestion 11")
print(f"Number of unique genre : {number_of_unique_genres}")


