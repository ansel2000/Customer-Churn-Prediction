from django.shortcuts import render
from joblib import dump, load
from customer_predict.models import Customer
from django.shortcuts import get_object_or_404
from keras.models import load_model 
import sklearn.preprocessing
import pickle
import sklearn
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
# from mod import create_larger1
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import sys

# our home page view
def index(request):
   
    sys.path.append('D:/customer_churn-master/')
    
    def create_larger1():
        model = Sequential()
        model.add(Dense(100, input_dim=34, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
    mod = create_larger1()
    col = load('data_files/coltrans.joblib')
    mod.load_weights('data_files/cdcnn.h5')

    
    
    if request.method == 'POST':
        pos = request.POST.get('email')
        try:
            customer = Customer.objects.filter(userid=pos).values()[0]
            customer.pop('userid')
            customer.pop('id')
            customer.pop('password')
            c = ['Tenure', 'PreferredLoginDevice', 'CityTier', 'WarehouseToHome',
        'PreferredPaymentMode', 'Gender', 'HourSpendOnApp',
        'NumberOfDeviceRegistered', 'PreferedOrderCat', 'SatisfactionScore',
        'MaritalStatus', 'NumberOfAddress', 'Complain',
        'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
        'DaySinceLastOrder', 'CashbackAmount']

            
            df = pd.DataFrame([list(customer.values())],columns=c)
           
            test = col.transform(df)
            r = mod.predict_classes(test)
            res = mod.predict(test)
           
            if r[0][0]:
                print("Probability of customer churning", res[0][0]*100,"%")
            else:
                print("Probability of customer not churning",100 - (res[0][0]*100),"%")
            print('The result of the churn is this',r[0][0])
            if r[0][0] ==1:
                print("To persuade the customer to stay give a discount coupon")
            else:
                print("Direct the customer to the main home page")

            
            context = {'result':r[0][0]}
            return render(request, 'index.html',context)
        except Exception as e:
            print(e)
            print("Exception")
            pass
    return render(request, 'index.html')

def login(request):   
    return render(request, 'login.html')

def signup(request):    
    return render(request, 'signup.html')





