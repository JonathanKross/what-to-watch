from movie_lib import *
import sys


def main():
    Interface.load()
    Interface.clear()

    while True:
        print("\n\nWelcome to the MovieLens Database \n\nMAIN MENU")
        print("""
1 - View movies by highest average rating
2 - Search for a movie by id
3 - Search for a movie by title
4 - View highest rated movies that you haven't rated yet
5 - Exit
    """)
        menu_option = int(input("Enter a number to navigate: "))

        if menu_option == 1:
            Interface.display_top_rated_movies()
        elif menu_option == 2:
            Interface.display_movie_by_id()
        elif menu_option == 3:
            Interface.display_movies_by_title()
        elif menu_option == 4:
            Interface.display_top_unrated_movies()
        else:
            sys.exit()



if __name__ == '__main__':
    main()
