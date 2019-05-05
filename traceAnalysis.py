totalDroppedPackets = 0.0

totalSentPackets = 0.0

totalReceivedPackets = 0.0

totalDequeuedPackets = 0.0



fname = input("Enter the name of the trace file: ")

Column = 0
Data = []




with open(fname, 'r') as f:
    for line in f:
        check = line.split(" "):
        Data.append(line[Column])
        totalDroppedPackets += Data[-1].count('d')
        totalSentPackets += Data[-1].count('+')
        totalReceivedPackets += Data[-1].count('r')
        totalDequeuedPackets += Data[-1].count('-')





print("Number of total dropped packets: " + totalDroppedPackets + "\n\n")
print("Number of total sent packets: " + totalSentPackets + "\n\n")
print("Number of total received packets: " + totalReceivedPackets + "\n\n")
print("Number of total queued packets: " + totalDroppedPackets + "\n\n")
print("Number of total enqueued packets: " + totalDroppedPackets + "\n\n")
