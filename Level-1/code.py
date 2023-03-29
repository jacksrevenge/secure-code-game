'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payments = []
    product_cost = 0
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            payments.append(("payment",item.amount * item.quantity))
        elif item.type == 'product':
            payments.append(("product",item.amount * item.quantity))
        else:
            return("Invalid item type: %s" % item.type)
    print(payments)
    for payment in payments:
        if payment[0] == "product":
            product_cost += payment[1]
        if payment[0] == "payment":
            net += payment[1]

    if product_cost != net:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net - product_cost))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
