school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

school_set = set(school_friends)
college_set = set(college_friends)

common_friends_set = school_set & college_set

print("\nCommon friends (Set & operator):", list(common_friends_set))