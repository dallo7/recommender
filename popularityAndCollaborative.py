import popularity
import contentBasedFiltering
import random


def popularCollabo(carname):
    popular = popularity.popularity()
    collabo = contentBasedFiltering.recommend_cars(carname)
    popularcollborative = popular + collabo
    random.shuffle(popularcollborative)
    popularcollborative = popularcollborative[:4]
    return popularcollborative

