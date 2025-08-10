from sklearn.linear_model import LinearRegression
import joblib

# Example training data (you can replace this with real preprocessed data)
X = [[100, 30, 80, 6.5], [90, 28, 75, 6.7]]  # rainfall, temp, nitrogen, pH
y = [2.5, 2.8]  # crop yields

model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model/trained_model.pkl')
