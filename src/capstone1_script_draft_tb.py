# Import in libraries for EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
font = {'weight':'bold', 'size':16}

# Read in Initial May 2016 Dataset for Listings

may_2016_df = pd.read_csv('./data/may_2016/2016_may_listings.csv')

# Count Unique Listing ID's for May 2016 

may_2016_listing_ total = may_2016_df['id'].count()

# Total Unique Listing ID's for May 2016 = 2505

# Repeat Steps Above to Evaluate Unique Listing Totals for All Other Datasets Availalble 

# Total Unique Listing ID's for Remaining Months
# May 2016 = 2505
# November 2017 = 3918
# April 2018 = 4412
# July 2018 = 4853
# August 2018 = 4984
# September 2018 = 5089
# October 2018 = 5105
# November 2018 = 5222
# December 2018 = 5106
# January 2019 = 4766
# February 2019 = 4808
# March 2019 = 4668
# April 2019 = 4686
# May 2019 = 4659
# June 2019 = 4511
# July 2019 = 4588
# August 2019 = 4541
# September 2019 = 4601
# October 2019 = 4794
# November 2019 = 4865
# December 2019 = 4964
# January 2020 = 4860
# February 2020 = 4951
# March 2020 = 4868 (Data Scraped on 3/23/20)
# April 2020 = 4478
# May 2020 = 4256
# June 2020 = 4200

# Build a Dictionary of the Unique Listing ID totals for each month

den_airbnb_listing_totals = {
    'may_2016': 2505,
    'nov_2017': 3918,
    'april_2018': 4412,
    'july_2018': 4853,
    'aug_2018': 4984,
    'sept_2018': 5089,
    'oct_2018': 5105,
    'nov_2018': 5222,
    'dec_2018': 5106,
    'jan_2019': 4766,
    'feb_2019': 4808,
    'march_2019': 4668,
    'april_2019': 4686,
    'may_2019': 4659,
    'june_2019': 4511,
    'july_2019': 4588,
    'august_2019': 4541,
    'sept_2019': 4601,
    'oct_2019': 4794,
    'nov_2019': 4865,
    'dec_2019': 4964,
    'jan_2020': 4860,
    'feb_2020': 4951,
    'march_2020': 4868,
    'april_2020': 4478,
    'may_2020': 4256,
    'june_2020': 4200
}

# Will Plot Results Later but max was around November 2018

# Question 2: What is the Breakdown of Rental Property Type per Month?

# Utilized a 'Group By' method in Pandas to extract the data:

dec_2018_room_types = dec_2018_df.groupby('room_type').count()

