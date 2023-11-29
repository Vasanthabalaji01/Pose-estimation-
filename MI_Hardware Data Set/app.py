import pandas as pd
import matplotlib.pyplot as plt

# Load sleep data
sleep_data = pd.read_csv('Sleep.csv')

# Load steps data
steps_data = pd.read_csv('Steps.csv')

# Calculate total sleep time
sleep_data['total_sleep'] = sleep_data['deepSleepTime'] + sleep_data['shallowSleepTime'] + sleep_data['wakeTime']

# Calculate total steps metrics
steps_data['total_metrics'] = steps_data['distance'] + steps_data['runDistance'] + steps_data['calories']

# Pie chart for sleep data
labels_sleep = ['Deep Sleep', 'Shallow Sleep', 'Wake Time']
sizes_sleep = sleep_data[['deepSleepTime', 'shallowSleepTime', 'wakeTime']].sum()
colors_sleep = ['lightblue', 'lightcoral', 'lightgreen']

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(sizes_sleep, labels=labels_sleep, colors=colors_sleep, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Sleep Time')

# Pie chart for steps data
labels_steps = ['Distance', 'Run Distance', 'Calories']
sizes_steps = steps_data[['distance', 'runDistance', 'calories']].sum()
colors_steps = ['gold', 'lightcoral', 'lightgreen']

plt.subplot(1, 2, 2)
plt.pie(sizes_steps, labels=labels_steps, colors=colors_steps, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Steps Metrics')

plt.tight_layout()  # Adjust layout for better spacing
plt.show()
