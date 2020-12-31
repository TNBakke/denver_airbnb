# EDA

# Standard Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Function to determine airbnb quantities over time

def get_total_airbnb_quan(file_path):
    ''' 
    Calculates total quantity of Airbnb Rentals for month

    Parameters: 
    file_pate (str): Direct File Path to dataset

    Returns: 
    airbnb_quan (int): Total Number of Airbnb Rental Units
    
    '''
    
    df = pd.read_csv(file_path)

    airbnb_quan = df['id'].count()

    return airbnb_quan

total_airbnb_quan_dict = {}

# Add Results to Dict in Order to Keep Track of Total Listings per Month

def update_total_quan_dict(date_, airbnb_quan):
    '''
    Updates total_airbnb_quan_dict with Month and Quantity totals

    Parameters:

    date_ (str): The month and year the data was collected (i.e. 'jan_2020')
    airbnb_quan (int): The total number of Airbnb Rental Units for the Month and Year 
                       (Note: See 'get_total_airbnb_quan(file_path)' function above)

    Returns:
    total_airbnb_quan_dict (dict): Updated copy of the Airbnb Quantity Dictionary for data storage

    '''
    
    total_airbnb_quan_dict[date_] = airbnb_quan

    return total_airbnb_quan_dict


# Function to see Denver Airbnb rental listing broken down by rental type

def rental_breakdown(date_, file_path):
    '''
    Collects the rental type breakdown for the desired month of data

    Parameters:
    file_path (str): Direct file path to desired dataset 
    date_ (str): The month and year the data was collected (i.e. 'jan_2020')

    Returns:
    rental_type_dict (dict): New dictionary including breakdown of data by type of rental

    '''

    df = pd.read_csv(file_path)
    df_grouped = df.groupby('room_type').count()
    df_grouped_new = df_grouped[['id']]
    
    rental_type_dict = df_grouped_new.to_dict()

    rental_type_dict[date_] = rental_type_dict.pop('id')

    return rental_type_dict

# Function to show Top 10 neighborhoods currently have the most Airbnb listings

def neighborhood_breakdown(date_, file_path, top_num = 10):
    '''
    Collects the results of the Top Num Airbnb Rental Neighborhoods for the desired Month

    Parameters:
    file_path (str): Direct file path to desired dataset 
    date_ (str): The month and year the data was collected (i.e. 'jan_2020')

    Returns:
    neighborhood_d (dict): New dictionary including breakdown of Top 10 neighborhoods

    '''

    df = pd.read_csv(file_path)
    df_grouped = df.groupby('neighbourhood').count()
    
    new_d = dict(df_grouped['id'].sort_values(ascending = False).head(top_num))

    new_d = {k.lower(): v for k,v in new_d.items()}
    new_d = {k.replace(" ","_"): v for k,v in new_d.items()}

    neighborhood_d = {date_ : new_d}

    return neighborhood_d

# Function to calculate distribution of pricing for each rental type

    def price_breakdown_by_type(file_path):
        '''
        Collects the prices for all Airbnb listings in a month and appends them to a list for plotting

        Parameters:
        file_path (str): Direct file path to desired dataset 

        Returns: 
        pricing_d (dict): Returns a Dictionary with all prices broken out by rental type. See info below on lists.
        
        entire_unit_price_list (list): Returns a list of integers with all prices for entire unit rentals
        private_room_price_list (list): Returns a list of integers with all prices for private room rentals
        hotel_price_list (list): Returns a list of integers with all prices for hotel rentals
        shared_room_price_list (list): Returns a list of integers with all prices for shared room rentals
        '''

        df = pd.read_csv(file_path)
        
        hotel_prices = df[df['room_type']=='Hotel room']
        new_hotel_price = hotel_prices.loc[0:, 'price']
        hotel_price_list = list(new_hotel_price)

        entire_unit_prices = df[df['room_type']=='Entire home/apt']
        new_entire_unit_price = entire_unit_prices.loc[0:, 'price']
        entire_unit_price_list = list(new_entire_unit_price)

        shared_prices = df[df['room_type']=='Shared room']
        new_shared_price = shared_prices.loc[0:, 'price']
        shared_room_price_list = list(new_shared_price)

        private_prices = df[df['room_type']=='Private room']
        new_private_price = private_prices.loc[0:, 'price']
        private_room_price_list = list(new_private_price)

        # Creating a dictionary with keys being rental types and values being price list 
        pricing_d = {'entire_unit':entire_unit_price_list, 'private_room':private_room_price_list, 
             'hotel':hotel_price_list, 'shared_room':shared_room_price_list}
        

        return pricing_d
    
# Function to see which neighborhoods charge the most per listing

    def top_10_neighborhood_prices(file_path):
        '''
        Collects the highest average prices for the Top 20 Denver Neighborhoods for a desired month

        Parameters:
        file_path (str): Direct file path to desired dataset 

        Returns:
        neighb_pricing_d (dict): Returns a Dictionary with the neighborhoods as keys and the values as
        average rental price for the desired month
        '''

        df = pd.read_csv(file_path)

        df_group = df.groupby('neighbourhood')

        neighb_pricing_d = dict(df_group['price'].mean().sort_values(ascending=False).head(10))

        return neighb_pricing_d

# Function to see what is the current occupancy rate for Airbnb in Denver?

    def occupancy_rate(file_path):
        '''
        Computes the occupancy rate of the Airbnb rentals for the desired month

        Parameters:
        file_path (str): Direct file path to desired dataset 

        Returns:
        occ_rate (float): Ratio of properties that are reserved vs. vacant (number between 0-1)
        '''

        df = pd.read_csv(file_path)

        occ_rate_df = df.groupby('available').count()
        occ_rate_d = dict(occ_rate_df['listing_id'])

        occ_rate = occ_rate_d['f']/(occ_rate_d['f'] + occ_rate_d['t'])

        return occ_rate
    
if __name__ == '__main__':
    
    get_total_airbnb_quan('./data/may_2016/2016_may_listings.csv')
    update_total_quan_dict('jan_2020', 2505)
    
    rental_breakdown('jan_2020','./data/jan_2020/jan_2020_listings.csv')

    neighborhood_breakdown('jan_2020','./data/jan_2020/jan_2020_listings.csv')
    
    price_breakdown_by_type('./data/jan_2020/jan_2020_listings.csv')

    top_10_neighborhood_prices('./data/feb_2020/feb_2020_listings.csv')

    occupancy_rate('./data/denver_airbnb_2019/calendar.csv')

    