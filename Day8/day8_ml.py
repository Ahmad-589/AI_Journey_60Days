import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'price': [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)
print(df)

X = df[['area']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predicted Prices:", predictions)

plt.scatter(df['area'], df['price'], color='blue', label='Data')
plt.plot(df['area'], model.predict(df[['area']]), color='red', label='Model')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($1000)')
plt.legend()
plt.title('House Price Prediction')
plt.show()
