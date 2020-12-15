#Google is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system (Pizza Points™)
#that can be tweaked in the future. The rules are simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!

#Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. Return a list of customers that are eligible for a free pizza.

#Examples
'''customers = {
  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}

  pizza_points(customers, 5, 20) ➞ ["Spider-Man"]

  pizza_points(customers, 3, 10) ➞ ["Batman", "Spider-Man"]

  pizza_points(customers, 5, 100) ➞ []'''
#Notes
#⚠️Sort the returned array of customer names in alphabetical order.

dict1 = {
  'Batman': [22, 30, 11, 17, 15, 52, 27, 12],
  'Spider-Man': [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}

dict2 = {
  'Captain America': [10, 10, 54, 14, 51, 33, 42, 73, 66, 33, 55, 42, 47],
  'Iron Man': [30, 56, 38, 14, 17],
  'Hulk': [53, 25, 13, 7, 61, 16, 17, 29, 64, 8],
  'Superman': [27, 28]
}

dict3 = {
  'Zorro': [13, 53, 10, 51],
  'Wolverine': [16],
  'Elon Musk': [26, 61, 23, 61, 39, 50, 53, 54, 45, 46, 42, 49, 18, 75, 11, 73, 42, 61, 15, 60, 70, 67, 8, 9, 63, 55, 55, 35, 24, 59, 13, 49, 46, 26, 7, 8, 8, 34, 73, 60, 27, 28, 28, 48, 10]
}


def pizza_points(customers, min_orders, min_price):
    customerGetPizza = []
    for customer in customers:
        priceL = []
        for price in customers[customer]:
            if price >= min_price:
                priceL.append(price)
            else:
                pass
            if len(priceL) >= min_orders and customer not in customerGetPizza:
                customerGetPizza.append(customer)
    return sorted(customerGetPizza)


print(pizza_points(dict2,3,12))
