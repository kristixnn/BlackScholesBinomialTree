from numpy import exp,sqrt,log
from scipy.stats import norm

#TO-DO:
#add binomial tree for american options
#expand on greeks
#add pnl
#implement check for options returning dividends

class BlackScholes:
    def __init__(
        self,
        time_of_expiry : float,
        strike: float,
        spot_price: float,
        volatility: float,
        interest_rate: float,
    ):
        self.time_of_expiry = time_of_expiry
        self.strike = strike
        self.spot_price = spot_price
        self.volatility = volatility
        self.interest_rate = interest_rate
    
    def run(
        self,
    ):
        time_of_expiry = self.time_of_expiry
        strike = self.strike
        spot_price = self.spot_price
        volatility = self.volatility
        interest_rate = self.interest_rate
        
        d1 = (log(spot_price/strike)+(interest_rate+0.5*volatility**2)*time_of_expiry)/(volatility*sqrt(time_of_expiry))
        d2 = d1-volatility*sqrt(time_of_expiry)
        
        call=spot_price * norm.cdf(d1)-(strike*exp(-(interest_rate*time_of_expiry))*norm.cdf(d2))
        put=(strike*exp(-(interest_rate*time_of_expiry))*norm.cdf(-d2))-spot_price * norm.cdf(d1)
        
        self.call=call
        self.put = put
        
        self.call_delta = norm.cdf(d1)
        self.put_delta = 1-norm.cdf(d1)
        self.gamma=norm.pdf(d1)/(strike*volatility*sqrt(time_of_expiry))
        

if __name__== "__main__":
    time_of_expiry = 2
    strike = 90
    spot_price = 100
    volatility = 0.2
    interest_rate = 0.05
    BS = BlackScholes(
    time_of_expiry=time_of_expiry,
    strike = strike,
    spot_price = spot_price,
    volatility=volatility,
    interest_rate=interest_rate
    )
    BS.run()
    
