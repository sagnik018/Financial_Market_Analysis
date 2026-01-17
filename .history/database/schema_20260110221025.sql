USE financial_db;

USE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(20),
    trade_date DATE,
    open_price DECIMAL(10,2),
    close_price DECIMAL(10,2),
    high DECIMAL(10,2),
    low DECIMAL(10,2),
    adjusted-
    volume BIGINT
);
