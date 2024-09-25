
# Meta Stock Price Prediction Model Based on Social Media Usage Age

## Project Overview

This project explores the correlation between the average age at which children start using social media and Meta's (formerly Facebook) stock price over time. The aim is to understand whether younger social media adoption correlates with stock performance and how broader market trends, such as the S&P 500, also influence Meta's stock price.

## Key Features

- **Logistic Age Model**: Models the average age of social media users over time, starting from 2010 to 2023.
- **Stock Data**: Historical stock data for Meta and the S&P 500 index is collected from Yahoo Finance.
- **OLS Regression**: A regression model is used to determine the relationship between the average age, the S&P 500 index, and Meta's stock price.
- **Analysis of Results**: The model shows a high correlation (R-squared = 0.949) between the average age and Meta's stock price, indicating that both the average age and market trends significantly influence stock performance.

## Libraries Used

- `yfinance` for stock data
- `pandas` and `numpy` for data manipulation and calculations
- `matplotlib` for visualization
- `statsmodels` for regression analysis

## Project Goals

1. Understand how the average social media adoption age affects the performance of social media company stocks.
2. Test whether broader market conditions (e.g., S&P 500 index) also impact Meta’s stock performance.
3. Provide a base for further research on social media adoption trends and stock market correlations.

## Results

- The regression analysis suggests that younger users joining social media at earlier ages correlates strongly with Meta's stock price.
- The combination of the S&P 500 index and the average age as predictors resulted in a model with a high R-squared value (94.9%), indicating a strong fit.

## Limitations

- Small dataset: The model uses only 11 observations, which may reduce the statistical power.
- Multicollinearity: Some degree of multicollinearity between predictors (e.g., age and market trends) was observed.
- Future data: It's challenging to access up-to-date data on the average age of new social media users.

## Future Work

- Extend the model to include more predictors such as Meta's user growth rate and advertising revenue.
- Perform additional backtesting with new data as it becomes available.
- Explore how other social media platforms (e.g., Snap, TikTok) correlate with younger user adoption trends.

## How to Use

1. Install the necessary dependencies:
    ```bash
    pip install yfinance pandas numpy matplotlib statsmodels
    ```

2. Run the Python script to fetch stock data and analyze the correlation:
    ```bash
    python metaagetest.py
    ```

3. The script will print the correlation and display a plot comparing the average age of social media usage with Meta’s stock price over time.

## License

This project is open-source and available under the MIT License.
