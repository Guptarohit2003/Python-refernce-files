purchased_jewels_list = [i for i in input().split(" ")]
purchased_quatity_in_grams_list = [int(i) for i in input().split(' ')] 
avail_jewel_price_per_gram_dict = { 
        'Bentex': 20,
        "Silver": 50,
        "Gold": 2600,
        'Platinum': 3000,
        }
bill_amount = 0
for i in range(len(purchased_jewels_list)):
    if purchased_jewels_list[i] in avail_jewel_price_per_gram_dict:
        bill_amount += purchased_quatity_in_grams_list[i]*avail_jewel_price_per_gram_dict.get(purchased_jewels_list[i])
    else: 
        bill_amount = -1

if bill_amount > 20000:
    print(float(bill_amount*(97/100)))
else:
    print(float(bill_amount))