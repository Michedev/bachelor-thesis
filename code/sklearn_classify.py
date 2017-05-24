from functools import reduce
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


def train_model(dataset: list, model, cross_validation=True):
    """
    
    :param dataset: List of tuples (label, features).
    :param model: a model instance
    :param cross_validation: flag for cross validation
    :return: the model and the test error predictions. In case of cross validation the mean of all the errors
    """
    y, X = zip(*dataset)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = model.fit(X_train, y_train)
    test = list(zip(X_test, y_test))
    return model, test_model(model, test, cross_validation)


add = lambda a, b: a + b


def test_model(model: {'predict'}, test: list, cross_validation):

    if cross_validation:
        X_test, y_test = zip(*test)
        scores = cross_val_score(model, X_test, y_test, cv=10, scoring='accuracy')
        return 1 - scores.mean()
    else:
        predictions = [(model.predict([X_i])[0], y_i) for X_i, y_i in test]
        wrong_predictions = reduce(add, [1 for prediction, real_label in predictions if prediction != real_label], 0)
        return wrong_predictions / float(len(test))
