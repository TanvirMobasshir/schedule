import math
import pyperclip
import json
from datetime import datetime

current_month = datetime.now().month
current_year = datetime.now().year
months = [None, 'JAN', "FEB", "MAR", 'APR', 'MAY', 'JUNE', 'JULY', 'AUG', 'SEPT', 'OCT', 'NOV', 'DEC']

count = 0

new_draft = """
🏷️ {}{}

💵 Price (Including Tax in USA): 

🇺🇸 ${:,.2f} ({})

🇧🇩 BDT {:,.2f}

📦 Weight Rate: BDT {}TK/100g 

(To be Added After Product Arrival to BD)

🌐 Product Link: {}

🔢 Quantity: Limited Available

{}

--------

💳 Advance Payment: BDT {:,.2f}
{}
✈️ Shipment Time: {} Weeks Minimum (Subject to Change)

--------

🛒 How to Order:

➡️ Place Order in our Portal: http://app.shoptobd.com/

➡️ Inbox Us with Product Name/Image to get started
"""

constants = {
    'usa_rate': 134,
    'usa_weight': '200',
    'usa_week': '7-8',
    'usa_tax': 9,
    'canada_rate': 92,
    'canada_weight': "200",
    'canada_week': '5-6',
    'canada_tax': 15
}


def get_values():
    global count
    product_name = product_price = sale_price = product_link = shipping = tax_rate = order_by = weeks = color = None
    while True:
        product_name = input("Enter product name fully: ")
        if product_name == '-1': continue
        if 'count' in product_name:
            count = count + int(product_name[6:len(product_name)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        product_price = input("Enter price: ")
        if product_price == '-1': continue
        if 'count' in product_price:
            count = count + int(product_price[6:len(product_price)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        sale_price = input("Enter sale price: ")
        if sale_price == '-1': continue
        if 'count' in sale_price:
            count = count + int(sale_price[6:len(sale_price)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        product_link = input("Enter product link: ")
        if product_link == '-1': continue
        if 'count' in product_link:
            count = count + int(product_link[6:len(product_link)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        color = input("Enter product Color/Size: ")
        if color == '-1': continue
        if 'count' in color:
            count = count + int(product_link[6:len(product_link)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        shipping = input("shipping: ")
        if shipping == '-1': continue
        if 'count' in shipping:
            count = count + int(shipping[6:len(shipping)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        tax_rate = input("Enter tax rate(books 5%): ")
        if tax_rate == '-1': continue
        if 'count' in tax_rate:
            count = count + int(tax_rate[6:len(tax_rate)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        order_by = input("Order by: ")
        if order_by == '-1': continue
        if 'count' in order_by:
            count = count + int(order_by[6:len(order_by)])
            print(f"\n\ntotal deal posted: {count}\n")
            continue

        weeks = input("Delivery Week: ")
        if weeks == '-1': continue
        if 'count' in weeks:
            count = count + int(weeks[6:len(weeks)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

        break

    dictionary = {
        'product_name': product_name,
        'product_price': product_price,
        'sale_price': sale_price,
        'product_link': product_link,
        "color": color,
        'shipping': shipping,
        'tax_rate': tax_rate,
        'order_by': order_by,
        'weeks': weeks
    }

    return dictionary


def change_constant_values():
    global constants

    print('\n')

    usa_rate = input("USA dollar rate: ")
    try:
        constants['usa_rate'] = int(usa_rate)
    except ValueError:
        constants['usa_rate'] = constants['usa_rate']

    usa_weight = input("USA weight charge: ")
    if len(usa_weight) != 0:
        constants['usa_weight'] = usa_weight
    else:
        constants['usa_weight'] = constants['usa_weight']

    usa_week = input("USA shipment time: ")
    if len(usa_week) != 0:
        constants['usa_week'] = usa_week
    else:
        constants['usa_week'] = constants['usa_week']

    usa_tax = input("USA tax rate: ")
    try:
        constants['usa_tax'] = int(usa_tax)
    except ValueError:
        constants['usa_tax'] = constants['usa_tax']

    canada_rate = input("canada dollar rate: ")
    try:
        constants['canada_rate'] = int(canada_rate)
    except ValueError:
        constants['canada_rate'] = constants['canada_rate']

    canada_weight = input("canada weight charge: ")
    if len(canada_weight) != 0:
        constants['canada_weight'] = canada_weight
    else:
        constants['canada_weight'] = constants['canada_weight']

    canada_week = input("canada shipment time: ")
    if len(canada_week) != 0:
        constants['canada_week'] = canada_week
    else:
        constants['canada_week'] = constants['canada_week']

    canada_tax = input("canada tax rate: ")
    try:
        constants['canada_tax'] = int(canada_tax)
    except ValueError:
        constants['canada_tax'] = constants['canada_tax']


def assign(dictionary: dict):
    rate = constants['usa_rate']
    weight_charge = constants['usa_weight']
    week = constants['usa_week'] if not dictionary['weeks'] else dictionary['weeks']

    if not dictionary['order_by']:
        order_by = ''
    else:
        order_by = f"\nOrder By - {dictionary['order_by']} hours\n"

    tax_rate = dictionary['tax_rate']
    if tax_rate == "":
        tax_rate = constants['usa_tax']
    else:
        tax_rate = float(dictionary['tax_rate'])

    product_price = float(dictionary['product_price'])
    if dictionary['sale_price'] != "":
        sale_price = float(dictionary['sale_price'])
        off_int = round((product_price - sale_price) / product_price * 100)
        off = " - {}% Off".format(off_int)
        product_price = sale_price
    else:
        off = ''

    if dictionary['shipping'] != "":
        product_price = product_price + float(dictionary['shipping'])
        tax = "with Tax and Shipping"
    else:
        tax = 'with Tax'

    color = dictionary['color']
    if color != "":
        color = f"↔️ Color/Size: {color}"

    final_price = math.ceil((product_price + (product_price * tax_rate / 100)))
    bdt = final_price * rate
    advance = int((bdt / 2) / 100) * 100

    product_name = dictionary['product_name'].replace('-', ' ')
    product_link = dictionary['product_link']

    df = new_draft.format(product_name, off, final_price, tax, bdt, weight_charge, product_link, color, advance,
                          order_by, week)
    return df


if __name__ == '__main__':
    while True:
        print(json.dumps(constants, indent=4))
        print('\n')

        print(f"\n\ntotal deal posted: {count}")
        change = input('Change Constant Values? ')
        if change: change_constant_values()
        print('\n')

        try:
            values = get_values()
        except KeyboardInterrupt as e:
            confirm = input("Are you sure? type 'yes'\n")
            if confirm != 'yes':
                continue
            else:
                exit()
        post = assign(values)
        try:
            pyperclip.copy(post)
        except Exception as e:
            print()
        count += 1
        line = '_______________________________________________________________________________________________________'

        print('\n' + line + '\n' + line)
        print("\n\n" + post)
        print(line + '\n' + line)
        print(f"\n\ntotal deal posted: {count}\n\n")
