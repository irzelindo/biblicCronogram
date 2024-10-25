# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Data from Adam's descendants to Noah
data = {
    "Name": [
        "Adam",
        "Seth",
        "Enosh",
        "Kenan",
        "Mahalalel",
        "Jared",
        "Enoch",
        "Methuselah",
        "Lamech",
        "Noah",
    ],
    "Age at fatherhood (years)": [130, 105, 90, 70, 65, 162, 65, 187, 182, 500],
    "Total years of life": [930, 912, 905, 910, 895, 962, 365, 969, 777, 950],
    "Son's Name": [
        "Seth",
        "Enosh",
        "Kenan",
        "Mahalalel",
        "Jared",
        "Enoch",
        "Methuselah",
        "Lamech",
        "Noah",
        "Shem, Ham, and Japheth",
    ],
}

# Define a list of darker colors for each descendant
colors = [
    "darkblue",
    "darkgreen",
    "darkred",
    "darkorange",
    "darkcyan",
    "darkmagenta",
    "darkslateblue",
    "brown",
    "saddlebrown",
    "indigo",
]

# Create DataFrame
descendants_df = pd.DataFrame(data)

# Calculate the cumulative sum of ages of ancestors when they had their sons
start_ages = [0]  # Adam starts at zero

for i in range(1, len(descendants_df)):
    start_ages.append(
        start_ages[i - 1] + descendants_df["Age at fatherhood (years)"][i - 1]
    )

# Create the Hat Graph
plt.figure(figsize=(10, 6))

# Add a medium green background from 0 to the age when Adam died
plt.axvspan(
    0,
    descendants_df["Total years of life"][0],
    color="mediumseagreen",
    alpha=0.3,
    label="Adam's lifespan period",
)

# Add a medium red background starting from the year of the Flood (1656) onward
plt.axvspan(
    1656,
    max(start_ages) + max(descendants_df["Total years of life"]),
    color="orange",
    alpha=0.3,
    label="Post-Flood Period",
)

# Plot the "bars" of the Hat Graph for each descendant
for i in range(len(descendants_df)):

    final_age = start_ages[i] + descendants_df["Total years of life"][i]

    initial_age = start_ages[i]

    plt.hlines(
        y=i,
        xmin=start_ages[i],
        xmax=final_age,
        color=colors[i % len(colors)],  # Cycle through the colors if needed
        linewidth=15,
        label=descendants_df["Name"][i],
    )
    # Add dashed line at the end of each "bar"
    plt.axvline(
        x=final_age,
        color="red",
        linestyle="--",
        linewidth=0.5,
        visible=True,
    )
    # Show the value where the dashed line intersects the x-axis
    plt.text(
        final_age,
        i,
        "Died: " + str(final_age),
        va="bottom",
        ha="left",
        color="darkred",
        fontsize=8,
    )

    # Add dashed line at the start of each "bar"
    plt.axvline(
        x=initial_age,
        color="darkgreen",
        linestyle="--",
        linewidth=0.5,
        visible=True,
    )

    plt.text(
        initial_age,
        i,
        "Born: " + str(initial_age),
        va="bottom",
        ha="right",
        color="darkgreen",
        fontsize=8,
    )

    # Add the total years of life in the middle of the "bar"
    plt.text(
        final_age / 2 + initial_age / 2,
        i,
        str(descendants_df["Total years of life"][i]) + " years",
        va="center_baseline",
        ha="center",
        color="white",
        fontsize=10,
        fontweight="bold",
    )

# Adjust axes
plt.yticks(range(len(descendants_df)), descendants_df["Name"])
plt.xlabel("Years of Life")
plt.title("Descendants from Adam to Noah")
plt.legend()

# Display the graph
plt.tight_layout()
plt.show()
