from os.path import join, dirname
import pandas as pd
import numpy as np
from pymongo import MongoClient
import re

"""

Use this file to read in the project nurse data, perform text pre-processing
and store data in mongo. The fields we're interested in storing are:

  'How many years of experience do you have?' -> experience,
  'What's your highest level of education?' -> education,
  'What is your hourly rate ($/hr)?' -> salary,
  'Department' -> department,
  'What (City, State) are you located in?' -> location,
  'What is the Nurse - Patient Ratio?' -> patientNurseRatio

Check server/models/Record.js for an example of the schema.

"""

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['clipboardinterview']
    df = pd.read_csv(join(dirname(__file__), '../data/projectnurse.csv'))
    
    #Part1
    df['What is your hourly rate ($/hr)?'] = df['What is your hourly rate ($/hr)?'].map(lambda x: re.sub(r'[A-Za-z$/()-,]', '', x))
        
    #Part3
    count = sum(x == 'Bachelors' for x in df["What's your highest level of education?"])
    print(count/df["What's your highest level of education?"].count())

    #Part2
    df['Department'] = pd.concat([df['Department'].astype(str).str.upper() for col in df.columns], axis=1)

    df = df[['Department','What (City, State) are you located in?']].groupby(['Department'])['What (City, State) are you located in?']\
            .count() \
            .reset_index(name='count') \
            .sort_values(['count'], ascending=False)\
            .head(10)
    print(df)
    print ('done')

if __name__ == "__main__":
    main()
