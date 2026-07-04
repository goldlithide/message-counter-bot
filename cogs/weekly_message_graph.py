import json
import matplotlib.pyplot as plt
import pandas as pd

with open(filename, "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)
user_id = input("Enter a user ID: ")

df = df[df["user_id"].astype(str) == user_id]
df["date_sent"] = pd.to_datetime(df["date_sent"])

df["week_start"] = df["date_sent"].dt.to_period("W-MON").dt.start_time

weekly_counts = df["week_start"].value_counts().sort_index()

weekly_counts.index = weekly_counts.index.strftime("%Y-%m-%d")

plt.figure(figsize=(12, 6))
weekly_counts.plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Messages Sent by Week", fontsize=14)
plt.xlabel("Week Start Date", fontsize=12)
plt.ylabel("Number of Messages", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("messages_per_week.png")
plt.show()
