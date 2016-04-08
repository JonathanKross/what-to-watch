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

# movie_list = []
# user_list = []
# rating_list = []
movie_dict = {}
user_dict = {}
rating_dict = {}


class Movie():
    def __init__(self, movie_id, movie_title):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.ratings = {}


    def __str__(self):
        # return "Movie ID: Movie Title: {}, Ratings= {}".format(self.movie_id, self.movie_title, self.ratings)
        return "{} OBJECT, Ratings= {}".format(self.movie_title, self.ratings)


    def __repr__(self):
        return self.__str__()

class User():
    def __init__(self, user_id):
        self.user_id = user_id
        self.ratings = {}

    def __str__(self):
        return "Ratings= {}".format(self.ratings)

    def __repr__(self):
        return self.__str__()


class Rating():
    def __init__(self, user_id, item_id, rating):
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating

    def __str__(self):
        return "User ID: {}, Item ID: {}, Rating: {}".format(self.user_id, self.item_id, self.rating)

    def __repr__(self):
        return self.__str__()


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
        user_dict[int(row[0])].ratings[int(row[1])] = {'rating': int(row[2])}
        #find movie_id, add dict of user_id key dict rating
        movie_dict[int(row[1])].ratings[int(row[0])] = {'rating': int(row[2])}


print(movie_dict)
# print(user_dict)






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

def main():
    pass

if __name__ == '__main__':
    main()