den_airbnb_room_type = {
    'may_2016': {
        'total': 2505,
        'entire_unit': 1621,
        'private_room': 818,
        'shared_room': 66,
    },
    'nov_2017': {
        'total': 3918,
        'entire_unit': 2659,
        'private_room': 1188,
        'shared_room': 71,
    },
    'april_2018': {
        'total': 4412,
        'entire_unit': 3901,
        'private_room': 1234,
        'shared_room': 87,
    },
    'july_2018': {
        'total': 4853,
        'entire_unit': 3561,
        'private_room': 1220,
        'shared_room': 72,
    },
    'aug_2018': {
        'total': 4984,
        'entire_unit': 3664,
        'private_room': 1239,
        'shared_room': 81,
    },
    'sept_2018': {
        'total': 5089,
        'entire_unit': 3753,
        'private_room': 1254,
        'shared_room': 82,
    },
    'oct_2018': {
        'total': 5105,
        'entire_unit': 3740,
        'private_room': 1275,
        'shared_room': 90,
    },
    'nov_2018': {
        'total': 5222,
        'entire_unit': 3843,
        'private_room': 1269,
        'shared_room': 110,
    },
    'dec_2018': {
        'total': 5106,
        'entire_unit': 3765,
        'private_room': 1241,
        'shared_room': 100,
    },
    'jan_2019': {
        'total': 4766,
        'entire_unit': 3506,
        'private_room': 1159,
        'shared_room': 101,
    },
    'feb_2019': {
        'total': 4808,
        'entire_unit': 3558,
        'private_room': 1147,
        'shared_room': 103,
    },
    'march_2019': {
        'total': 4668,
        'entire_unit': 3446,
        'private_room': 1118,
        'shared_room': 104,
    },
    'april_2019': {
        'total': 4686,
        'entire_unit': 3457,
        'private_room': 1125,
        'shared_room': 104,
    },
    'may_2019': {
        'total': 4659,
        'entire_unit': 3434,
        'private_room': 1124,
        'shared_room': 101,
    },
    'june_2019': {
        'total': 4511,
        'entire_unit': 3300,
        'private_room': 1113,
        'shared_room': 98,
    },
    'july_2019': {
        'total': 4588,
        'entire_unit': 3356,
        'private_room': 1122,
        'shared_room': 110,
    },
    'august_2019': {
        'total': 4541,
        'entire_unit': 3368,
        'hotel_room': 1,
        'private_room': 1098, 
        'shared_room': 74,
    },
    'sept_2019': {
        'total': 4601,
        'entire_unit': 3402,
        'hotel_room': 34,
        'private_room': 1090,
        'shared_room': 75,
    },
    'oct_2019': {
        'total': 4794,
        'entire_unit': 3543,
        'hotel_room': 39,
        'private_room': 1123,
        'shared_room': 89,
    },
    'nov_2019': {
        'total': 4865,
        'entire_unit': 3619,
        'hotel_room': 39,
        'private_room': 1144,
        'shared_room': 63,
    },
    'dec_2019': {
        'total': 4964,
        'entire_unit': 3727,
        'hotel_room': 38,
        'private_room': 1132,
        'shared_room': 67,
    },
    'jan_2020': {
        'total': 4860,
        'entire_unit': 3653,
        'hotel_room': 36,
        'private_room': 1120,
        'shared_room': 51,
    },
    'feb_2020': {
        'total': 4951,
        'entire_unit': 3710,
        'hotel_room': 36,
        'private_room': 1148,
        'shared_room': 57,
    },
    'march_2020': {
        'total': 4868,
        'entire_unit': 3647,
        'hotel_room': 35,
        'private_room': 1124,
        'shared_room': 62,
    },
    'april_2020': {
        'total': 4478,
        'entire_unit': 3358,
        'hotel_room': 35,
        'private_room': 1040,
        'shared_room': 45,
    },
    'may_2020': {
        'total': 4256,
        'entire_unit': 3200,
        'hotel_room': 35,
        'private_room': 972,
        'shared_room': 49,
    },
    'june_2020': {
        'total': 4200,
        'entire_unit': 3186,
        'hotel_room': 35,
        'private_room': 935,
        'shared_room': 44,
    }
    
}


# Question 3: What is the breakdown by units per Neighborhood in Devner for each data set? 

june_2020_neighborhoods = june_2020_df.groupby('neighbourhood').count()
d = dict(june_2020_neighborhoods['id'].sort_values(ascending = False).head(10))

d = {k.lower(): v for k,v in d.items()}
d = {k.replace(" ","_"): v for k,v in d.items()}

for k,v in d.items():
    print(f"'{k}': {v},")

# WHEN CREATING THE SCRIPT ADD SOME CODE TO APPEND THE DICT/    

