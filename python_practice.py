numbers = [0, 1, 2, 3, 4]

for num in numbers:

    print(num)



for num in range(10):

    print(num)

#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#Arapahoe county has 369237 registered voters.
#Denver county has 413229 registered voters.
#Jefferson county has 390222 registered voters.'

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#You received 265489 number of votes. The total number of votes in the election was 2345689. You received 11.32% of the total votes.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# The time right now is 2019-09-18 14:11:42.394131