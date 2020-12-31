
# Standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 22, 'font.family': 'sans'})


# Dictionary for Denver airbnb quantities over the months

int_den_airbnb_listing_totals_new = {
     1: 3918, 6: 4412, 9: 4853, 10: 4984, 11: 5089, 12: 5105, 13: 5222, 14: 5106, 15: 4766,
     16: 4808, 17: 4668, 18: 4686, 19: 4659, 20: 4511, 21: 4588, 22: 4541, 23: 4601, 24: 4794,
     25: 4865, 26: 4964, 27: 4860, 28: 4951, 29: 4868, 30: 4478, 31: 4256, 32: 4200
    }

# Months of airbnb data for plot x labels

lst2_new =[ '11/17', '12/17','01/18','02/18','03/18','04/18','05/18','06/18','07/18',
            '08/18','09/18','10/18','11/18','12/18','01/19','02/19','03/19','04/19',
            '05/19','06/19','07/19','08/19','09/19','10/19','11/19','12/19','01/20',
            '02/20','03/20','04/20','05/20','06/20' ]

# Setting x-ticks 
lst1_new = np.arange(1,33)

def airbnb_quan_plot():
    fig, ax = plt.subplots(figsize=(20,10))
    ax.set_title("Denver Airbnb Rental Listing Quantities")
    plt.rcParams['figure.dpi'] = 400

    for k,v in int_den_airbnb_listing_totals.items():
        x = int_den_airbnb_listing_totals_new.keys()
        y = int_den_airbnb_listing_totals_new.values()
        plt.plot(x,y, color = 'blue')

    plt.rcParams.update({'font.size': 22})
    plt.xticks(ticks = lst1_new, labels = lst2_new)
    plt.xticks(rotation=70)
    plt.ylabel("Quantity of Airbnb Listings")
    plt.xlabel("Date (MM/YY)")
    # Plotting a Vertical Line to Represent COVID-19 lockdown start
    ax.axvline(29.5, color='red', linestyle='--', linewidth=1)
    plt.text(29.6, 2600, 'COVID-19 Lockdown', color = 'red', rotation=90)
    plt.tight_layout()
    plt.ylim(2000)
    plt.show()


def rental_breakdown_plot_quarterly (month_dict1, month_dict2, month_dict3):
    # Computing the totals for each rental room type for the desired quarter
    total_quan = test_dict[month_dict1]['total']+test_dict[month_dict2]['total']+test_dict[month_dict3]['total']
    total_entire_unit = test_dict[month_dict1]['entire_unit']+test_dict[month_dict2]['entire_unit']+test_dict[month_dict3]['entire_unit']
    total_hotel_room = test_dict[month_dict1]['hotel_room']+test_dict[month_dict2]['hotel_room']+test_dict[month_dict3]['hotel_room']
    total_private_room = test_dict[month_dict1]['private_room']+test_dict[month_dict2]['private_room']+test_dict[month_dict3]['private_room']
    total_shared_room = test_dict[month_dict1]['shared_room']+test_dict[month_dict2]['shared_room']+test_dict[month_dict3]['shared_room']

    # Computing the ratios for each room type
    entire_unit_ratio = total_entire_unit / total_quan  
    hotel_room_ratio = total_hotel_room / total_quan
    private_room_ratio = total_private_room / total_quan
    shared_room_ratio = total_shared_room / total_quan

    x_values = ['Entire Home/Apt', 'Private Room', 'Shared Room', 'Hotel Room']
    y_values = [entire_unit_ratio, private_room_ratio, shared_room_ratio, hotel_room_ratio]

    fig, ax = plt.subplots(figsize=(20,10))
    plt.rcParams['figure.dpi'] = 400
    plt.rcParams.update({'font.size': 22}) 

    x = len(x_values)
    ax.bar(x_values,y_values)
    ax.set_xticklabels(x_values)
    ax.set_title('Breakdown of Denver Airbnb Rentals (Q1 2020)')
    ax.set_xlabel('Type of Airbnb Rental')
    ax.set_ylabel('Ratio of Rental Types')   
    plt.show();

#Plotting pricing distrubtion for a desired month by room type

