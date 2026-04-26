import pandas as pd
import matplotlib.pyplot as plt
from dune_client.client import DuneClient

# ==========================================
# 1. API SETUP & DATA EXTRACTION
# ==========================================
DUNE_API_KEY = "iEuaSNBZeMLZcwoqQdAqWa1uVUgyQ8d3"
QUERY_ID = 7375748 

print("Fetching OP Airdrop data from Dune API...")
dune = DuneClient(DUNE_API_KEY)
query_result = dune.get_latest_result(QUERY_ID)

# Convert to Pandas DataFrame
df = pd.DataFrame(query_result.result.rows)
print(f"Data loaded successfully! Total wallets analyzed: {len(df)}")

# ==========================================
# 2. DATA AGGREGATION
# ==========================================
print("Aggregating behavioral profiles...")

# Count the number of wallets in each psychological category
profile_counts = df['behavior_profile'].value_counts()

# ==========================================
# 3. DATA VISUALIZATION (DONUT CHART)
# ==========================================
print("Generating Donut Chart...")

plt.figure(figsize=(9, 9))

# Define strategic colors for psychological profiling
# Green/Blue for loyal users, Orange/Red for opportunistic dumpers
color_map = {
    'Diamond Hands 💎': '#2ecc71',   # Emerald Green
    'Strong Holder 🛡️': '#3498db',   # Ocean Blue
    'Partial Seller ⚖️': '#f39c12',  # Orange
    'Full Dumper 🏃‍♂️': '#e74c3c'     # Crimson Red
}

# Map colors strictly to the data index order to prevent color mismatch
colors = [color_map.get(label, '#95a5a6') for label in profile_counts.index]

# Create the base Pie Chart
plt.pie(profile_counts.values, 
        labels=profile_counts.index, 
        colors=colors, 
        autopct='%1.1f%%',       # Show percentages with 1 decimal
        startangle=140,          # Rotate slightly for better aesthetics
        pctdistance=0.82,        # Position the percentage text
        textprops={'fontsize': 11, 'fontweight': 'bold'},
        wedgeprops={'edgecolor': 'white', 'linewidth': 2}) # White borders

# The Magic Trick: Draw a white circle in the middle to create the "Donut" effect
centre_circle = plt.Circle((0,0), 0.65, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a perfect circle
plt.axis('equal')  

# Add a professional title
plt.title('OP Airdrop: User Retention & Behavioral Profiling', fontsize=16, fontweight='bold', pad=20)

# Save the chart as a PNG file for GitHub
plt.savefig('op_airdrop_retention.png', bbox_inches='tight')

# Render the final chart
plt.show()
