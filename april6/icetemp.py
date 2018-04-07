import numpy as np
import matplotlib.pyplot as plt

temp = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1]).reshape(-1,1)
ice = np.array([215,325,185,332,406,522,412,614]).reshape(-1,1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(temp,ice)

# Predicting the Test set results
y_pred = regressor.predict(temp)

# Visualising the Training set results
plt.scatter(temp, ice, color = 'red')
plt.plot(temp, regressor.predict(temp), color = 'blue')
plt.show()