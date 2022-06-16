# pip install scikit-learn
import numpy as np
from sklearn.datasets import load_iris, load_wine

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

for ds_name, load_ds in [("iris", load_iris), ("wine", load_wine)]:
    print("DATASET:", ds_name)
    X, y = load_ds(return_X_y=True)
    # X features matrix
    # y target/labels vector
    print("features X:", X.shape, X.dtype)  # 150 samples, 4 attributes
    print("labels y:", y.shape, y.dtype)
    classes, counts = np.unique(y, return_counts=True)
    print("classes:", classes, counts)  # 50 of each class
    print()

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    for name, clf in [
        ("decision tree", DecisionTreeClassifier()),
        ("support vector machine", SVC()),
        ("k nearest neighbors", KNeighborsClassifier()),
        ("gaussian naive bayes", GaussianNB()),
    ]:
        # fit classifier to training data
        clf.fit(X_train, y_train)
        # evaluate classifier on test data
        y_pred = clf.predict(X_test)
        print(f"{name:24} accuracy:", (y_pred == y_test).mean())
    print()
