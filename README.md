# Stock simulation

## Strategy
The current simulation is composed of a uniform time step evolution in which at every time step, the program iterates through all investors, which stochastically produce actions.
## Stages of Each Individual Iteration
1. Evaluation
2. Action Decision
3. Action
### Evaluation
In the evaluation phase, the investor will look at the market and ,while utilizing his own memory and intelligence, assess what he thinks the stocks intrinsic values are. 
With this value now stored which we call **eval** , he will derive three values: Buying, Selling and Holding probabilities.
These values are drawn from a sigmoid functions which relate the difference between **eval** and the current market price. 
The buy sigmoid with parameters kb and xb, the sell sigmoid with parameters ks and xs.
The hold distribution is just the 1-buy_sigmoid-sell_sigmoid
<img width="1436" alt="Screenshot 2024-05-22 at 17 18 37" src="https://github.com/ianshimabukuro/stock_analysis/assets/140802890/791f8420-db61-4ff5-82e8-f0c21d0086fd">
With this all values are normalized.
However there are a couple combinations of xs,xb,ks,kb that cause the hold distribution to have negative values. I have not yet figured out the relation and limits of those, so for now
it is better to just plot it and eye-ball it.
The x parameters are simply alignment parameters for the functions and the k parameters control the stepness of the sigmoids.
### Action Decision
In the action decision phase, the investor will decide to buy, sell or hold based on the previosuly adquired probabilities
