import heapq

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # Convert `a` to a max-heap by pushing negative values
    a = [-num for num in a]
    heapq.heapify(a)
    
    # Continue reducing the two largest elements until the condition breaks
    while True:
        # Get the two largest elements (least negative values in max-heap)
        largest1 = -heapq.heappop(a)
        
        # Check if there are not enough elements left in the heap
        if largest1 <= k:
            heapq.heappush(a, -largest1)
            break
        
        if a:
            largest2 = -heapq.heappop(a)
            
            if largest2 <= k:
                # If the second largest is <= k, push back the elements and stop
                heapq.heappush(a, -largest1)
                heapq.heappush(a, -largest2)
                break
            
            # Decrement both values
            largest1 -= 1
            largest2 -= 1
            
            # Push them back into the heap
            heapq.heappush(a, -largest1)
            heapq.heappush(a, -largest2)
        else:
            # Only one element left greater than k, push it back and exit
            heapq.heappush(a, -largest1)
            break

    # Sum up the remaining elements, converting them back to positive
    print(-sum(a))
