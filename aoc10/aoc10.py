def solve2(l):
     # add the starting (0) joltage. l has the sorted input data
    adaptors = [0] + l
    # Add a final joltage equal to the max of the current list + 3
    adaptors.append(adaptors[-1] + 3)
    # Create a dictionary to store the number of possible routes "to each joltage".
    routes = {}
    # Initialise with 1 route to the starting joltage.
    routes[0] = 1
    # Begin iterating through adaptors (ignoring the first value because we already set it above).
    for j in adaptors[1:]:
        # Each joltage route is equal to the sum of the number of routes to the previous three joltages.
        # However, some of the joltages won't be present in the list of adaptors.
        # So the number of routes to them will be 0.
        routes[j] = routes.get(j-1, 0) + routes.get(j-2, 0) + routes.get(j-3, 0)

    # Print the number of possible routes to get to the final adaptor.
    print routes[max(routes.keys())]


with open("input.txt") as f:
    l=sorted(map(int, map(str.strip, f.readlines())))
    print l
    solve2(l)
    diff1 = 0
    diff2 = 0
    diff3 = 0
    if l[0]==1:
        diff1 += 1
    if l[0]==2:
        diff2 += 1
    if l[0]==3:
        diff3 += 1
    for i in range(1, len(l)):
        if l[i]-l[i-1]==1:
            diff1+=1
        if l[i]-l[i-1]==2:
            diff2+=1
        if l[i]-l[i-1]==3:
            diff3+=1
    print diff1*(diff3+1)

