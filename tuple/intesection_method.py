school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

school_set = set(school_friends)

common_friends_intersection = school_set.intersection(college_friends)

print("\nCommon friends (Set intersection method):", list(common_friends_intersection))