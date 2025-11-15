import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# تحميل البيانات
df = pd.read_csv("car_prices.csv")

# عرض أول 5 صفوف
print("First 5 rows of the dataset:")
print(df.head())

# معلومات وإحصائيات عن البيانات
print("\nDataset info:")
print(df.info())
print("\nDataset statistics:")
print(df.describe())

# اختيار الميزات والهدف
X = df[['year', 'mileage']]  # الميزات
y = df['price']              # الهدف

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تدريب نموذج الانحدار الخطي
model = LinearRegression()
model.fit(X_train, y_train)

# التنبؤ على بيانات الاختبار
y_pred = model.predict(X_test)

# تقييم النموذج
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nModel evaluation:")
print(f"MSE = {mse}")
print(f"R² = {r2}")

# رسم النتائج
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Car Prices")
plt.show()

# تجربة نموذج على سيارة جديدة
new_car = pd.DataFrame({'year':[2020], 'mileage':[15000]})
predicted_price = model.predict(new_car)
print(f"\nPredicted price for the new car: {predicted_price[0]:.2f}")
