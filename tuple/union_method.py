school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

school_set = set(school_friends)

all_friends_union = school_set.union(college_friends)

print("\nAll friends (Set union method):", list(all_friends_union))