#001_friendships.py - "network metric degree of centrality"

#list of users, each represented by a dictionary that contains
#that user's id and name
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

#with given friendship pairs
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (8, 9) ]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j) # add j as a friend of user i
    friendships[j].append(i) # add i as a friend of user j

def number_of_friends(user):
    """How many friends does _user_have"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                        for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

#Create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user))
                           for user in users]

num_friends_by_id.sort(
    key = lambda id_and_friends: id_and_friends[1],
    reverse = True)

# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

#--------------------------------------------------------
# Data Scientists you may know
def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print(friendships[0]) # [1, 2]
print(friendships[1]) # [0, 2, 3]
print(friendships[2]) # [0, 1, 3]

from collections import Counter
from csv import unregister_dialect
from email.policy import default

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]   # for each of my friends,
        for foaf_id in friendships[friend_id]   # find their friends
        if foaf_id != user_id                   # who aren't me
        and foaf_id not in friendships[user_id] # and aren't my friends
    )

print(friends_of_friends(users[3]))             # Counter({0: 2, 5: 1})

#--------------------------------------------------------
# identify users with similar interests.

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (1, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"), 
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), 
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++")
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"), 
    (6, "probability"), (6, "mathematics"), (6, "theory"), 
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), 
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), 
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return[user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]

# build an index from interests to users
from collections import defaultdict

# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Build an index between users and interests
# Keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

#--------------------------------------------------------
# Salaries and Experience

salaries_and_tenures = [(83000, 8.7), (88000, 8.1)
                        (48000, 0.7), (76000, 6)
                        (69000, 6.5), (76000, 7.5)
                        (60000, 2.5), (83000, 10)
                        (48000, 1.9), (63000, 4.2)]

# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# group together the salaries corresponding to each bucket
# Keys are tenure buckets, values are lists of salaries for that bucket.
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# compute the average salary for each group
# Keys are tenure buckets, values are average salary for that bucket.
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
