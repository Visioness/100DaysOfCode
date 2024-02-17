from rent_data import RentData
from sheet import Sheet


rent = RentData()
sheet = Sheet()

addresses, links, prices = rent.get_data()

for n in range(len(addresses)):
    sheet.send_form(addresses[n], prices[n], links[n])
    print(f'Sent the form {n}.')

print('All forms are sent!')