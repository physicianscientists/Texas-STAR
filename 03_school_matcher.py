import os
import pandas as pd
pd.set_option('max_colwidth', 400)  #wider pandas columns upon render
import numpy as np
from itertools import islice
from thefuzz import fuzz
from datetime import date
import warnings
warnings.filterwarnings("ignore")  #ignoring warning messages from pandas


def data_importer():
    """
    Function to import 3 dataframes:
    1. a df of all Texas STAR residency programs
    2. a df of unmatched Texas STAR residency programs
    3. a df of all programs/specialties in doximity with their rankings
    """
    
    # Importing dataframes 
    star = pd.read_csv("tables/texasSTAR_unique_programs.csv")
    unmatched = pd.read_csv("tables/unmatched_unique_programs.csv")
    dox = pd.read_excel("tables/doximity_rankings.xlsx")
    
    # Optional filter for specialties that I already matched
    #specialties = ["Anesthesiology", "Child Neurology", "Dermatology", "Emergency Medicine", "Family Medicine", "Internal Medicine"]
    unmatched = unmatched[unmatched["specialty"]=="Vascular Surgery"]  #change accordingly
    
    print(star.head())
    print(unmatched.head())
    print(dox.head())
    return star, unmatched, dox



def program_matcher(unmatched, dox):
    """
    Function to perform fuzzy string matching and user selection.
    Matches unmatched Texas STAR programs with those in doximity, while filtering things down by specialty
    Type 'done' to finish
    Returns a dataframe 
    """
    
    match_list = []
    for index, row in unmatched.iterrows():
        
        # Programs and specialties from Texas STAR
        program = row["program"]
        specialty = row["specialty"]
        
        # Filtering doximity by specialty and getting a unique list of specialties
        dox_filt = dox[dox["specialty"].isin(["Vascular Surgery", "Surgery"])]  #==specialty change this
        dox_filt = dox_filt["program"].unique()
        
        # Looping over each specialty and appending fuzzy string match scores
        ratio = []
        partial_ratio = []
        sort_ratio = []
        set_ratio = []
        partial_token = []
        dox_program_list = []
        for dox_program in dox_filt:
            ratio.append(fuzz.ratio(program, dox_program))
            partial_ratio.append(fuzz.partial_ratio(program, dox_program))
            sort_ratio.append(fuzz.token_sort_ratio(program, dox_program))
            set_ratio.append(fuzz.token_set_ratio(program, dox_program))
            partial_token.append(fuzz.partial_token_sort_ratio(program, dox_program))
            dox_program_list.append(dox_program)
        
        # Making a dataframe and displaying to top 10 matches
        df = pd.DataFrame({"ratio": ratio, "partial_ratio": partial_ratio, "sort_ratio": sort_ratio, "set_ratio": set_ratio, "partial_token": partial_token, "dox_program": dox_program_list})
        df["star_program"] = program
        df["specialty"] = specialty
        df["mean_ratio"] = df[["ratio", "partial_ratio", "sort_ratio", "set_ratio", "partial_token"]].mean(axis=1)
        df = df.sort_values("mean_ratio", ascending=False).reset_index(drop=True)
        max_ratio = max(df["mean_ratio"])
        df_print = df.iloc[:, 5:9]
        print(df_print.head(10))
        
        # User selection of the top match and appending the matched selection to the match list
        # If there is an exact match, pick the selection automatically to speed things up
        if max_ratio>=97.0:
            matched_df = pd.DataFrame(df.iloc[0]).transpose()
            match_list.append(matched_df)
        else:
            selection = input("\nSelect the top match by index: ")
            if selection=="done":
                print("\nfinished with looping")
                break
            try:
                selection = int(selection)
                matched_df = pd.DataFrame(df.iloc[selection]).transpose()
                match_list.append(matched_df)
            except:
                unmatched_df = pd.DataFrame({"ratio": np.nan, "partial_ratio": np.nan, "sort_ratio": np.nan, "set_ratio": np.nan, "partial_token": np.nan, "dox_program": program, "star_program": program, "specialty": specialty, "mean_ratio": "unable to match"}, index=[0])
                match_list.append(unmatched_df)

    # Concatenating and returning the df
    df_total = pd.concat(match_list)
    return df_total



def data_exporter(df):
    """
    Function to export the dataframe with today's date and user input for specialty
    """
    user_input = input("\nWhich Specialties did you run this on (underscore separated): ")
    today = str(date.today())
    filename = today + "_" + user_input
    df.to_excel("dox_matching/" + filename + ".xlsx", index = False)



# Executing the script
if __name__ == "__main__":
    star, unmatched, dox = data_importer()
    df_total = program_matcher(unmatched=unmatched, dox=dox)
    data_exporter(df=df_total)
    print("Done with Script!")