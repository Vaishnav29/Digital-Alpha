import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
from scipy import stats
import statsmodels.api as sm
from sklearn import metrics
from sklearn import preprocessing
from IPython import get_ipython
import matplotlib.pyplot as plt 
plt.rc("font", size=25)
#from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data = pd.read_csv('adult11.csv',header=0)
data = data.dropna()
print(data.shape)
data=data.replace(' ?',np.nan)
data=data.replace(' <=50K',0)
data=data.replace(' >50K',1)
data = data.dropna()
#data = data.drop(data.occupation==' ?',axis=0)
print(data.shape)
print(data.columns)




get_ipython().run_line_magic('matplotlib','inline')
pd.crosstab(data['education-num'],data.prediction).plot(kind='bar')
plt.title('salary prediction')
plt.xlabel('education-num')
plt.ylabel('Salary frequency')
plt.savefig('purchase_fre_job')


pd.crosstab(data['occupation'],data.prediction).plot(kind='bar')
plt.title('salary prediction')
plt.xlabel('education-num')
plt.ylabel('Salary frequency')
plt.savefig('purchase_fre_job')

pd.crosstab(data['race'],data.prediction).plot(kind='bar')
plt.title('salary prediction')
plt.xlabel('education-num')
plt.ylabel('Salary frequency')
plt.savefig('purchase_fre_job')


pd.crosstab(data['workclass'],data.prediction).plot(kind='bar')
plt.title('salary prediction')
plt.xlabel('education-num')
plt.ylabel('Salary frequency')
plt.savefig('purchase_fre_job')


pd.crosstab(data['relationship'],data.prediction).plot(kind='bar')
plt.title('salary prediction')
plt.xlabel('education-num')
plt.ylabel('Salary frequency')
plt.savefig('purchase_fre_job')

cat_vars=['workclass', 'education','marital-status', 'occupation', 'relationship', 'race', 'sex',
       'native-country']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1
cat_vars=['workclass', 'education','marital-status', 'occupation', 'relationship', 'race', 'sex',
       'native-country']
data_vars=data.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]

data_final=data[to_keep]
data_final.columns.values
data_final_vars=data_final.columns.values.tolist()
X=[i for i in data_final_vars if i not in 'prediction']
print(X)
print(len(X))


logreg = LogisticRegression()
rfe = RFE(logreg, 18)
rfe = rfe.fit(data_final[X], data_final['prediction'])
print(rfe.support_)
print(rfe.ranking_)
cols=[]
for i in range(104):
    if rfe.support_[i] == True:
        cols.append(data_final_vars[i])
print(cols)    

X=data_final[cols]
y=data_final['prediction'] 
print(y)
print(X)





stats.chisqprob=lambda  chisq, df:stats.chi2.sf(chisq,df)

logit_model=sm.Logit(y.astype(float),X.astype(float))
result=logit_model.fit()
print(result)
#print(result.summary())




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)



y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))






kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))






confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)






print(classification_report(y_test, y_pred))




logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()




