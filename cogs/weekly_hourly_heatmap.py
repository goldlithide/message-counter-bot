import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
df = pd.read_json('message_log_new_est.json')
daily_hourly_counts = df.groupby(['date_sent', 'day_of_week', 'hour']).size().reset_index(name='msg_count')
avg_messages = daily_hourly_counts.groupby(['day_of_week', 'hour'])['msg_count'].mean().reset_index()
pivot_data = avg_messages.pivot(index="hour", columns="day_of_week", values="msg_count")
pivot_data = pivot_data.reindex(index=range(0, 24), columns=range(0, 7), fill_value=0)
days_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
pivot_data.columns = [days_mapping[col] for col in pivot_data.columns]
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_data, cmap="Purples", annot=True, fmt=".1f", linewidths=.5)
plt.title("Average Hourly Message Counts")
plt.xlabel("Day")
plt.ylabel("Hour")
plt.yticks(rotation=0)
plt.tight_layout()
image_buffer = io.BytesIO()
plt.savefig(image_buffer, format='png', bbox_inches='tight')
image_buffer.seek(0)
plt.show()
