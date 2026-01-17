
USE investment_data;

CREATE TABLE asset_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20),
    asset_type VARCHAR(20),
    trade_date DATE,
    close_price DECIMAL(10,2),
    volume BIGINT
);