def price_distribution(file_path):
    df = pd.read_csv(file_path)
    df['price'].sort_values(ascending = False).head(20)
    
    # Eliminating  Outliers
    df_filtered = df[df['price']<9000]
    
    # Gathering pricing data as list for Hotels
    hotel_prices = df_filtered[df_filtered['room_type']=='Hotel room']
    new_hotel_price = hotel_prices.loc[0:, 'price']
    hotel_prices_list = list(new_hotel_price)

    # Gathering pricing data as list for Shared Rooms
    shared_prices = df_filtered[df_filtered['room_type']=='Shared room']
    new_shared_price = shared_prices.loc[0:, 'price']
    shared_prices_list = list(new_shared_price)

    # Gathering pricing data as list for Private Rooms
    private_room_prices = df_filtered[df_filtered['room_type']=='Private room']
    new_private_price = private_room_prices.loc[0:, 'price']
    private_room_prices_list = list(new_private_price)

    # Gathering pricing data as list for Entire Home 
    entire_home_prices = df_filtered[df_filtered['room_type']=='Entire home/apt']
    new_entire_home_price = entire_home_prices.loc[0:, 'price']
    entire_home_prices_list = list(new_entire_home_price)

    # Now that all information is gathered. Time to plot the results

    room_types = ['Hotel Room', 'Shared Room', 'Private Room', 'Entire Home/Apt']

    fig, ax = plt.subplots(figsize=(20,10))
    plt.rcParams['figure.dpi'] = 400
    plt.rcParams.update({'font.size': 22})

    room_type_prices = [hotel_prices_list, shared_prices_list, private_room_prices_list, entire_home_prices_list]

    ax.set_title("Pricing Distribution by Airbnb Rental Room Type")
    ax.set_ylabel("Airbnb Rental Type")
    ax.set_xlabel("Pricing of Rental Unit per Night")
    # Setting X-Axis Limit to accentuate the distribution curves 
    ax.set_xlim(0,1000)
    ax.set_yticks(np.arange(1, len(room_types) + 1))
    ax.set_yticklabels(room_types)
    fig.tight_layout()
    ax.violinplot(room_type_prices, vert=False, showmeans=True)
    plt.show()

# Plotting which Denver Neighborhoods have the most listings

def top_neighborhoods(month_dict1, month_dict2, month_dict3):

    x = np.arange(len(top_neighbs))

    y_2018 = month_dict1.values()
    y_2019 = month_dict2.values()
    y_2020 = month_dict3.values()

    top_neighbs = month_dict1.keys()

    width = 0.2

    fig, ax = plt.subplots(figsize=(20,10))

    plt.rcParams['figure.dpi'] = 400
    plt.rcParams.update({'font.size': 22}) 
    ax.bar(x-(width), y_2018, width, color='b')
    ax.bar(x, y_2019, width, color='orange')
    ax.bar(x+(width), y_2020, width, color='green',)
    ax.set_xticks(x)
    ax.set_xticklabels(top_neighbs)
    #Adjust the Title as Desired
    ax.set_title('Top 5 Airbnb Rental Neighborhoods (2018-2020)')
    ax.set_xlabel('Denver Neighborhoods')
    ax.set_ylabel('Quantity of Airbnb Listings')
    plt.xticks(rotation=70)
    
    # If using different years you will need to change legend below
    fig.legend(labels=("2018","2019","2020"), loc='upper left')

    plt.show();


# Plotting which Denver Neighborhoods are Fastest Growing?

new_d = {}
for key, val in feb_2020_d.items():
    for k, v in feb_2019_d.items():
        if key == k:
            new_d[key] = val-v

# Sort the results of the dictionary in order to see which neighborhoods had the 
# largest change over the time period (positive numbers are growing)

neighb_list_grow = grow_neighb.keys()
neighb_increase = grow_neighb.values()


grow_neighb = {'Union Station': (246/148-1), 'Green Valley Ranch': (158/99-1) , 
              'Stapleton':(123/104-1) , 'West Colfax': (144/129-1) , 
              'Cheesman Park': (97/86-1) }

fig, ax = plt.subplots(figsize=(15,10))
plt.rcParams['figure.dpi'] = 400
# plt.rcParams.update({'font.size': 26})

ax.bar(neighb_list_grow, neighb_increase, color = 'g')
ax.set_title('Top 5 Fastest Growing Airbnb Neighborhoods from February 2019-2020')
ax.set_xlabel('Denver Neighborhoods')
ax.set_ylabel('Percent Growth')
plt.xticks(rotation=70)
# plt.tight_layout()

plt.show()


# Plotting which Denver Neighborhoods Charge the Highest Listing Price?

def top_5_airbnb_neighb_price(file_path):

    df = pd.read_csv(file_path)

    neighb_price_d = dict(df['price'].mean().sort_values(ascending=False).head(5))

    neighb_list = neighb_price_d.keys()
    neighb_price_list = neighb_price_d.values()

    fig, ax = plt.subplots(figsize=(15,10))
    plt.rcParams['figure.dpi'] = 400
    plt.rcParams.update({'font.size': 22})

    ax.bar(neighb_list, neighb_price_list, color = 'b')
    ax.set_title('Top 5 Airbnb Neighborhood Average Rental Price')
    ax.set_xlabel('Denver Neighborhoods')
    ax.set_ylabel('Average Rental Price')
    plt.xticks(rotation=70)

    plt.show()