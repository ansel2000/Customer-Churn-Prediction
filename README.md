# Customer Churn to facilitate market using Django and CNN

#### Please go through entire readme for complete project specifications

Semster 6 Mini Project. This project aims to analyze the dataset provided containing customer data with known churn value and design a model that finds the patterns in the data using which it is able to predict the churn value for customers whose churn value is not known. This project includes an application of the predicted churn value where proactive action is take if the customer is going to churn.

This project covers the following topics

- Data Preprocessing
    * OneHotEncoding
    * Data Scaling
    * Outlier Analysis
- Machine Learning
    * Training
    * Validation
- Web apps using Django

### Resources:

-   [Miniproject presentation](https://drive.google.com/file/d/1SjQvsUjmBcz_5ujsWxm_hQYTdi5V16QU/view?usp=sharing)

## Technologies used

- Frontend - HTML, CSS, JS
- Frameworks - Django
- Machine Learning Algorithms
    * Linear Discriminant Analysis
    * Decision Tree
    * Random Forest
    * XGBoost
    * Making a Pipeline
    * CNN
-   * Package managers - pip

## Dependencies

-   [Sklearn](https://scikit-learn.org/stable/)
-   [pip](https://pip.pypa.io/en/stable/)
-   [Django](https://www.djangoproject.com/)
-   Text Editor([VS Code](https://code.visualstudio.com/))

# Get started

-   Install dependencies - `pip install -r requirements.txt`

# Dataset

[Dataset Used](https://www.kaggle.com/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)

- Description
   * The data set belongs to a leading online E-Commerce company. An online retail (E commerce) company wants to know the customers who are going to churn, so accordingly they can approach customer to offer some promos.

#### Note:

The `dataset file`, `trained model weights` and the `pipeline that does data preprocessing`.

The [Mini_Proj.ipynb](https://github.com/ansel2000/Customer-Churn-Prediction/blob/main/Mini_Proj.ipynb) file contains all the code used in cleaning the data and model validation.

## To-do

- [x] -   Data Cleaning and Pre-processing
    - [x] - Handle missing values (replacing with median value)
    - [x] - Categorical and Numeric Data Identification
    - [x] - Plotting Data Feartures (For Understanding)
    - [x] - One Hot Encoding (Nominal to Numeric conversion)
    - [x] - Data Scaling
    - [x] - Analysing the Churn by each Variable - Visualising via Graphs
- [x] -   Model Training - Repeated for different Algorithms
    - [x] - Train Model based on processed Data
    - [x] - Model Validation on Test Data
    - [x] - Model Score (Precision, recall f1-score, support)
    - [x] - Confusion Matrix
    - [x] - Model Comparison
- [x] -   Exporting Model
    - [x] - Exporting Model Weights
    - [x] - Creating Data Pipeline
- [x] -   Web Applicaion
    - [x] - Creating an Ecommerce Website Frontend
    - [x] - Loading trained model weights and Pipeline
    - [x] - Creating Database containing customer churn with unknown churn.
    - [x] - Prediction of Churn and Coupon Display on Homepage
