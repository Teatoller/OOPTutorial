# movingAveragerfn.py
class MovingAverage():

    def __init__(self, symbol, bars, short_window, long_window):
        self.symbol = symbol
        self.bars = bars
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = 0.0

        signals['short_mavg'] = bars['Close'].rolling(
            window=self.short_window, min_periods=1, center=False).mean()
        signals['long_mavg'] = bars['Close'].rolling(
            window=self.long_window, min_periods=1, center=False).mean()

        signals['signal'][self.short_window:] = np.where(
            signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0)

        signals['positions'] = signals['signal'].diff()

# Example 1 to instantiate
apple = MovingAverage('aapl', aapl, 40, 100)
print(apple.generate_signals())

# Example2
microsoft = MovingAverage('msft', msft, 40, 100)
print(microsoft.generate_signals())
