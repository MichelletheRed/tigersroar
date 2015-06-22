'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_table('imdb_1000.csv', sep=',')
# check the number of rows and columns
movies.shape (979,6) = 979 rows and 6 columns
# check the data type of each column
movies.dtypes
# calculate the average movie duration
movies.describe(include='all') = 121 minutes
# sort the DataFrame by duration to find the shortest and longest movies
movies.duration.describe() = 242 max, 64 min
# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=5)
# use a box plot to display that same data
movies.duration.plot(kind='box')
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()
# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar')
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace('APPROVED','PASSED','GP','NOT RATED', inplace='UNRATED')
# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace('X','TV-MA', inplace='NC-17')
# count the number of missing values in each column
movies.content_rating.isnull().sum()
# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.fillna(value='UNRATED')
# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies.groupby('duration').describe()
# use a visualization to detect whether there is a relationship between star rating and duration
movies.boxplot(column='star_rating', by='duration')
# calculate the average duration for each genre
movies.groupby('genre').duration.agg(['mean'])
'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

# determine the top rated movie (by star rating) for each genre

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
