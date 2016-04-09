import csv
import os
import sys

movie_dict = {}
user_dict = {}


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

    # def get_movie_title_from_id(self, movie_id):
    #     if self.movie_id == movie_id:
    #         return self.title
    #
    # def get_ratings_for_single_movie(self, movie_dict):
    #     movie_dict[self.movie_id].ratings
    #     return

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
        #should work to calc ratings for a user and for ratings for a movie
        # all_ratings = [dict.values() for dict in ratings_attr.values()]
        return round(float(sum(ratings_attr.values())/len(ratings_attr.values())), 1)

    def get_top_rated_movies(num_of_movies, min_num_ratings):

        top_rated_movies = [movie for movie in movie_dict.values() if len(movie.ratings) >= min_num_ratings]
        return sorted(top_rated_movies, key= lambda movie: movie.avg_rating, reverse=True)[:num_of_movies]
        # top_rated_movies = []
        # for movie in movie_dict.values():
        #     if len(movie.ratings) >= min_num_ratings:
        #         top_rated_movies.append(movie)
        #
        # return sorted(top_rated_movies, key= lambda movie: movie.avg_rating, reverse=True)[:num_of_movies]

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




class User():
    def __init__(self, user_id):
        self.user_id = user_id
        self.ratings = {}
        self.avg_rating = ""

    def __str__(self):
        return "USER ID {}, Average Rating= {}, their Ratings= {}".format(self.user_id, self.avg_rating, self.ratings)

    def __repr__(self):
        return self.__str__()

    def list_user_ratings(self):
        # returns a list of user's ratings contained in a dictionary
        return self.ratings.values()


class Interface():

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def play_again():
        """Asks user if they want to play the game again."""

        play_again = input("Do you want to play again? [y/N] \n")

        if play_again.lower().strip() == "y":
            clear()
            main()

        else:
            print("Thank you. We appreciate your business.")
            sys.exit()

    def view_top_rated_movies():
        while True:
                try:
                    num_of_movies = int(input("How many movies would you like to view? "))
                    min_num_ratings = int(input("What's the minimum number of ratings? "))

                except ValueError:
                    print("That's not a number!\n")

                else:
                    Interface.clear()
                    print("RANK\tRATING\tTITLE")
                    for i, movie in enumerate(Rating.get_top_rated_movies(num_of_movies, min_num_ratings), start=1):
                        print(i, "\t", movie.avg_rating, "\t", movie.movie_title)
                    print()


def main():

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
            #find user ID, add dict of item_id key dict rating
            user_dict[int(row[0])].ratings[int(row[1])] = int(row[2])

            #find movie_id, add dict of user_id key dict rating
            movie_dict[int(row[1])].ratings[int(row[0])] = int(row[2])


    for movie_obj in movie_dict.values():
        movie_obj.avg_rating = Rating.calc_avg_rating(movie_obj.ratings)

    for user_obj in user_dict.values():
        user_obj.avg_rating = Rating.calc_avg_rating(user_obj.ratings)


    Interface.view_top_rated_movies()


    # """Find all ratings for a movie by id"""
    # print(list(movie_dict[1].ratings.values()))
    #
    # """Find the average rating for a movie by id"""
    # print(movie_dict[1].avg_rating)
    #
    # """Find the name of a movie by id"""
    # print(movie_dict[1].movie_title)
    #
    # """Find all ratings for a user"""
    # print(user_dict[1].ratings)





if __name__ == '__main__':
    main()
