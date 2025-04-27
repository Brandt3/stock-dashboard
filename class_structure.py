class Stock:
    def __init__(self, da, op, hi, lo, cl, vol, sy):
        self.date = da
        self.open = op
        self.high = hi
        self.low = lo
        self.close = cl
        self.volume = vol
        self.symbol = sy

class CompanyMetaData:
    def __init__(self, sy, lare, op, tz):
        self.symbol = sy
        self.lastRefresh = lare
        self.outputSize = op
        self.timeZone = tz



