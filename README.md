# Pokemon Dataset - Data Cleaning Project

## What this project does
Cleans a raw 800-row Pokemon dataset from Kaggle using Python and Pandas.

## Problems found in the raw data
- Mega Evolution names were broken (e.g. "VenusaurMega Venusaur")
- 386 missing values in Type 2 column
- Inconsistent column names (#, Sp. Atk, Sp. Def)
- Total stats column missing

## What was fixed
- Wrote a custom function to fix all Mega Evolution names
- Replaced missing Type 2 values with "None"
- Renamed all columns to clean snake_case
- Added a Total_stats column combining all 6 stats

## Tools used
Python, Pandas

## Dataset source
https://www.kaggle.com/datasets/abcsds/pokemon
