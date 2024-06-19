"""
create a DataFrame with vendor details for cuisines that have
"Tomato Sauce" as an ingredient and vendors with a rating above 4.
"""

import pandas as pd
import json

def filter_rating_ingredient(file_path, rating, ingredient):
    # Load the JSON data from file
    with open(file_path) as file:
        json_data = json.load(file)

    # Normalize the JSON data into a flat table
    df = pd.json_normalize(
        data=json_data,
        record_path=['cuisines', 'ingredients', 'vendors'],
        meta=[
            ['hotel', 'name'],
            ['hotel', 'rating'],
            ['hotel', 'contact'],
            ['cuisines', 'name'],
            ['cuisines', 'ingredients', 'name']
        ],
        errors='ignore'
    )

    # Rename columns for clarity
    df.rename(columns={
        'hotel.name': 'hotel_name',
        'hotel.rating': 'hotel_rating',
        'hotel.contact': 'hotel_contact',
        'cuisines.name': 'cuisine_name',
        'cuisines.ingredients.name': 'ingredient_name'
    }, inplace=True)

    # Convert vendor_rating to numeric
    df['rating'] = pd.to_numeric(df['rating'])

    # Filter dataframe for vendors with a rating above 4 and "Tomato Sauce" as an ingredient
    filtered_df = df[
        (df['ingredient_name'] == ingredient) &
        (df['rating'] > rating)
    ]

    # Select relevant columns
    filtered_df = filtered_df[['cuisine_name', 'name', 'rating', 'contact']]

    return filtered_df

if __name__ == '__main__':
    result = filter_rating_ingredient(
        file_path='data.json',
        rating=4,
        ingredient="Tomato Sauce"
    )
    print(result)

