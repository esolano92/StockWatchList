# Configure logging
logging.basicConfig(level=logging.INFO, filename="app.log", format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure Dynanodb
dynamodb = boto3.resource('dynamodb', region_name="us-east-1" )
table = dynamodb.Table("StockWatchList")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            if 'add_stock' in request.form:
                symbol = request.form.get('symbol')
                desired_price = Decimal(request.form.get('desired_price'))
                
                # Add Stock log
                logger.info(f"Attempting to add stock: {symbol} with desired price: {desired_price}")

                # Fetch current stock price using yfinance
                stock = yf.Ticker(symbol)
                hist = stock.history(period="1d")
                
                # Extract current price if available
                if not hist.empty:
                    current_price = round(Decimal(hist["Close"].iloc[0]), 2)
                    
                    # Save stock to DynamoDB
                    table.put_item(
                        Item={
                            'Symbol': symbol,
                            'current_price': current_price,
                            'desired_price': desired_price
                        }
                    )
                    # Add Stock success log
                    logger.info(f"Stock {symbol} added successfully with current price: {current_price}")
                else:
                    # Stock not available log
                    logger.warning(f"Stock data not available for symbol: {symbol}")
                    return jsonify({"error":"Stock data not available."}), 400

            elif 'remove_stock' in request.form:
                symbol = request.form.get('symbol_to_remove')
                
                # Remove Stock log
                logger.info(f"Attempting to remove stock: {symbol}")
                # Delete stock from DynamoDB
                table.delete_item(
                    Key={
                        'Symbol': symbol
                    }
                )

                # Remove Stock successful
                logger.info(f"Stock {symbol} removed successfully.")

    # Log for stocks fetch 
    logger.info("Fetching stocks from DynamoDB.") 

    # Fetch stocks from DynamoDB
    response = table.scan()
    user_stocks = response.get('Items', [])

    # Successful fetch from DynamoDB
    logger.info(f"Fetched {len(user_stocks)} stocks from DynamoDB.")


    return render_template('index.html', stocks=user_stocks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
