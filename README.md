# Basic-Calculator-Program-in-Python

## 📋 Description
Python program that performs basic arithmetic operations — **addition, subtraction, multiplication, division, and modulus (%)** — on two numbers provided by the user.

The calculator ensures that:
- The user enters **valid numeric inputs**.
- The user selects a **valid operation** from the allowed list.
- It **prevents division/modulus by zero** and handles such cases gracefully.


## Features

- Accepts user input for two numbers
- Performs one of the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Modulus (`%`)
- Displays the result of the operation
- Prompts again if the user enters an invalid operation
- Protects against division or modulus by zero


## WEEK 3 ASSIGNMENT

# Discount Calculator in Python

## Description
This Python program calculates the final price of an item after applying a discount.  
If the discount percentage is **20% or higher**, the discount is applied.  
Otherwise, the original price is returned without changes.

## Features
- Prompts the user for the original price.
- Prompts the user for the discount percentage.
- Applies the discount only if it's **20% or more**.
- Displays either the discounted price or the original price.

## How It Works
1. The program defines a function `calculate_discount(price, discount_percent)`:
   - If `discount_percent >= 20`, it applies the discount and returns the final price.
   - Otherwise, it returns the original price.
2. The user is prompted to input:
   - Original price (float value)
   - Discount percentage (float value)
3. The program prints the result based on the discount condition.

