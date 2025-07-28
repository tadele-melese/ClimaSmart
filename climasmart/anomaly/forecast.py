
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler

class LSTMForecaster(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2, output_size=1):
        super(LSTMForecaster, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        out = self.fc(lstm_out[:, -1, :])
        return out

def forecast_lstm(series, n_input=12, n_forecast=6, epochs=100):
    scaler = MinMaxScaler()
    series_scaled = scaler.fit_transform(series.values.reshape(-1, 1))

    X, y = [], []
    for i in range(len(series_scaled) - n_input):
        X.append(series_scaled[i:i+n_input])
        y.append(series_scaled[i+n_input])
    X, y = np.array(X), np.array(y)

    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32)

    model = LSTMForecaster()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(epochs):
        model.train()
        output = model(X_tensor)
        loss = criterion(output, y_tensor)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    forecast_input = torch.tensor(series_scaled[-n_input:], dtype=torch.float32).unsqueeze(0)
    model.eval()
    forecast = []
    for _ in range(n_forecast):
        pred = model(forecast_input)
        forecast.append(pred.item())
        new_input = torch.cat((forecast_input[:, 1:, :], pred.unsqueeze(0).unsqueeze(2)), dim=1)
        forecast_input = new_input

    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1)).flatten()
    return pd.Series(forecast, index=pd.date_range(start=series.index[-1]+pd.Timedelta("30D"), periods=n_forecast, freq='M'))
