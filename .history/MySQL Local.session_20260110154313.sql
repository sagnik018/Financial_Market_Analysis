USE financial_db;

CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20),
    trade_date DATE,
    open_price DECIMAL(10,2),
    high_price DECIMAL(10,2),
    low_price DECIMAL(10,2),
    close_price DECIMAL(10,2),
    volume BIGINT
);
INSERT INTO stock_prices (
    id,
    symbol,
    trade_date,
    open_price,
    high_price,
    low_price,
    close_price,
    volume
  )
VALUES (
    id:int,
    'symbol:varchar',
    'trade_date:date',
    'open_price:decimal',
    'high_price:decimal',
    'low_price:decimal',
    'close_price:decimal',
    'volume:bigint'
  );