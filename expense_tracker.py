import pandas as pd
import numpy as np 

from dataclasses import dataclass


def main():
    '''
    This is the main function which will have our main code
    '''

    total_budjet = 100000

    print('Welcome To Expense Tracker Tool ❤')
    print('Track your expenses with our tool 💻')

    try:
        while True:
            expense_name = input('Enter your expense name 🛒: ')
            expense_price = input('Enter your expense amount 💸:')
            
            data = {
                'expense_name' : [expense_name],
                'price' : [expense_price]
            }

            data_row = pd.DataFrame(data)

            expense_data = pd.read_csv('expenses.csv')

            updated_data = pd.concat([expense_data, data_row])

            updated_data.to_csv('expenses.csv', index=False)

            new_data = pd.read_csv('expenses.csv')

            total_expense = sum(new_data['price'].values)

            print(f'Total Expenses Are 💰: {total_expense}')
            print(f'Budjet Left 💸: {total_budjet - total_expense}')

            continue_again = input('Do you want to add another expense (y / n): ').lower()

            if continue_again == 'y':
                continue

            else:
                break

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()