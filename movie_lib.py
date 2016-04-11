import csv
import os


movie_dict = {}
user_dict = {}


class Interface():

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def display_top_rated_movies():
            try:
                num_of_movies = int(input("How many movies would you like to view? "))
                min_num_ratings = int(input("What's the minimum number of ratings? "))

            except ValueError:
                print("That's not a number!\n")

            else:
                Interface.clear()
                print("RANK\tRATING\tTITLE")
                for i, movie in enumerate(Rating.list_top_rated_movies(num_of_movies, min_num_ratings), start=1):
                    print(i, "\t", movie.avg_rating, "\t", movie.movie_title)

    def display_movie_by_id():
        id_num = int(input("Enter a movie id: "))
        print("ID\tRATING\tTITLE")
        print(movie_dict[id_num].movie_id, '\t', movie_dict[id_num].avg_rating, '\t', movie_dict[id_num].movie_title)


    def display_movies_by_title():
        """Find all movies by words in the movie title"""
        title = input("Enter all or part of a movie title: ").title()
        print("ID\tRATING\tTITLE")
        for movie in movie_dict.values():
            if title in movie.movie_title:
                print(movie.movie_id, '\t', movie.avg_rating, '\t', movie.movie_title)

    def display_top_unrated_movies():
        user_id = int(input("What is your user id? "))
        num_of_movies = int(input("How many movies that you haven't rated yet would you like to see? "))
        min_num_ratings = int(input("How many minimum number of ratings should your top unrated movies have? "))

        unrated_movies = Rating.list_top_unrated_movies(user_id, num_of_movies, min_num_ratings)
        print("RANK\tRATING\tTITLE")
        for movie in enumerate(unrated_movies, start=1):
            print(movie[0], "\t", movie[1][1], "\t", movie[1][2])

    def load():

        with open('ml-100k/u.user') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                user_dict[int(row[0])] = User(user_id=row[0])


        with open('ml-100k/u.item', encoding='latin_1') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                movie_dict[int(row[0])] = Movie(movie_id=row[0],
                                       movie_title=row[1])

        with open('ml-100k/u.data') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                """Adds a dictionary of movie ratings to each User object. key = movie_id"""
                user_dict[int(row[0])].ratings[int(row[1])] = int(row[2])

                """Adds a dictionary of movie ratings to each Movie object. key = user_id"""
                movie_dict[int(row[1])].ratings[int(row[0])] = int(row[2])

        """Adds average movie rating as an attribute to each Movie object"""
        for movie_obj in movie_dict.values():
            movie_obj.avg_rating = Rating.calc_avg_rating(movie_obj.ratings)

        """Adds average movie rating as an attribute to each User object"""
        for user_obj in user_dict.values():
            user_obj.avg_rating = Rating.calc_avg_rating(user_obj.ratings)


class Movie():

    def __init__(self, movie_id, movie_title):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.ratings = {}
        self.avg_rating = ""


    def __str__(self):
        return "{}, Average Rating= {} Ratings= {}".format(self.movie_title, self.avg_rating, self.ratings)


    def __repr__(self):
        return self.__str__()

    def search_movie_by_id(id):
        """Find a movie title by searching with the movie id"""

        return movie_dict[id].movie_title

    def search_movies_by_title(title):
        """Find all movies by words in the movie title"""

        searched_movies = []
        for movie in movie_dict.values():
            if title in movie.movie_title:
                searched_movies.append(movie.movie_title)
                return searched_movies


class Rating():

    # def __init__(self, user_id, item_id, rating):
    #     self.user_id = user_id
    #     self.item_id = item_id
    #     self.rating = rating

    # def __str__(self):
    #     return "User ID: {}, Item ID: {}, Rating: {}".format(self.user_id, self.item_id, self.rating)
    #
    # def __repr__(self):
    #     return self.__str__()

    def calc_avg_rating(ratings_attr):

        return round(float(sum(ratings_attr.values())/len(ratings_attr.values())), 1)

    def search_ratings_by_movie_id(id):
        """Find all ratings for a movie by id"""

        return list(movie_dict[id].ratings.values())

    def search_ratings_by_user_id(id):
        """Find all ratings for a user"""

        return user_dict[id].ratings


    def list_top_rated_movies(num_of_movies, min_num_ratings):

        top_rated_movies = [movie for movie in movie_dict.values() if len(movie.ratings) >= min_num_ratings]
        return sorted(top_rated_movies, key= lambda movie: movie.avg_rating, reverse=True)[:num_of_movies]
        # top_rated_movies = []
        # for movie in movie_dict.values():
        #     if len(movie.ratings) >= min_num_ratings:
        #         top_rated_movies.append(movie)
        #
        # return sorted(top_rated_movies, key= lambda movie: movie.avg_rating, reverse=True)[:num_of_movies]

    def list_top_unrated_movies(user_id, num_of_movies, min_num_ratings):
        rated_movies = user_dict[user_id].ratings.keys()
        top_unrated_movies = []

        for k in movie_dict.keys():
            if k not in rated_movies and len(movie_dict[k].ratings) >= (min_num_ratings):
                top_unrated_movies.append([movie_dict[k].movie_id, movie_dict[k].avg_rating, movie_dict[k].movie_title])

        return sorted(top_unrated_movies, reverse=True, key=lambda m: m[1])[:num_of_movies]


    def euclidean_distance(list_1, list_2):
        """Given two lists, give the Euclidean distance between them on a scale
        of 0 to 1. 1 means the two lists are identical.
        """

        # Guard against empty lists.
        if len(v) is 0:
            return 0

        # Note that this is the same as vector subtraction.
        differences = [list_1[idx] - list_2[idx] for idx in range(len(v))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)

        return 1 / (1 + ((sum_of_squares) ** 0.05))


class User():
    def __init__(self, user_id):
        self.user_id = user_id
        self.ratings = {}
        self.avg_rating = ""

    def __str__(self):
        return "USER ID {}, Average Rating= {}, their Ratings= {}".format(self.user_id, self.avg_rating, self.ratings)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    main()
