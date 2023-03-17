import csv

with open('Friday Ladder - Raw.csv', newline='') as csvfile:
    results = {}
    for row in csv.DictReader(csvfile):
        pairA = row['Pair A']
        pairB = row['Pair B']
        score = 4 - int(row['Position'])
        if pairA not in results: results[pairA] = []
        results[pairA].append(score)
        if pairB not in results: results[pairB] = []
        results[pairB].append(score)

totals = {}
for name, scores in results.items():
    points = sorted(scores,reverse=True)[:6]
    totals[name] = sum(points)

scores = sorted(totals.items(), key=lambda item: item[1], reverse=True)
with open('Friday Ladder - Analysed.csv', newline='', mode='w') as csvfile:
    fieldnames = ["Name", "Points", "Individual"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for name, score in scores:
        individual = sorted(results[name],reverse=True)    
        print (name, score, individual)
        writer.writerow({'Name': name, 'Points': score, 'Individual': individual})
    
    
