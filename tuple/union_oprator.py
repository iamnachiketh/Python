school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

school_set = set(school_friends)
college_set = set(college_friends)

all_friends = school_set | college_set

print("\nAll friends (Set | operator):", list(all_friends))