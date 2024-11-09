#explaination
#took help for dictionary, need to revise dicts

def max_training_items(N, items):
    # Create a dictionary to count occurrences of each word
    # for both spam (1) and non-spam (0) cases
    word_counts = {}
    
    # Process each item
    for word, is_spam in items:
        if word not in word_counts:
            word_counts[word] = {0: 0, 1: 0}
        word_counts[word][is_spam] += 1
    
    # For each word, we can take all occurrences of either spam
    # or non-spam (whichever is more frequent)
    max_items = 0
    for counts in word_counts.values():
        max_items += max(counts[0], counts[1])
    
    return max_items




for _ in range(int(input())):
    N = int(input())  # Number of items in dataset
    items = []
    
    # Read each item
    for _ in range(N):
        word, spam = input().split()
        items.append((word, int(spam)))
    
    # Process this test case
    result = max_training_items(N, items)
    print(result)

# code submitted 

# def f(n, arr):
#    d = {}
#    for w, s in arr:
#        if w not in d:
#            d[w] = {0: 0, 1: 0}
#        d[w][s] += 1
   
#    r = 0
#    for v in d.values():
#        r += max(v[0], v[1])
#    return r

# for _ in range(int(input())):
#    n = int(input())
#    arr = []
#    for i in range(n):
#        x, y = input().split()
#        arr.append((x, int(y)))
#    print(f(n, arr))