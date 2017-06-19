#before each hyper param there is 'estimator__' because OneVsRest classifier
h_params_knn = {'estimator__n_neighbors': range(5,61,2)}
knn = KNeighborsClassifier()
#Incapsulation of knn model into OneVsOneClassifier is necessary to multiclass prediction
multiclass_knn = OneVsOneClassifier(knn)
grid_src_knn = GridSearchCV(multiclass_knn, h_params_knn, cv=5, scoring='accuracy')

grid_src_knn.fit(X_train, y_train)

#Now grid_src_knn.best_params_ contains the n_neightbors to maximize the accuracy

best_params_knn = {k[len('estimator__'):]:v for k,v in grid_src_knn.best_params_.items()}

knn_val = KNeighborsClassifier(**best_params_knn)
knn = KNeighborsClassifier()
multiclass_knn = OneVsRestClassifier(knn)
multiclass_knn_val = OneVsRestClassifier(knn_val)
multiclass_knn.fit(X_train, y_train)
multiclass_knn_val.fit(X_train, y_train)

predictions_knn = multiclass_knn.predict(X_test)
predictions_knn_val = multiclass_knn_val.predict(X_test)

accuracy_knn = np.sum(predictions_knn == y_test) / len(y_test)
accuracy_knn_val = np.sum(predictions_knn_val == y_test) / len(y_test)
