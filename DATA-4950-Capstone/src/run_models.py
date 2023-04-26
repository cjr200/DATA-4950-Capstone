import pandas as pd
from data.make_dataset import makeData
from models.linear_reg import linearModel
from models.gradient_tree import boostedTree

# load data and prepare it for model building
df = makeData.load_data("salaries_clean.csv")
df = makeData.clean_data(df)
X_train, X_test, y_train, y_test = makeData.splitTrain(df)

# build linear regression
linear_pred = linearModel.buildModel(X_train, X_test, y_train, y_test)
# predict on test data and output results
print('Regression Results:')
linearModel.testModel(X_train, X_test, y_train, y_test, linear_pred)


# build gradient boosted regressor
tree_pred = boostedTree.build_tree(X_train, X_test, y_train, y_test)
# predict on test data and output results
print('\n Boosted Tree Results:')
boostedTree.test_out(X_test, y_test, tree_pred)
