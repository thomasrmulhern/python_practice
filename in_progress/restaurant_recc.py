
# names_to_rating = {
# 'Georgie Porgie': 87,
# 'Queen St. Cafe': 82,
# 'Dumplings R Us': 71,
# 'Mexican Grill': 85,
# 'Deep Fried Everything': 52
# }
#
#
# price_to_name = {
# '$': ['Queen St. Cafe, Dumplings R Us, Deep Fried Everything'],
# '$$': ['Mexican Grill'],
# '$$$': ['Georgie Porgie'],
# '$$$$': []
# }
#
#  cuisine_to_names = {
# 'Canadian': ['Georgie Porgie'],
# 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
# 'Malaysian': ['Queen St. Cafe'],
# 'Thai': ['Queen St. Cafe'],
# 'Chinese': ['Dumplings R Us'],
# 'Mexican': ['Mexican Grill']
# }


def recommend(file, price, cuisine_list):
    ''' (file open for reading, list of str) -> list of (int, str) list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in the cuisines_list. Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    '''

    #Read the file and build the data structure
    # - a dict of (restaurant: rating%)
    # - a dict of (price: list of restaurant names)
    # - a dict of (cuisine: list of restaurant names)
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for price first
    # Price: look up the list of restaurant names for the requested price.
    names_matching = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisines_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve
    # the requested cuisine. Need to look at ratings and sort this list.

    # Return the sorted list


def filter_by_cuisine(names_matching_price, cuisines_to_names, cuisines_list):
    '''(list of str, dict of (str: list of str), list of str) -> list of str

    >>> names = []
    >>> cuis = {'Canadian': ['Georgie Porgie'],
   'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
   'Malaysian': ['Queen St. Cafe'],
   'Thai': ['Queen St. Cafe'],
   'Chinese': ['Dumplings R Us'],
   'Mexican': ['Mexican Grill']}
    >>> cuisine = ['Chinese', Thai]
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    '''

def read_restaurants(file):
    '''(file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

     - a dict of (restaurant: rating%)
     - a dict of (price: list of restaurant names)
     - a dict of (cuisine: list of restaurant names)
     '''
     filename = "../data/restaurants.txt"
     file = open(filename, 'r')

     name_to_rating = {}
     price_to_names = {'$': [],'$$': [], '$$$': [], '$$$$':[]}
     cuisine_to_names = {}

     for line in file:



     return name_to_rating, price_to_names, cuisine_to_names
