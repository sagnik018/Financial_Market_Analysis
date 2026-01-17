USE financial_db;

USE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(20),
    trade_date ,
    trade_date DATE,
    close_price DECIMAL(10,2),
    volume BIGINT
);
