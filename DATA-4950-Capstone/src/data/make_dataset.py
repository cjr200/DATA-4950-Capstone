import pandas as pd

# class to load, clean, and split data
class makeData:
    # loads data set
    def load_data(file: str):
        fileName = "../data/external/" + file
        dataSet = pd.read_csv(fileName, sep=" ",header=None)
        return dataSet

    # cleans the data set
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        #drop the outliers
        df = df[df.annual_base_pay < 1000000]
        # drop the outliers
        df = df[df.annual_base_pay < 1000000]
        # drop unneccessary variables
        df = df.drop(["index","salary_id","location_latitude","location_longitude","comments","submitted_at"],axis=1)
        # job_title_rank, location_state, and location_country have too many missing values so they will be dropped
        df = df.drop(['job_title_rank','location_state','location_country'],axis=1)
        # drops employer experience years
        df = df.drop("employer_experience_years",axis=1)
        # drops columns with too many unique values
        df = df.drop("employer_name",axis=1)
        df = df.drop("job_title",axis=1)
        df = df.drop("location_name",axis=1) 
        # fill experience missing values with the mean
        df.loc[:, "total_experience_years"] = df.loc[:, "total_experience_years"].fillna(df["total_experience_years"].mean())
        df.loc[:, "annual_base_pay"] = df.loc[:, "annual_base_pay"].fillna(df["annual_base_pay"].mean())
        df.loc[:, "signing_bonus"] = df.loc[:, "signing_bonus"].fillna(method='ffill')
        df.loc[:, "annual_bonus"] = df.loc[:, "annual_bonus"].fillna(method='ffill')
        # stock bonus is a string so will be dropping it
        df = df.drop("stock_value_bonus",axis=1)
        # creates dummy variables for job category
        dummies = pd.get_dummies(df['job_title_category'], prefix='job_category')
        # merges dummy variables with dataframe and drops original column
        df = pd.concat([df, dummies], axis=1)
        df = df.drop('job_title_category', axis=1)
        return df

    # splits data into training and test sets
    def splitTrain(df: pd.DataFrame) -> pd.DataFrame:
        # seperates features into x and y variables
        X = df.drop('annual_base_pay', axis = 1)

        y = df['annual_base_pay'] 

        # splits data into 70% training and 30% test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
        return X_train, X_test, y_train, y_test
        