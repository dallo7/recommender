import pandas as pd

# Build a Popularity filtering recommender
newDf = pd.read_csv("newDf.csv")


def popularity():
    popularity = newDf.carName.value_counts()

    top_4_items = dict(popularity.nlargest(4))

    # Initialize variables to None (or empty strings if preferred)
    car1 = None
    car2 = None
    car3 = None
    car4 = None

    # Counter variable to keep track of assigned variables
    counter = 0

    for key in top_4_items.keys():
        if counter == 0:
            car1 = key
        elif counter == 1:
            car2 = key
        elif counter == 2:
            car3 = key
        else:
            car4 = key
        counter += 1

        if counter == 4:
            break

    return [car1, car2, car3, car4]
