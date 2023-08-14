# with open("./Queries/Emaar.txt", "r") as file:
# with open("./Queries/GTAA.txt", "r") as file:
with open("./Queries/Oxford.txt", "r") as file:
    document = {}
    queryIdx = 0
    for line in file:
        # Start of Query
        if line.startswith("Query is: "):
            # Read query
            curQuery = line[10:]
            print(curQuery)
            queryIdx += 1

            # Add query to document dictionary
            document[queryIdx] = {}

            # Initialize query for full-text and neural results
            document[queryIdx][1] = []
            document[queryIdx][2] = []
            resultIdx = 0

        # Start of Result
        elif line.startswith("->>>>>>>>>>>>>>>>>>>>"):
            # Full-text results 1
            # Neural results 2
            resultIdx += 1
            # Initialize 10 empty strings for each response
            for i in range(0, 50):
                document[queryIdx][resultIdx].append("")
            responseIdx = 0

        # End of result
        elif line.startswith("-" * 80):
            responseIdx += 1

        else:
            # Add response to document dictionary
            print(responseIdx)
            document[queryIdx][resultIdx][responseIdx] += line


for i in range(1, 4):
    for j in range(1, 3):
        for k in range(0, 50):
            print(document[i][j][k] + "\n")
