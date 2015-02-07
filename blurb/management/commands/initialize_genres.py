from django.core.management import BaseCommand
import blurb.amazon_api_for_books
import blurb.utils as utils
from blurb.models import Genre

class Command(BaseCommand):
    def handle(*args, **kwargs):
        print("I am running!")
        Genre.objects.all().delete()
        # Get the information from Amazon
        dict_books = blurb.amazon_api_for_books.getBooksFromAmazon()
        # Gather into strings for each genre
        genre_dict = {}
        for genre_id in dict_books:
            list_of_tuples = dict_books[genre_id]
            genre_dict[genre_id] = utils.clean(list_of_tuples)
        # Get genre names (need function)
        # Create Genre object and add to database
        genre_names_dict = blurb.amazon_api_for_books.getGenreId_GenreName(1000)

        print genre_dict.keys()
        print genre_names_dict.keys()



        for genre_id in genre_dict.keys():

            genre_temp = Genre(
                id = genre_id,
                name = genre_names_dict[genre_id],
                title_options = genre_dict[genre_id][0],
                author_options =  genre_dict[genre_id][1],
                descr_options = genre_dict[genre_id][2],
            )
            genre_temp.save()
        print "-------------"
        print Genre.objects.all()
        print "---------------"

        """
        blurb1 = utils.generate_all(genre_dict["25"])
        print blurb1[0] +"\n"
        print blurb1[1] + "\n"
        print blurb1[2] + "\n"
        """