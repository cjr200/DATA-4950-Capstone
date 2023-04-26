import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class boostedTree:
    # trains regressor, returns prediction
    def build_tree(X_train, X_test, y_train, y_test):
        reg = GradientBoostingRegressor(random_state=0)
        reg.fit(X_train, y_train)
        pred_val = reg.predict(X_test)
        return pred_val

    # predicts on test data and outputs results
    def test_out(X_test, y_test, pred_val):
        test_mse = mean_squared_error(y_test, pred_val)
        print(f'The test MSE is:\t{round(test_mse)}')
        test_r_squared = r2_score(y_test, pred_val)
        print(f'The test Rsquared is:\t{round(test_r_squared, 3)}')

