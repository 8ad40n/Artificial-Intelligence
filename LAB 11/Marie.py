#Marie


p_rain_yearly = 5 / 365  
p_correct_given_rain = 0.9  
p_incorrect_given_no_rain = 0.1  

p_forecast_rain = p_rain_yearly * p_correct_given_rain + (1 - p_rain_yearly) * p_incorrect_given_no_rain

p_rain_given_forecast = (p_correct_given_rain * p_rain_yearly) / p_forecast_rain

print("Probability that it will rain on Marie's wedding day using Bayes' theorem:", p_rain_given_forecast)



