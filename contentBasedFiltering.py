import pandas as pd

df1 = pd.read_csv("newDfForTraining.csv")


def recommend_cars(car_name, data=df1):
    df = data
    correlation_matrix = df.corr()

    recommended_cars = set()  # Use a set to store unique recommended cars

    # Get initial recommendations, excluding the input car
    recommendations = correlation_matrix[car_name].sort_values(ascending=False)[1:5]
    recommendations = recommendations[recommendations.index.str.startswith("carName_")]
    # print(recommendations)

    # Add unique recommendations to the set
    for car in recommendations.index:
        recommended_cars.add(car)

    # Fill in with more recommendations if needed, ensuring uniqueness
    while len(recommended_cars) < 4:
        top_correlations = correlation_matrix[car_name].sort_values(ascending=False)[1:]
        for car in top_correlations.index:
            if car not in recommended_cars and car.startswith("carName_"):
                recommended_cars.add(car)
            if len(recommended_cars) == 4:
                break
    loop = pd.Series(list(recommended_cars))
    test = []
    for i in list(loop):
        test.append(i.replace("carName_", ""))

    return test
