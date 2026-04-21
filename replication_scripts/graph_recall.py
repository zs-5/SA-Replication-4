import csv
import matplotlib.pyplot as plt


# Use your data for recall (from thresholds 0.5 to 0.9)
# recall_learned_embedding = [0.8953, 0.8897, 0.8842, 0.8791, 0.8721, 0.865 , 0.8564, 0.8457, 0.8297] # Data from our 2nd last run
# recall_random_embedding = []
recall_learned_embedding = []
ts = [] # Threshold values. For example: [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]

with open("outputs/threshold_recalls.csv", "r") as csvfile:
	data = csv.reader(csvfile)
	next(data) # Skip headings
	for t, recall in data:
		recall_learned_embedding.append(float(recall))
		ts.append(float(t))

plt.plot(ts, recall_learned_embedding, color="purple", marker="+")
# plt.plot(ts, recall_random_embedding, color="lightgreen", marker="x")

plt.xlim(0.4, 1)
plt.ylim(0, 1)

plt.title("Swapped Arguments")
plt.ylabel("Recall")
plt.xlabel("Threshold for reporting warnings")

plt.savefig("outputs/recall_graph.png")
plt.show()