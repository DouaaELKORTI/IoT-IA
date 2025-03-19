from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(X, y):
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, '../models/rf_model.pkl')
    return model
