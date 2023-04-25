import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error

# trains and test linear regression
class linearModel:
    # builds intial model
    def buildModel(X_train, X_test, y_train, y_test):
        # builds model with backward selection applied
        X_reg = X_train
        X_reg = X_reg.drop(['job_category_Data','job_category_Applied Science','job_category_Operations','job_category_Web','job_category_Engineering'],axis=1)
        X_reg = sm.add_constant(X_reg) 
        
        reg1 = sm.OLS(y_train, X_reg).fit()
        reg1.save("../models/salary_regression.pkl")

        # Create a list of statistically significant variables to use for the final model
        results = reg.params.reset_index()
        results = pd.DataFrame(results)
        stat_sig_Pred = results['index'].values
        display(stat_sig_Pred)
        stat_sig_Pred = np.delete(stat_sig_Pred, 0)
        return stat_sig_Pred

    # tests model and outputs results
    def testModel(X_train, X_test, y_train, y_test,stat_sig_Pred):
        # Final model
        X_reg = X_train
        X_train_new = X_reg[stat_sig_Pred]
        X_train_new = sm.add_constant(X_train_new)

        reg2 = sm.OLS(y_train, X_train_new).fit()
        # Predict on the test data
        X_test_new = X_test[stat_sig_Pred] 
        X_test_new = sm.add_constant(X_test_new)


        # Calculate the estimated y values using the test dataset
        y_hat_test = reg2.predict(X_test_new)

        # output results
        test_mse = mean_squared_error(y_test, y_hat_test)
        test_rmse = np.sqrt(test_mse)
        test_mae = mean_absolute_error(y_test, y_hat_test)
        test_r_squared = r2_score(y_test, y_hat_test)
        test_mape = mean_absolute_percentage_error(y_test, y_hat_test)

        print(f'The test RMSE is:\t{round(test_rmse, 2)}')
        print(f'The test MAE is:\t{round(test_mae, 2)}')
        print(f'The test Rsquared is:\t{round(test_r_squared, 3)}')
        print(f'The test MAPE is:\t{round(test_mape, 2)}')
        

        
        