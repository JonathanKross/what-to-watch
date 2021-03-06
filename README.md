# What to Watch
Build a movie recommender.
Use the MovieLens data to recommend movies to users.

## Objectives
After completing this assignment, you will...

- Be able to use the csv module to read files.
- Be able to use list comprehensions to filter data and perform calculations.
- Be able to model a problem using objects and functions.

## Deliverables
- A Git repo called what-to-watch containing at least:
- A README.md file explaining how to run your project.
- A movie_lib.py file containing your classes and functions.
- A movie_lib_tests.py file containing unit tests.
- Other Python files containing programs that use the classes in movie_lib.py.

### Normal Mode
First, go to the MovieLens website and download the MovieLens 100K data. Unzip it and read the README file to understand the data.

You will write a system that will recommend movies to a user based on ratings from similar users.

#### Step 1
Decide on the data structures that you're going to use to represent the information you'll need for this project.

You need to write classes to represent the concepts in this project. You also need to write tests for your classes preferably in a test-driven manner.

I suggest the following classes:

- Movie
- User
- Rating
Take a look at the MovieLens README file to determine what fields you should associate with each of these classes.

Note that you will need to make associations between users and ratings, and ratings and movies.

Specifically, you will need to be able to:

Find all ratings for a movie by id
Find the average rating for a movie by id
Find the name of a movie by id
Find all ratings for a user
Write methods to handle the above use cases, and then write some tests and load in some test data to ensure they work.

#### Step 2
You need to be able to load in movie and rating data. Using the csv module, write a module that will load in the the user data from u.user, the movie data from u.item, and the rating data from u.info.

#### Step 3
The easiest way to recommend movies is to recommend the most popular movies. Write a program to show the top X movies by average rating with their rating. You need to be able to state a minimum number of ratings for a movie to be considered.

Now, create the ability to find the top X movies by average rating that a specific user has not rated. This allows you to suggest popular movies for a specific user.

#### Step 4
Popular movies are not really good enough on their own. What would be great is a way to match two users by their tastes. You need to create the ability to take two users and find their similarity. There's a few ways to do this. We'll focus on the Euclidean distance. If you have a list of movie ratings for user 1 (v) and a list for user 2 (w), where each list is made up of ratings for movies they've both seen in the same order, then you can use this formula:

```
def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """

    # Guard against empty lists.
    if len(v) is 0:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))
```
#### Step 5
Now that you can calculate the similarity between two users, add a new ability. Given a list of all users, find the users most similar to a specific user, and then recommend the highest rated movies from those users that the specific user hasn't seen.

A good formula for figuring out movies that user might like the most is similarity * rating.

#### Step 6
Put this all together! The interface is up to you. You may want to have one program that presents a menu system so you can see top overall movies, popular movies you haven't seen (you'll have to give your user id), or recommendations specific to you.

Another option would be a command-line program that takes arguments on the command line. Look at the argparse library for this. You might make multiple programs, like so:

popular_movies.py -- returns a table of popular movies, takes a user_id argument to filter out movies that user has seen
recommendations.py -- returns a table of recommended movies for a user
