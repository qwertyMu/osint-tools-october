

# username = "albionLives"
# followers = 1500
# recent_tweet = "England for the English"

# followers += 500

# print(followers)




# import datetime
 
# FirstName = "Tommy Robinson"
# DoB = datetime.datetime(1982, 11, 27)
# Email = "topbulldog@albionlives.com"
# Username = Email.split("@")[0]
# Nickname = "Robbo"
# Age = 42
# Occupation = "Scum"
# Followers = 1500
# Following = 2345
# Recent_Tweet = "England for English"
 
# Followers += 500
# Difference = Following-Followers
 
# print(Followers)
# print(Difference)
# print(Username) #Expected Output: topbulldog



# This splits the email variable by the @ symbol and prrints the first part of the resulting string
# email = "topbulldog@albionlives.com"
# username = email.split("@")[0]
# print(username) #Expected Output: topbulldog




# pairs_of_trainers = 3
# pairs_of_boots = 2

# pairs_of_shoes = pairs_of_trainers + pairs_of_boots

# print(pairs_of_shoes)



# users = 20
# using = 10
# percentage = (using / users) * 100
# print(percentage)

# balance = 3.80
# chocolate_bar = 1.20
# new_balance = balance - chocolate_bar

# print("You had: " + str(balance) + ", Now you have: " + str(new_balance))



# name = "Alice"
# age = 30
# # print("Name: " + str(name) + " Age: " + str(age))

# print(f"Name: {name}, Age: {age}")




# keywords_found = 3
# near_sensitive_location = True
# print(f"{keywords_found}, keywords have been found. The suspect has been found in a sensitive location = {near_sensitive_location}")
# # Note the commas






# # Creating a list of suspicious usernames
# suspicious_usernames = ["user123", "anonymous_456", "strangeUser789"]
# print()
# print("Initial list:", suspicious_usernames)
# print()

# # Appending a new suspicious username
# suspicious_usernames.append("newSuspiciousUser")
# print()
# print("After appending:", suspicious_usernames)
# print()

# # Counting occurrences of a specific username
# count = suspicious_usernames.count("anonymous_456")
# print()
# print("Occurrences of 'anonymous_456':", count)
# print()

# # Inserting a high-priority username at the start of the list
# suspicious_usernames.insert(0, "highPriorityUser")
# print()
# print("After inserting high-priority username:", suspicious_usernames)
# print()

# # Removing a specific username by value
# suspicious_usernames.remove("anonymous_456")
# print()
# print("After removing 'anonymous_456':", suspicious_usernames)
# print()







# hashtags = ["#ConflictZone", "#BreakingNews", "#Alert", "#Crisis"]

# for tag in hashtags:
#     print("Monitoring:", tag)



# count = 1

# while count >= 10:
#     print(f"Sus activity count: {count}")
#     count += 1

# List of Posts
# Posts = [
#     "Loving the #sunshine and #beach vibes.",               # First Post with two safe hashtags
#     "Planning something with #explosives haha #bomb",       # Second Post with two dangerous hashtag
#     "Lets create #chaos in the streets! #sunshine"          # Third Post with one dangerous hashtag and one safe hashtag
#     "I want to #bomb the Councils office"                   # Fourth Post with one dangerous hashtag
# ]

# # List of Hashtags to Count
# Hashtags = ["#sunshine", "#explosives", "#chaos", "#bomb"]
# Safe_Hashtags = ["#sunshine"]                               # Safe Hashtags we want to keep track of
# Dangerous_Hashtags = ["#explosives", "#chaos", "#bomb"]     # Dangerous Hashtags we want to keep track of

# # Create a dictionary to store the count of each hashtag, starting at 0
# Safe_Counts = {"#sunshine": 0}
# Dangerous_Counts = {"#explosives": 0, "#chaos": 0, "#bomb": 0}

# # Loop through each post in the list of posts
# for Post in Posts:
#     # Loop through each Safe Hashtag we are tracking
#     for Safe_Hashtag in Safe_Hashtags:
#         # Check if the current Hashtag is in the current post
#         if Safe_Hashtag in Post:
#             Safe_Counts[Safe_Hashtag] += 1  # Increment the Safe Count by 1 for this Hashtag
#     # Loop through each Dangerous Hashtag we are tracking
#     for Dangerous_Hashtag in Dangerous_Hashtags:
#         # Check if the current Hashtag is in the current post
#         if Dangerous_Hashtag in Post:
#             Dangerous_Counts[Dangerous_Hashtag] += 1  # Increment the Dangerous Count by 1 for this Hashtag

# # Calculate total counts
# Total_Count = sum(Safe_Counts.values()) + sum(Dangerous_Counts.values())

# # Print the Final counts for each Hashtag
# print("Safe Hashtag counts:", Safe_Counts, 
#       "Safe percentage of Hashtags used:", round((sum(Safe_Counts.values()) / Total_Count) * 100, 2),"%")
# print("Dangerous Hashtag counts:", Dangerous_Counts, 
#       "Dangerous percentage of Hashtags used:", round((sum(Dangerous_Counts.values()) / Total_Count) * 100, 2), "%")




# transaction_amount = 1200 # Amount in £
# risk_threshold = 000
# if transaction_amount > risk_threshold:
#     print("High-risk transaction detected!")
# else:
#     print("Transaction is within the safe limit.")



# keyword_detected = True
# late_night_activity = True
# if keyword_detected and late_night_activity:
#     print("Suspicious activity detected!")
# else:
#     print("No immediate threat.")



# suspicious_score = 0
# suspicious_posts = 3
# suspicious_transactions = 2
# suspicious_score += suspicious_posts * 10 
# suspicious_score += suspicious_transactions * 20 
# print("Suspicious Score:", suspicious_score)



