#!/usr/bin/env python
#Reducer.py
import sys

average_data = {"Amazon_average_open_price": [], 
            "Amazon_average_close_price": [],
            "Amazon_average_high_price": [],
            "Amazon_average_low_price": [],
            "Amazon_average_volume": [],

            "Google_average_open_price": [], 
            "Google_average_close_price": [],
            "Google_average_high_price": [], 
            "Google_average_low_price": [], 
            "Google_average_volume": [], 

            "Apple_average_open_price": [], 
            "Apple_average_close_price": [],
            "Apple_average_high_price": [],
            "Apple_average_low_price": [],
            "Apple_average_volume": []}

totaled_data = {
    "Amazon_total_volume": 0,
    "Google_total_volume": 0,
    "Apple_total_volume": 0,
}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    open, high, low, close, volume, company = line.split('\t')

    if (company == "Apple"):
        average_data["Apple_average_open_price"].append(float(open))
        average_data["Apple_average_close_price"].append(float(close))
        average_data["Apple_average_high_price"].append(float(high))
        average_data["Apple_average_low_price"].append(float(low))
        average_data["Apple_average_volume"].append(float(volume))

        totaled_data["Apple_total_volume"] = totaled_data["Apple_total_volume"] + int(volume)

    
    elif (company == "Google"):
        average_data["Google_average_open_price"].append(float(open))
        average_data["Google_average_close_price"].append(float(close))
        average_data["Google_average_high_price"].append(float(high))
        average_data["Google_average_low_price"].append(float(low))
        average_data["Google_average_volume"].append(float(volume))

        totaled_data["Google_total_volume"] = totaled_data["Google_total_volume"] + int(volume)

    elif (company == "Amazon"):
        average_data["Amazon_average_open_price"].append(float(open))
        average_data["Amazon_average_close_price"].append(float(close))
        average_data["Amazon_average_high_price"].append(float(high))
        average_data["Amazon_average_low_price"].append(float(low))
        average_data["Amazon_average_volume"].append(float(volume))

        totaled_data["Amazon_total_volume"] = totaled_data["Amazon_total_volume"] + int(volume)

#Reducer
for key in average_data.keys():
    averate_price = sum(average_data[key])*1.0 / len(average_data[key])
    print('{}\t{}'.format(key, averate_price))


print('{}\t{}'.format("Amazon_total_volume", totaled_data["Amazon_total_volume"]))
print('{}\t{}'.format("Google_total_volume", totaled_data["Google_total_volume"]))
print('{}\t{}'.format("Apple_total_volume", totaled_data["Apple_total_volume"]))
