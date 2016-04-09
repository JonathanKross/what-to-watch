import csv


'''user and ratings
    user_id and user_id & ratings
    ratings and movies
    item_id = movie_id
        user_id makes ratings
        user_id in ratings
        ratings on item_id
        item_id is movie_id
    Find all ratings for a movie by id
    Find the average rating for a movie by id
    Find the name of a movie by id
    Find all ratings for a user

    View movies by highest average rating (include min rating)
    Search for a movie
'''

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

    def get_movie_title_from_id(self, movie_id):
        if self.movie_id == movie_id:
            return self.title

    # def get_ratings_for_single_movie(self, movie_dict):
    #     movie_dict[self.movie_id].ratings
    #     return


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


class Rating():
    def __init__(self, user_id, item_id, rating):
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating

    def __str__(self):
        return "User ID: {}, Item ID: {}, Rating: {}".format(self.user_id, self.item_id, self.rating)

    def __repr__(self):
        return self.__str__()

    def calc_avg_rating(ratings_attr):
        #should work to calc ratings for a user and for ratings for a movie
        # all_ratings = [dict.values() for dict in ratings_attr.values()]
        return round(float(sum(ratings_attr.values())/len(ratings_attr.values())), 2)



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
            # user_dict[int(row[0])].ratings[int(row[1])] = {'rating': int(row[2])}
            user_dict[int(row[0])].ratings[int(row[1])] = int(row[2])

            #find movie_id, add dict of user_id key dict rating
            # movie_dict[int(row[1])].ratings[int(row[0])] = {'rating': int(row[2])}
            movie_dict[int(row[1])].ratings[int(row[0])] = int(row[2])


    for movie_obj in movie_dict.values():
        movie_obj.avg_rating = Rating.calc_avg_rating(movie_obj.ratings)

    for user_obj in user_dict.values():
        user_obj.avg_rating = Rating.calc_avg_rating(user_obj.ratings)

    # def average_movie_rating(movie_dict):
    #     for movie_object in movie_dict.values():
    #         movie.avg_rating = Ratings.ave_rating(movie.ratings)





    print(movie_dict[1])




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


if __name__ == '__main__':
    main()



# with open('ml-100k/u.user') as f:
#     reader = csv.DictReader(f, fieldnames=['user_id'], delimiter='|')
#     for row in reader:
#         user_list.append(User(int(row['user_id'])))


# with open('ml-100k/u.data') as f:
#     reader = csv.DictReader(f, fieldnames=['user_id', 'item_id', 'rating'], delimiter='\t')
#     for row in reader:
#         Rating(int(row['user_id']), int(row['item_id']), int(row['rating']))


# with open('ml-100k/u.item', encoding='latin_1') as f:
#     reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title',], delimiter='|')
#     for row in reader:
#         movie_list.append(Movie(int(row['movie_id']), row['movie_title']))
