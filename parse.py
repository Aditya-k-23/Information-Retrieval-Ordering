with open("./Queries/Emaar.txt", "r") as file:
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
        if line.startswith("->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Results"):
          # Full-text results 1
          # Neural results 2
          resultIdx += 1

          # Initialize 10 empty strings for each response
          for i in range (0, 10):
            document[queryIdx][resultIdx].append("")
          responseIdx = 0

        # End of result
        if line.startswith("------------------------------------------"):
          responseIdx += 1

        else:
          # Add response to document dictionary
          document[queryIdx][resultIdx][responseIdx] += line


