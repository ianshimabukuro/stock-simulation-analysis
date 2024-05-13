import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm


def find_mode_of_skewnorm(alpha, loc, scale):
    # Calculate the mode of the skewed normal distribution
    delta = alpha / np.sqrt(1 + alpha ** 2)
    mode = loc + delta * scale
    return mode


def generate_stock_price_distribution(current_price, intrinsic_value):
    # Define the range for plotting
    x_range = np.linspace(min(current_price, intrinsic_value) - 50, max(current_price, intrinsic_value) + 50, 1000)

    # Set sigma as 5% of the peak value
    sigma_current = 0.05 * current_price
    sigma_intrinsic = 0.05 * intrinsic_value

    # Fixed skewness factor, ensuring tails meet
    skew_adj = 4  # Constant skew to maintain shape consistency

    # Determine skew directions based on the relationship between current price and intrinsic value
    if current_price > intrinsic_value:
        skew_current = -skew_adj  # Negative skew for current price
        skew_intrinsic = skew_adj  # Positive skew for intrinsic value
    else:
        skew_current = skew_adj  # Positive skew for current price
        skew_intrinsic = -skew_adj  # Negative skew for intrinsic value

    # Generate initial skewed Gaussian distributions with no location adjustment
    initial_skewed_current = skewnorm(alpha=skew_current, loc=current_price, scale=sigma_current)
    initial_skewed_intrinsic = skewnorm(alpha=skew_intrinsic, loc=intrinsic_value, scale=sigma_intrinsic)

    # Find the modes of these distributions
    mode_current = find_mode_of_skewnorm(skew_current, current_price, sigma_current)
    mode_intrinsic = find_mode_of_skewnorm(skew_intrinsic, intrinsic_value, sigma_intrinsic)

    # Calculate location adjustments to align peaks exactly at the specified values
    loc_adj_current = current_price - mode_current
    loc_adj_intrinsic = intrinsic_value - mode_intrinsic

    # Generate the adjusted skewed Gaussian distributions
    skewed_current = skewnorm.pdf(x_range, skew_current, loc=current_price + loc_adj_current, scale=sigma_current)
    skewed_intrinsic = skewnorm.pdf(x_range, skew_intrinsic, loc=intrinsic_value + loc_adj_intrinsic,
                                    scale=sigma_intrinsic) * 0.05

    # Combine the distributions
    combined_distribution = skewed_current + skewed_intrinsic

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(x_range, skewed_current, label='Adjusted Skewed Current Stock Price', linestyle='dashed')
    plt.plot(x_range, skewed_intrinsic, label='Adjusted Skewed Intrinsic Value', linestyle='dashed')
    plt.plot(x_range, combined_distribution, label='Combined Skewed Distributions', color='red')
    plt.fill_between(x_range, combined_distribution, color='red', alpha=0.3)
    plt.title('Stock Price Evaluation Distribution')
    plt.xlabel('Stock Price')
    plt.ylabel('Probability Density')
    plt.axvline(x=current_price, color='red', linestyle='--', label='Current Stock Price')
    plt.axvline(x=intrinsic_value, color='green', linestyle='--', label='Intrinsic Value')
    plt.legend()
    plt.grid(True)
    plt.show()


# Parameters
current_stock_price = 100  # Current stock price
intrinsic_value = 120  # Intrinsic value

# Generate and visualize the distribution
generate_stock_price_distribution(current_stock_price, intrinsic_value)
