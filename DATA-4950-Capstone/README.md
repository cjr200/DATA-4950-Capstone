4950_Capstone
==============================

Predicting Tech Salaries with Predictive Modeling
	When people apply to jobs, the first aspect of the job posting most people would look at would be the salary. Some employers may have difficulty 
to decide the salary range for a job posting. There are many factors to consider for a salary such as job rank, title, and skills required to do the job 
correctly. This is where predictive modeling could help employers decide an adequate salary range. With the right features and model, predictive modeling 
could predict the salary for any position.
	The data used for this project comes from a 2016 survey that asks participants in the tech industry for information about their job. An initial 
exploratory data analysis was then conducted on the data, which found that many of the features had missing data. If there was 20% or less of the data 
missing, I imputed the missing values. If it was any more than that, the column will be dropped. Due to the data being collected from a survey, some of 
the records were not realistic. Some entries had salaries in the millions, these outliers would greatly impact the model results. To keep the model tuned 
to more realistic standards, I dropped any records with salaries more than a million dollars. One insight I gained through the eda is that the signing 
bonus and annual salary are correlated. This could mean the higher the salary, the higher the signing bonus.
	The two models used for this project are linear regression and boosted gradient regression tree. The linear regression model is a simple but 
effective predictive model. The regression model requires a quantitative target variable and at least one independent variable. The model will then 
calculate the linear equation with the smallest number of residuals. If the independent variable does not explain the dependent variable well, then the 
model will have poor results. The gradient boosted regressor is a more complicated model. This model has a similar goal to the regression model, minimize 
the size of the residuals. Gradient boosted regressors are based on decision trees, which represents the model as an upside-down tree which branches into 
different subtrees. The leaves at the end of the tree represent a classification of the data based on the path down the tree. The gradient boosted tree 
builds upon the decision tree by training multiple iterations of itself. The model will continue to train itself until it has reached the best model 
results it can. I chose these models due to my dependent variable, salary, being a quantitative variable. Linear regression is an effective model and I 
wanted to test the gradient boosted tree to see how they compare.
	The primary model performance measures I used are r squared and mean squared error. The r squared shows how much the independent variable 
explains the variability in the dependent variable. The mean square error is the average of the squared errors or residuals. For the linear regression, 
the model had an r squared of 0.03 and test mse of 63,608.64. These results are not favorable, the model doesn’t predict the data well. The gradient 
boosted tree had a r squared of .39 and test mse of 13,061. These results are much better than the linear regression, but the results are still too low 
to reliably use to predict the salary. The model I would choose for the best results would be the gradient boosted tree. While the results are not 
favorable, they are far better than the results of the linear regression.
	With a bigger and more complete data set, the models used in this project would have more data to train on and become more accurate. In a 
business setting, the linear regression model would be a better choice. It is easier to explain to stakeholders and with the right data will provide 
accurate results. The gradient boosted tree is a good model but hard to understand and explain. The performance measures used, r squared and mse, are 
understandable and summarize the model well. Performance measures are important for gauging how well the model performs. Without them, it would be hard 
to measure the accuracy of these models. If I were to redo this project, I would pick a bigger and more complete data set. Web scrapping job postings and 
putting the results in a csv would be a great way to get the data required for this project.


Data set link: https://www.kaggle.com/datasets/thedevastator/know-your-worth-tech-salaries-in-2016 
gradient boosted regressor source: https://blog.paperspace.com/implementing-gradient-boosting-regression-python/#:~:text=Gradient%20boosting%20Regression%20calculates%20the,maps%20features%20to%20that%20residual. 



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
