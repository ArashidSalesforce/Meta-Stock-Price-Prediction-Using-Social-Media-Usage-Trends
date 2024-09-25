import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Step 1: Logistic function to model distribution-based changes in age from 2010 to 2021
def logistic_age_change(x, L=12.5, k=-0.5, x0=2015):
    """
    Logistic function to model the drop in starting age between 2010 and 2021.
    L: Initial starting age (2010)
    k: Growth rate (controls how fast the age drops)
    x0: Midpoint of the curve (around 2015)
    """
    return L / (1 + np.exp(k * (x - x0)))

# Define the years from 2010 to 2023 and calculate the average ages
years_full = np.arange(2010, 2024)
ages_2010_2021 = logistic_age_change(years_full[:12], L=12.5, k=-0.5, x0=2015)

# Assume slower growth from 2021 to 2023, stabilizing at 11 years
ages_2021_2023 = np.linspace(8, 11, len(years_full[12:]))

# Combine the two age segments
ages = np.concatenate([ages_2010_2021, ages_2021_2023])

# Create a DataFrame for the ages
ages_df = pd.DataFrame({
    'Year': years_full,
    'Average Age': ages
})

# Download historical stock data for Meta (Facebook)
fb_stock = yf.download('META', start='2010-01-01', end='2023-01-01')

# Download broader market data (e.g., S&P 500 Index)
sp500 = yf.download('^GSPC', start='2010-01-01', end='2023-01-01')

# Resample stock and market data annually to match the available 'ages' data
fb_stock_yearly = fb_stock.resample('YE').mean()
sp500_yearly = sp500.resample('YE').mean()

# Ensure both DataFrames have matching years
fb_stock_yearly['Year'] = fb_stock_yearly.index.year
sp500_yearly['Year'] = sp500_yearly.index.year

# Merge the datasets
merged_data = pd.merge(ages_df, fb_stock_yearly[['Close', 'Year']], on='Year')
merged_data = pd.merge(merged_data, sp500_yearly[['Close', 'Year']], on='Year', suffixes=('_META', '_SP500'))

# Step 2: Build the Regression Model
X = merged_data[['Average Age', 'Close_SP500']]  # Add more explanatory variables if needed
y = merged_data['Close_META']

# Add a constant (intercept) to the model
X = sm.add_constant(X)

# Step 3: Fit the regression model
model = sm.OLS(y, X).fit()

# Step 4: Analyze the model performance
print(model.summary())

# Step 5: Plot the results
fig, ax1 = plt.subplots()

ax1.set_xlabel('Year')
ax1.set_ylabel('Average Age', color='tab:blue')
ax1.plot(merged_data['Year'], merged_data['Average Age'], color='tab:blue', label='Average Age')

ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Meta Stock Price', color='tab:green')  # Set the right y-axis
ax2.plot(merged_data['Year'], merged_data['Close_META'], color='tab:green', label='Meta Stock Price')

plt.title('Relationship between Average Age of Social Media Adoption, Market Trends, and Meta Stock Price')
plt.show()
