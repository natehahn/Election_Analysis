# Election Analysis

## Project Overview
A Colorado Board of Elections employee, TOM, provided the attached spreadsheet to complete the following tasks in support of the local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data sheet: election_results.csv
- Software: Python 3.10, Visual Studio 1.73

## Summary
The analysis of the election are as follow:
- There were 367, 711 total votes
- The cadidates were:
    - Dianna DeGette
    - Charles Casper Stockham
    - Raymon Anthony Doane
- Candidate results were:
    - Dianna DeGette received 73.8% of the vote with 272,892 votes
    - Charles Casper Stockham received 23.0% of the vote with 85,213 votes
    - Raymon Anthony Doane received just 3.1% of the vote with 11,606 votes
- The winner of the election was:
    - Dianna Degette by a comfortable margin

## Challenge Overview

In this challenge, Tom requested that we also include county specific results for the election.  This allowed the election commision to identify where favor was for each candidate.

# Summary of Challenge
The analysis of county data was as follows:
- Three counties were included in this election:
   - Arapahoe
   - Denver
   - Jefferson
-  County results were:
    - Arapahoe voters had 6.7% of the total vote with 24801 votes.
    - Denver voters had 82.8%  of the total votes with 306055 votes.
    - Jefferson voters had 10.5% of the total votes with 38855 votes.
-  The largest voter turnout by far was Denver county.

## Final Thoughts
I believe this code accomplished what you were looking for.  The great thing about the code is that it could be used for any election with any amount of voters.  If you were interested in pulling more statistics, like voter demographics by age or race.  Simplying adding that data field to the spreadsheet and applying another for loop will allow you to add add this analysis.  Duplicating the code that is already there with new variables for age, variables to hold the count of all ages, and dictionaries to hold the ages of individuals.  Finally, a if-elif statement to place individuals into an age group for easier referencing.  
