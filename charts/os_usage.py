import seaborn as sns
import matplotlib.pyplot as plt

os_stat = {
    'Android': 43.72,
    'Windows': 27.43,
    'iOS': 17.82,
    'OS X': 5.86,
    'Linux': 1.54,
    'Others': 3.63
}

os_name = list(os_stat.keys())
os_usage = [os_stat[k] for k in os_name]
ax = sns.barplot(x=os_name, y=os_usage, hue=os_name)
ax.set(title='OS Usage as per StatCounter Global Stats (Feb 2024)', xlabel='OS Name', ylabel='Usage (%)')
for i in ax.containers:
    ax.bar_label(i,)
plt.show()
