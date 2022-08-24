import math
import pyperclip

count = 0
dealpost_draft = """>>> {} [24 HOURS]<<<
----------------------------------
{}{}
Sale Price - ${:,.2f} ({})
IN BDT - TK {:,.2f}
+
Weight Charge (To be Added After Product Arrival to BD)
Rate - {}Tk per 100gm
----------------------------------
Product Link: {}
----------------------------------
Advance Required - TK {:,.2f}
Quantity Available - Limited{}

Expected Shipment Arrival:
In Between {} Weeks minimum (Exact estimate can't be given)
----------------------------------
**ATTENTION: Please try to use PC/Laptop & Google Chrome Browser. The system isn't fully compatible with Mobile or \
other browsers.**
----------------------------------
How to Order:
1. Sign In/Sign Up to our Ordering Portal here: http://app.shoptobd.com/
2. {}(Tutorial Video, if needed: http://bit.ly/shoptobdorder)
3. Shoptobd will verify the order & generate the Initial Invoice. Log back later to check it & contact us \
to confirm.
4. Proceed with the Advance for your order. Payment Methods are	mentioned in your account dashboard.
5. Contact us on FB or through email with the proof of payment, either picture for Deposit Slip or \
Number/Transaction ID for bKash.
6. Once Payment is confirmed, the order will be placed.
"""


def get_values():
    global count
    product_name = product_price = sale_price = product_link = shipping = tax_rate = order_by = weeks = None
    while True:
        country = input("Enter Country(capital letters): ")
        if country == '-1': continue
        if 'count' in country:
            count = count + int(country[6:len(country)])
            print(f"\n\ntotal deal posted: {count}\n\n")
            continue

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
        'country': country,
        'product_name': product_name,
        'product_price': product_price,
        'sale_price': sale_price,
        'product_link': product_link,
        'shipping': shipping,
        'tax_rate': tax_rate,
        'order_by': order_by,
        'weeks': weeks
    }

    return dictionary


def assign(dictionary: dict):
    if not dictionary['country']:
        country = 'USA'
        rate = 122
        weight_charge = "200"
        tutorial = "Choose 'USA Order Cycle - Aug 2022(\"USD\")' & Place the order. "
        week = "5-6" if not dictionary['weeks'] else dictionary['weeks']
        # if 'amazon' in dictionary['product_link']: week = '4'
    else:
        country = 'CANADA'
        rate = 92
        weight_charge = "200"
        tutorial = "Choose 'CANADA Order Cycle - Aug 2022(\"CAD\")' & Place the order. "
        week = "5-6" if not dictionary['weeks'] else dictionary['weeks']
        # if 'amazon' in dictionary['product_link']: week = '3'

    if not dictionary['order_by']:
        order_by = ''
    else:
        order_by = f"\nOrder By - {dictionary['order_by']} hours"

    tax_rate = dictionary['tax_rate']
    if tax_rate == "":
        if country == "CANADA":
            tax_rate = 15
        elif country == "USA":
            tax_rate = 9
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

    final_price = math.ceil((product_price + (product_price * tax_rate / 100)))
    bdt = final_price * rate
    advance = int((bdt / 2) / 100) * 100

    product_name = dictionary['product_name']
    product_link = dictionary['product_link']

    country = "SHOPTOBD " + country + " DEAL"
    dealpost_final = dealpost_draft.format(country, product_name, off, final_price,
                                           tax, bdt, weight_charge, product_link,
                                           advance, order_by, week, tutorial)
    return dealpost_final


if __name__ == '__main__':
    while True:
        values = get_values()
        post = assign(values)
        pyperclip.copy(post)
        count += 1
        print("\n\n" + post)
        print(f"\n\ntotal deal posted: {count}\n\n")
