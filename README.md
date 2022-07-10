### **Written Analysis of the Election Audit**

## **Overview of Election Audit**

The local election council has approached our team with the request of creating automated code that can process election data in CSV format and output the following:
		1) Total Votes
		2) Breakdown of votes per county
		3) County with the largest number of votes
		4) Breakdown each candidate by;
			A) Name B) Number of votes received C) Percentage of overall votes
		5) Breakdown winning candidate results by;
			A) Name B) Number of votes received C) Percentage of overall votes
	
## **Election-Audit Results**
- How many votes were cast in this congressional election?
  - 369,711	
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  -County Votes:
  -Jefferson: 10.5% (38,855)
  -Denver: 82.8% (306,055)
  -Arapahoe: 6.7% (24,801)
			
- Which county had the largest number of votes?
    -Largest County turnout: Denver
			
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  -Charles Casper Stockham: 23.0% (85,213)
  -Diana DeGette: 73.8% (272,892)
  -Raymon Anthony Doane: 3.1% (11,606)
			
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  -Winner: Diana DeGette
  -Winning Vote Count: 272,892
  -Winning Percentage: 73.8%
			
		
## **Election-Audit Summary**

Our solution code for this task was able to process the data within seconds and print the outputs in less than a second.
One of the major advantages of this code is that it’s scope can be easily expanded or retracted or restructured for different types of elections
	1) Change the codes scope: As an example, we can easily update the codes to output state-level breakdowns instead of county level.
		○ Replace "county" variables to "state"
			§ largest_county to largest_state
			§ largest_county_summary to largest_state_summary
			§ county_count to state_count
			§ County_name to state_name
	2) Utilize code for legislation votes: This code can also be modified to process yes/no/abstain votes with minimal tweaking. The change in code required to make this possible would be;
		○ Update "candidate" variables to "options"
			§ candidate_name to option_name
			§ candidate_options to options_list
			§ candidate_votes to option_votes
