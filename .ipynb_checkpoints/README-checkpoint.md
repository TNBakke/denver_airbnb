# Denver Airbnb Market Analysis for Potential Investment Opportunity

## Motivation

Since moving to Denver about two years ago, I have been interested in investing in a local short-term rental property. The potential cash flow generated from a optimally located and priced rental sounds very appealing. I have spoken to several people who have or had Airbnb rental properties, but nobody in the Denver market. Additionally, when you speak to people who have had short-term rentals with Airbnb it usually encites an emotional and biased response about their specific experiences. So, when I found the Denver Airbnb datasets I thought this would be the perfect opportunity to delve in to the data and come up with my own unbiased analysis. 

## Airbnb History

The pioneer of the short-term vacation rental property marketplace, Airbnb, was founded in 2008 in San Francisco, CA. Airbnb was conceived after its founders rented out an air mattress in their living room, effectively turning their apartment into a bed and breakfast, to offset the high cost of rent in San Francisco. The company name "Airbnb" is a shortened version of its original name, AirBedandBreakfast.com. Over the years, the Airbnb marketplace has expanded rapidly and currently has rentals in 81,000 cities and 191 countries throughout the world. On August 19, 2020, Airbnb announced that it had filed for an initial public offering (IPO) and the company has been privately valued at 31 billion USD.

(SOURCE: https://en.wikipedia.org/wiki/Airbnb)

## Denver Airbnb Market Data

The 'Inside Airbnb' project compiled the Denver Airbnb datasets I used for my research and they have hundreds of other cities across the world to analyze (See project details here: http://insideairbnb.com/get-the-data.html). The data was scraped from Airbnb's website and the first dataset was published in May 2016. However, the second Denver Airbnb dataset was not published until November 2017 which is a gap of approximately 1.5 years. After that, the data was collected and published at a much more consistant rate eventually being published every month starting in July 2018. Fortunately, the datasets that were published by 'Inside Airbnb' did not require much data munging as there were almost zero NaN values so I was able to focus the majority of my time on the analysis. The data included in each month's dataset includes the following CSV files: "listings.csv", "calendar.csv", "reviews.csv", and "neighborhoods.csv". I used the "listings.csv" files for the majority of my data analysis. However, I needed the "calendar.csv" to compute the average Devner Rental Occupancy Rate.   

## Investment Opportunity / Strategy

In order to feel confident in making the correct investment decision, there are many questions that need to be answered with the data. In my opinion, the most important questions that needed to be answered before seriously considering the investment are listed below:

* How has the Denver Airbnb Market changed over the years in terms of quantity of listings? -- DONE
* How does the Airbnb occupancy rate in Denver compare to U.S. Average? -- DONE
* What is the current breakdown of Airbnb Rental types in Denver? -- DONE
* What is the distribution of prices by each rental type? -- DONE
* What are the most popular Denver Airbnb Rental Neighborhoods? -- DONE
* Which Denver Airbnb Neighborhoods charge the most for listings?
* Which neighborhoods are growing the fastest in terms of rental properties? 
* Which Denver Airbnb listings are the most successful (i.e. have most user reviews) and where are they located?

## Quantity of Denver Airbnb Listings Through the Years

After analyzing the data from the available datasets, you can see that the quantity of Denver Airbnb Rentals increased from under 4,000 in November 2017 to a maximum of about 5,200 units in November 2018. It is worth noting that the quantity of Denver Airbnb Rentals in May 2016 was only 2,505 units, but since there was an 18 month gap between datasets, I decided not to include that value in my plot. That growth over the 18 month span is a 156% increase in rental units.  

**INSERT PLOT HERE**

## Average Occupancy Rate in Denver Compared to U.S. Average

To determine the average Occupancy Rate in the Denver market, I evaluated the "calendar.csv" files from March 2019 to March 2020 so I could get an accurate assessment of the market prior to the COVID-19 global pandemic (Note: The Dataset for March_2020 was scraped before lockdowns in the United States began). By taking the occupancy rates and averaging them out across 12 months it will ensure that I am capturing any fluctuations due to 'seaonality'. While researching online, I found a resource which calcuated the average Occupancy Rate across 500 cities in the U.S. to be about 48% (see source link below). From my analysis, Denver, Colorado's rental Occupancy Rate was a very high 62.1% (about 129% over the national average). 

(SOURCE: https://www.alltherooms.com/analytics/average-airbnb-occupancy-rates-by-city/)

**INSERT PLOT HERE -- TAKE PLOT FROM SOURCE ABOVE


## Current Breakdown of Airbnb Listings by Rental Type 

By analyzing the "listings.csv" file for the first quarter of 2020 (January, February, March), I was able to get an average breakdown of the current Devner Airbnb Market by type of room. As it turns out, the "Entire Home/Apartment" type of rental accounts for the vast majority of all Denver Airbnb rentals at 75%. After that, the "Private Room" rental type contributes to about 23.1% of the market. Then the "Shared Room" and "Hotel Room" rental types account for only 1.1% and 0.73%, respectively. 

## Which Denver Neighborhoods Have the Most Listings?
April 2018 Top 5: Five Points, Highland, Capitol Hill, Speer, Sunnyside
April 2019 Top 5: Five Points, Highland, Capitol Hill, Speer, Sunnyside
April 2020 Top 5: Five Points, Highland, Capitol Hill, Union Station, Green Valley Ranch


## Which Denver Neighborhoods are the Fastest Growing?


## Which Denver Neighborhoods Charge the Highest Listing Prices?


## Investment Risks / Changes to Market? i.e. Local Government Regulations?

1) https://www.airbnb.com/help/article/1404/denver-co

2) https://www.westword.com/news/denver-city-council-approves-new-rules-for-short-term-rentals-11678846

3) https://www.denvergov.org/content/denvergov/en/denver-business-licensing-center/business-licenses/short-term-rentals.html

4) https://www.avalara.com/mylodgetax/en/blog/2019/03/new-rules-for-denver-airbnbs-start-in-april.html

## COVID Impact Denver Airbnb Market? Less shared rooms/homes?


## Conclusion


## Future Analysis

- BONUS: Which rental properties have the most reviews? Why?
- BONUS: How Does Variation in Seasonality Affect Rental Rates?
- BONUS: Which Denver neighborhoods are the fastest growing with regard to rental quantities.
- BONUS: How has the Denver Airbnb occupancy rate changed over the years? 

