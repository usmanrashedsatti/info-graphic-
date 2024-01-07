# github link
#https://github.com/usmanrashedsatti/info-graphic-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def prepare_data():
    # Assuming your data is stored in a list or DataFrame
    #data read from file location
    
    company_locations = pd.read_csv("data.csv")
    return pd.DataFrame({'company_location': company_locations})

def plot_pie_chart(data):
    # Count the occurrences of each location
    location_counts = data['company_location'].value_counts()

    # Set seaborn style
    sns.set(style="whitegrid")

    # Define a custom color palette
    colors = sns.color_palette("tab10")

    # Create explode data for the pie chart
    explode = tuple(0.1 if i == 0 else 0 for i in range(len(location_counts)))

    # Plotting the pie chart with advanced features
    plt.figure(figsize=(12, 8))
    plt.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode,
            wedgeprops=dict(width=0.6
                            , edgecolor='w'), shadow=True)

    # Add legend
    plt.legend(title='Locations', loc='upper right', bbox_to_anchor=(1, 0, 0.5, 1))

    # Add a title and adjust fontsize
    plt.title('Distribution of Company Locations', fontsize=18)

    # Show the plot
    plt.savefig('22075747.png', bbox_inches='tight')

def main():
    data = prepare_data()
    plot_pie_chart(data)

if __name__ == "__main__":
    main()


#plot 2
data_4 =  pd.read_csv("data-1.csv")
years = [2020, 2021, 2022, 2023]

# Set seaborn style
sns.set(style="whitegrid")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the data with different line styles and markers
for employment_type, values in data_4.items():
    ax.plot(years, values, label=employment_type, marker='o', linestyle='--')

# Adding labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_title('Employment Type Count Over the Years', fontsize=16)

# Adding grid lines
ax.grid(True, linestyle='--', alpha=0.7)

# Adding legend
ax.legend()

#Show plot
plt.savefig('22075747.png', bbox_inches='tight')




#3rd plot



#  data reading
data_2 = pd.read_csv("data_3.csv")

# Extracting labels and values from the data dictionary
labels = list(data_2.keys())
values = list(data_2.values())

# Create a more advanced bar plot using seaborn
plt.figure(figsize=(12, 8))
colors = sns.color_palette('Spectral', len(data_2))
sns.barplot(x=values, y=labels, palette=colors, edgecolor='w', ci=None)
plt.xlabel('Sum of Remote Ratio', fontsize=14)
plt.ylabel('Job Titles', fontsize=14)
plt.title('Sum of Remote Ratio for Different Job Titles', fontsize=16, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.2)
plt.savefig('22075747.png', bbox_inches='tight')





#plot 4
# Your data location
data_4 =  pd.read_csv("data_4.csv")

# Extracting labels and values from the data dictionary
labels = list(data_4.keys())
values = list(data_4.values())

# Create a more advanced bar plot using seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x=values, y=labels, palette='viridis', edgecolor='w', ci=None)
plt.xlabel('Average Salary in USD', fontsize=14)
plt.ylabel('Job Titles', fontsize=14)
plt.title('Average Salary for Different Job Titles', fontsize=16, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Adding data values on top of the bars
for i, v in enumerate(values):
    plt.text(v + 1000, i, f'${v:,.0f}', va='center', fontsize=12)
plt.savefig('22075747.png', bbox_inches='tight')



