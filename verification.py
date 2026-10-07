import csv

# join the tables
with open ("transactions.csv", mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
with open ("accounts.csv", mode='r', encoding='utf-8') as file2:
    reader2 = csv.reader(file2)
    
approved = 0
rejected = 0
flagged = 0

for row in reader:
    if ({row['fromAccount'] id status = "FROZEN")
        print (id, "rejected. Frozen account"), skip
        rejected += 1
    elif (f.fromAccount(id).status = "CLOSED")
        print (id, "rejected. Closed account"), skip
        rejected += 1
    elif (f.(amount) > f.fromAccount(limit))
        print (id, "rejected. Limit exceeded"), skip
        rejected += 1
    elif (f.(amount) > f.fromAccount(balance))
        print (id, "rejected. Insufficent funds"), skip
        rejected += 1
    elif (f.(amount) > 10000)
        print (id, "approved, flagged for verification"), skip
        flagged += 1
    else
        print (id, "Approved")
        approved += 1
        row['toAccount'].['balance'] += amount
        row['fromAccount'].['balance'] -= amount
        
print("Approved: " + approved, "/nRejected: " + rejected, "/nApproved but flagged: " + flagged)
    
