# monte-carlo-exotic-options
Simulation for predicting return on exotic option pricing (Asian and Barrier) using monte-carlo method.

# Personal Goals
  - Show an understanding of financial markets using real-world data
  - Program kernels to show understanding of GPU acceleration

## Inputs and Outputs
The user has a few different inputs they must select:
  - Ticker: String - A symbol used to identify the asset being traded
  - Call: Select based on whether to simulate against the asset price increasing or decreasing over time, respectively (Bool: True -> Call, False -> Put)
  - Strike Price: The price at which the asset is purchased at (Int)
  - T: The number of days before the option expires (Int)
  - N: The number of simulations run (Int)
  - Option Type: Either Asian or Barrier to simulate both exotic options (string)
  - Accelerated: Either True or False to determine whether GPU Parallelization is activated (Bool)

A few different outputs are returned:
  - Probability of profit: a percentage indicating the probability of making money based on the monte-carlo simulations
  - Time: the number of seconds to compute the simulation
  - Graph of simulation: A graph showing 20 random simulations

## How it Works:
The Monte Carlo simulation will essentially make the asset take a "step" every day. The valuation of the asset will either move up or down based on a random sample of the daily change the asset has experienced in the past two years. I've decided to use real world data instead of estimating the motion of assets (in methods like Geometric Brownian Motion) to simulate real-world fluctuation/randomness.