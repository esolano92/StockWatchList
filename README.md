# StockWatchList

StockWatchList is a serverless CRUD application built with Flask and DynamoDB that allows users to manage a watchlist of stocks. Users can add stocks by symbol and desired price, update or delete them, and receive notifications when a stock reaches the desired price.

## Features

- **Add Stocks**: Add a new stock to the watchlist with a desired price.
- **Update Stocks**: Update stock details in the watchlist.
- **Delete Stocks**: Remove stocks from the watchlist.
- **Notifications**: Get notified when a stock reaches the desired price.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8**: Make sure Python 3.8 is installed.
- **AWS CLI**: Install and configure AWS Command Line Interface.
- **Serverless Framework**: Install Node.js and NPM, then install Serverless Framework globally.
- **Docker**: Install Docker for containerization.
- **Anaconda**: Install Anaconda for managing Python environments.
- **AWS Account**: Set up an AWS account for deploying serverless functions.

## Installation

To set up the project on your local machine, follow these steps:

<details>
  <summary>Click to expand the setup instructions</summary>

```bash
# Clone the repository
git clone https://github.com/yourusername/StockWatchList.git
cd StockWatchList

# Set up the Conda environment
conda create --name stockwatchlist python=3.8
conda activate stockwatchlist

# Install Python dependencies
pip install -r requirements.txt

# Install Serverless Framework (if not already installed)
npm install -g serverless

# Deploy the Serverless Application
serverless deploy

# (Optional) Remove the Serverless Application
serverless remove