top10_neighborhood_totals = {
    'may_2016': {
        'five_points': 243,
        'capitol_hill': 193,
        'highland': 144,
        'speer': 98,
        'cheesman_park': 91,
        'sunnyside': 81,
        'city_park_west': 80,
        'union_station': 78,
        'baker': 76,
        'west_highland':75,
    },
    'nov_2017': {
        'five_points': 326,
        'highland': 247,
        'capitol_hill': 233,
        'speer': 155,
        'west_highland': 129,
        'sunnyside': 126,
        'whittier': 121,
        'baker': 111,
        'city_park_west': 97,
        'union_station': 93,
    },
    'april_2018': {
        'five_points': 350,
        'highland': 283,
        'capitol_hill': 273,
        'speer': 168,
        'sunnyside': 151,
        'west_highland': 134,
        'whittier': 126,
        'baker': 121,
        'lincoln_park': 110,
        'sloan_lake': 108,
    },
    'july_2018': {
        'five_points': 449,
        'highland': 320,
        'capitol_hill': 280,
        'speer': 174,
        'sunnyside': 157,
        'west_highland': 143,
        'cbd': 141,
        'union_station': 135,
        'whittier': 130,
        'baker': 122,
    },
    'aug_2018': {
        'five_points': 459,
        'highland': 336,
        'capitol_hill': 278,
        'speer': 172,
        'sunnyside': 157,
        'cbd': 154,
        'west_highland': 148,
        'union_station': 142,
        'whittier': 132,
        'lincoln_park': 125,
    },
    'sept_2018': {
        'five_points': 487,
        'highland': 359,
        'capitol_hill': 283,
        'speer': 180,
        'union_station': 163,
        'sunnyside': 153,
        'west_highland': 149,
        'cbd': 146,
        'whittier': 139,
        'lincoln_park': 126,
    },
    'oct_2018': {
        'five_points':497,
        'highland':348,
        'capitol_hill':273,
        'speer':191,
        'union_station':174,
        'sunnyside':155,
        'west_highland':145,
        'cbd':138,
        'whittier':132,
        'west_colfax':129,
    },
    'nov_2018': {
        'five_points':507,
        'highland':350,
        'capitol_hill':282,
        'speer':198,
        'union_station':176,
        'sunnyside':162,
        'west_highland':150,
        'cbd':139,
        'west_colfax':134,
        'lincoln_park':132,
    },
    'dec_2018': {
        'five_points':486,
        'highland':351,
        'capitol_hill':268,
        'speer':200,
        'union_station':174,
        'sunnyside':160,
        'west_highland':146,
        'west_colfax':138,
        'berkeley':130,
        'whittier':130,
    },
    'jan_2019': {
        'five_points':480,
        'highland':338,
        'capitol_hill':230,
        'speer':178,
        'sunnyside':160,
        'west_highland':143,
        'berkeley':136,
        'union_station':129,
        'west_colfax':125,
        'city_park_west':122,
    },
    'feb_2019': {
        'five_points':469,
        'highland':340,
        'capitol_hill':234,
        'speer':180,
        'sunnyside':164,
        'west_highland':149,
        'union_station':148,
        'berkeley':138,
        'west_colfax':129,
        'cbd':127,
    },
    'march_2019': {
        'five_points': 457,
        'highland': 341,
        'capitol_hill': 215,
        'speer': 172,
        'sunnyside': 166,
        'west_highland': 150,
        'union_station': 149,
        'berkeley': 133,
        'whittier': 126,
        'west_colfax': 120,
    },
    'april_2019': {
        'five_points': 462,
        'highland': 320,
        'capitol_hill': 219,
        'speer': 172,
        'sunnyside': 165,
        'union_station': 149,
        'west_highland': 144,
        'whittier': 132,
        'berkeley': 130,
        'west_colfax': 126,
    },
    'may_2019': {
        'five_points': 367,
        'highland': 315,
        'capitol_hill': 210,
        'speer': 173,
        'sunnyside': 159,
        'union_station': 156,
        'west_highland': 149,
        'west_colfax': 131,
        'berkeley': 130,
        'whittier': 130,
    },
    'june_2019': {
        'five_points': 366,
        'highland': 303,
        'capitol_hill': 205,
        'speer': 165,
        'sunnyside': 152,
        'west_highland': 149,
        'union_station': 140,
        'west_colfax': 130,
        'whittier': 128,
        'berkeley': 126,
    },
    'july_2019': {
        'five_points': 360,
        'highland': 303,
        'capitol_hill': 214,
        'sunnyside': 159,
        'union_station': 157,
        'speer': 156,
        'west_highland': 151,
        'whittier': 134,
        'west_colfax': 133,
        'gateway-green_valley_ranch': 126,
    },
    'august_2019': {
        'five_points': 334,
        'highland': 295,
        'capitol_hill': 213,
        'union_station': 160,
        'sunnyside': 153,
        'speer': 151,
        'west_highland': 146,
        'west_colfax': 137,
        'gateway-green_valley_ranch': 131,
        'whittier': 128,
    },
    'sept_2019': {
        'five_points': 359,
        'highland': 279,
        'capitol_hill': 213,
        'union_station': 171,
        'sunnyside': 165,
        'speer': 151,
        'gateway-green_valley_ranch': 143,
        'west_highland': 140,
        'whittier': 131,
        'west_colfax': 130,
    },
    'oct_2019': {
        'five_points': 372,
        'highland': 280,
        'capitol_hill': 215,
        'union_station': 185,
        'sunnyside': 164,
        'speer': 158,
        'gateway-green_valley_ranch': 153,
        'west_highland': 142,
        'west_colfax': 139,
        'whittier': 130,
    },
    'nov_2019': {
        'five_points': 381,
        'highland': 280,
        'capitol_hill': 209,
        'union_station': 207,
        'sunnyside': 166,
        'gateway-green_valley_ranch': 163,
        'speer': 154,
        'west_highland': 145,
        'west_colfax': 143,
        'whittier': 125,
    },
    'dec_2019': {
        'five_points': 465,
        'highland': 280,
        'union_station': 218,
        'capitol_hill': 207,
        'gateway-green_valley_ranch': 166,
        'sunnyside': 159,
        'speer': 156,
        'west_colfax': 149,
        'west_highland': 144,
        'berkeley': 128,
    },
    'jan_2020': {
        'five_points': 455,
        'highland': 273,
        'union_station': 225,
        'capitol_hill': 200,
        'gateway-green_valley_ranch': 160,
        'sunnyside': 158,
        'west_colfax': 152,
        'speer': 152,
        'west_highland': 145,
        'whittier': 126,
    },
    'feb_2020': {
        'five_points': 473,
        'highland': 286,
        'union_station': 246,
        'capitol_hill': 197,
        'gateway-green_valley_ranch': 158,
        'sunnyside': 152,
        'speer': 150,
        'west_colfax': 144,
        'west_highland': 143,
        'whittier': 127,
    },
    'march_2020': {
        'five_points': 477,
        'highland': 289,
        'union_station': 234,
        'capitol_hill': 205,
        'sunnyside': 152,
        'west_colfax': 146,
        'gateway-green_valley_ranch': 145,
        'speer': 144,
        'west_highland': 143,
        'cbd': 126,
    },
    'april_2020': {
        'five_points': 414,
        'highland': 287,
        'capitol_hill': 196,
        'union_station': 182,
        'gateway_-_green_valley_ranch': 147,
        'sunnyside': 145,
        'speer': 142,
        'west_highland': 142,
        'west_colfax': 129,
        'berkeley': 122,
    },
    'may_2020': {
        'five_points': 367,
        'highland': 258,
        'union_station': 213,
        'capitol_hill': 183,
        'gateway_-_green_valley_ranch': 146,
        'speer': 131,
        'west_highland': 130,
        'cbd': 129,
        'sunnyside': 126,
        'west_colfax': 116,
    },
    'june_2020': {
        'five_points': 377,
        'highland': 266,
        'capitol_hill': 182,
        'union_station': 169,
        'gateway_-_green_valley_ranch': 149,
        'west_highland': 136,
        'speer': 133,
        'cbd': 132,
        'sunnyside': 123,
        'berkeley': 117,
    }
}

df_filtered = may_2020_df[may_2020_df['price']<9000]
df_filtered['price'].sort_values(ascending = False).head(20)
may_2020_pricing_filtered = df_filtered.groupby('room_type')
may_2020_pricing_filtered.describe()176.366153


# THIS WORKED --- PREP FOR VIOLIN PLOT
hotel_prices = feb_2020_filtered[feb_2020_filtered['room_type']=='Hotel room']
print(len(hotel_prices.loc[0:, 'price']))

shared_prices = feb_2020_filtered[feb_2020_filtered['room_type']=='Shared room']
new_shared_price = shared_prices.loc[0:, 'price']
shared_prices_list = list(new_shared_price)
print(len(shared_prices_list))