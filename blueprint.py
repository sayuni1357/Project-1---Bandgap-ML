from mp_api.client import MPRester
print("MPRester imported successfully!")

from mp_api.client import MPRester
import pandas as pd
import os

api_key = os.getenv("MAPI_KEY")
mpr = MPRester(api_key)

def fetch_range(min_gap, max_gap, max_count=500):
    docs = mpr.materials.summary.search(
        criteria={
            "band_gap": {"$gte": min_gap, "$lte": max_gap},
            "energy_above_hull": {"$lte": 0.1}
        },
        fields=[
            "material_id",
            "formula_pretty",
            "band_gap",
            "energy_above_hull",
            "density",
            "volume",
            "symmetry.spacegroup_number",
        ],
        limit=max_count,
    )

    data = [doc.dict() for doc in docs]
    df = pd.DataFrame(data)
    return df

# Fetch datasets
metals = fetch_range(0.0, 0.1, max_count=500)
semis = fetch_range(0.1, 3.8, max_count=1000)
insul = fetch_range(3.8, 50.0, max_count=500)

# Add labels
metals["label"] = "metal"
semis["label"] = "semiconductor"
insul["label"] = "insulator"

# Combine
df_all = pd.concat([metals, semis, insul], ignore_index=True)
df_all.to_csv("data/all_classes_bandgaps.csv", index=False)

print(df_all["label"].value_counts())

# Import the correct MPRester
from mp_api.client import MPRester

# Replace this with your actual API key (stored securely if possible)
MAPI_KEY = "SS3reUV9Y5n9UtyavCqkimWscPqnDW03"
# Create the client and query
with MPRester(MAPI_KEY) as mpr:
    # Use the new API endpoint: materials.summary.search()
    results = mpr.materials.summary.search(
        # Define filtering criteria
        band_gap=(0.5, 3.0),   # Select semiconductors: 0.5 eV < Eg < 3.0 eV
        fields=["material_id", "formula_pretty", "band_gap", "structure"],
        num_chunks=1,           # Number of data chunks to fetch
        chunk_size=10           # Number of entries per chunk
    )

# Print the first few results
for r in results:
    print(f"{r.formula_pretty:10s}  Band gap: {r.band_gap:.2f} eV")

# Check what kind of object the results variable is
print(type(results))

# Look at the first result more closely
second_result = results[1]
print(second_result)


import pandas as pd

# Extract only key fields into a list of dictionaries
data = []
for r in results:
    data.append({
        "material_id": str(r.material_id),
        "formula": r.formula_pretty,
        "band_gap": r.band_gap
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print(df.head())

df.head()
df.info()

df_reduced = df[['formula_pretty', 'band_gap']]
df_reduced.head()

df.columns

df_reduced = df[['material_id','formula', 'band_gap']]
df_reduced.head()

def categorize_material(band_gap):
    if band_gap < 0.1:
        return "Conductor"
    elif band_gap < 3.8:
        return "Semiconductor"
    else:
        return "Insulator"

df_reduced['category'] = df_reduced['band_gap'].apply(categorize_material)
df_reduced.head()
