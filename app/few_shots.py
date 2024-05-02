few_shots = [
    {
        'Question' : "How many shoes do we have left for Nike in size 6 and white color?",
        'SQLQuery' : "SELECT SUM(stock_quantity) FROM shoes WHERE brand = 'Nike' AND color = 'White' AND size = '6'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "We have 31 shoes left for Nike white color shoes in size 6"
    },
    {
        'Question': "How much is the total price of the inventory for all size 7 shoes?",
        'SQLQuery':"SELECT SUM(price * stock_quantity) FROM shoes WHERE size = '7'",
        'SQLResult': "Result of the SQL query",
        'Answer': "The total price of inventory for size 7 shoes is 41476.12"
    },
    {
        'Question': "If we have to sell all the Adidas shoes today with discounts applied, how much revenue our store will generate (post discounts)?",
        'SQLQuery' : """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue 
                        FROM (SELECT SUM(price * stock_quantity) as total_amount, shoe_id 
                              FROM shoes WHERE brand = 'Adidas' GROUP BY shoe_id) a 
                        LEFT JOIN discounts ON a.shoe_id = discounts.shoe_id""",
        'SQLResult': "Result of the SQL query",
        'Answer': "Adidas shoes will generate revenue of 53408.14400000 after discount"
    },
    {
        'Question' : "If we have to sell all the Adidas shoes today, how much revenue our store will generate without discount?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM shoes WHERE brand = 'Adidas'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Adidas shoes will generate revenue of 59962.73 after discount"
    },
    # {
    #     'Question': "How many white color Adidas shoes do I have?",
    #     'SQLQuery' : "SELECT SUM(stock_quantity) FROM shoes WHERE brand = 'Adidas' AND color = 'White'",
    #     'SQLResult': "Result of the SQL query",
    #     'Answer' : "There are 189 white color Adidas shoes"
    # },
    {
        'Question': "How many Puma shoes do I have?",
        'SQLQuery' : "SELECT SUM(stock_quantity) FROM shoes WHERE brand = 'Puma'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "There are 690 Puma shoes"
    },
    {
        "Question": "What are the top 4 shoes with the highest quantity?",
        "SQLQuery": "SELECT * FROM shoes ORDER BY stock_quantity DESC LIMIT 4",
        "SQLResult": "[(5, 'Reebok', 'Red', '9', 36.79, 100), (12, 'Adidas', 'Blue', '7', 95.01, 99), (877, 'Puma', 'Blue', '9', 85.69, 99), (38, 'Reebok', 'Blue', '7', 68.54, 97)]",
        "Answer": "The top 4 shoes with the highest quantity are Reebok Red size 9, Adidas Blue size 7, Puma Blue size 9, and Reebok Blue size 7."
    },
    {
        "Question": "Update or create a new entry for a shoe with the following details: brand: [Brand], color: [Color], size: [Size], price: [Price], stock quantity: [StockQuantity].",
        "SQLQuery": "INSERT INTO shoes (brand, color, size, price, stock_quantity) VALUES ('[Brand]', '[Color]', '[Size]', [Price], [StockQuantity]) ON DUPLICATE KEY UPDATE price = VALUES(price), stock_quantity = VALUES(stock_quantity);",
        "SQLResult": "Result of the SQL query",
        "Answer": "The details have been updated if the entry already exists in the database. If not, a new entry has been created with the provided details."
    },
    {
        'Question': "I sold all the nike shoes.",
        'SQLQuery': "DELETE FROM Shoes WHERE brand = 'Nike'",
        'SQLResult': "Result of the SQL query",
        'Answer': "Success"
    },
    {
        "Question": "I sold all the Nike shoes. What is the new total stock quantity of Nike shoes?",
        "SQLQuery": "WITH DeletedDiscounts AS ( DELETE FROM discounts WHERE shoe_id IN (SELECT shoe_id FROM shoes WHERE brand='Nike')) UPDATE shoes SET stock_quantity= 0 WHERE brand = 'Nike'",
        "SQLResult": "Result of the SQL queries",
        "Answer": "All Nike shoes have been sold. The new total stock quantity of Nike shoes is 0."
    },
    {
        "Question": "All the size 8 shoes have been sold. Update the stock quantity of size 8 shoes to 0.",
        "SQLQuery": "UPDATE shoes SET stock_quantity = 0 WHERE size = '8';",
        "SQLResult": "Result of the SQL query",
        "Answer": "All size 8 shoes have been sold. The stock quantity of size 8 shoes has been updated to 0."
    },
    {
        "Question": "All the Nike shoes of all sizes have been sold. Update the stock quantity of all Nike shoes to 0.",
        "SQLQuery": "WITH DeletedDiscounts AS(DELETE FROM discounts WHERE shoe_id IN(SELECT shoe_id FROM shoes WHERE brand='Nike')) UPDATE shoes SET stock_quantity= 0 WHERE brand = 'Nike'",
        "SQLResult": "Result of the SQL queries",
        "Answer": "All Nike shoes of all sizes have been sold. The stock quantity of all Nike shoes has been updated to 0."
    },
    {
        "Question": "All the shoes have been sold. Update the stock quantity of all shoes to 0.",
        "SQLQuery": "UPDATE shoes SET stock_quantity = 0;",
        "SQLResult": "Result of the SQL query",
        "Answer": "All shoes have been sold. The stock quantity of all shoes has been updated to 0."
    },
    {
        "Question": "There are no more discounts on any shoes. Delete all entries from the discounts table.",
        "SQLQuery": "DELETE FROM discounts WHERE discount_id > 0",
        "SQLResult": "Result of the SQL query",
        "Answer": "All discounts on shoes have been removed. The discounts table is now empty."
    },
    {
        "Question": "There are no discounts on Puma shoes. Delete all discount entries for Puma shoes from the discounts table.",
        "SQLQuery": "DELETE FROM discounts WHERE shoe_id IN (SELECT shoe_id FROM shoes WHERE brand = 'Puma')",
        "SQLResult": "Result of the SQL query",
        "Answer": "All discounts on Puma shoes have been removed."
    },
   
]


