import streamlit as st
import pandas as pd

st.title("Recommendation System")

st.write("This page uses association rules from the Apriori algorithm to recommend products.")

# Load precomputed association rules and cluster assignments
rules = pd.read_csv("data/rules.csv")  # columns: antecedents, consequents, confidence, lift, support, etc.
clusters = pd.read_csv("data/clusters.csv")  # columns: item, Cluster


def parse_itemset(item_str):
    """ Extracts the item from a frozenset string. """
    start = item_str.find("{'") + 2  # position right after {'
    end = item_str.find("'}")
    item = item_str[start:end]
    return {item}  # return a set containing the extracted item


# Apply parsing to the antecedents and consequents
if 'antecedents' in rules.columns and 'consequents' in rules.columns:
    rules['antecedents'] = rules['antecedents'].apply(parse_itemset)
    rules['consequents'] = rules['consequents'].apply(parse_itemset)


# --- Sidebar Filters ---
st.sidebar.header("Recommendation Filters")
min_conf = st.sidebar.slider("Minimum Confidence", 0.0, 1.0, 0.0)
min_lift = st.sidebar.slider("Minimum Lift", 0.0, 10.0, 0.0)

# --- User Input ---
user_input = st.text_input("Enter a product name (e.g., 'electronics.smartphone_samsung'):")

if user_input:
    # Filter rules where the user's item is in the antecedents
    user_filtered_rules = rules[rules['antecedents'].apply(lambda x: user_input in x)]
    user_filtered_rules = user_filtered_rules[
        (user_filtered_rules['confidence'] >= min_conf) &
        (user_filtered_rules['lift'] >= min_lift)
    ]

    st.write("---")
    # Show recommendations from association rules
    if user_filtered_rules.empty:
        st.write(f"No association rules found that match '{user_input}' with the selected filters.")
    else:
        st.markdown("**Recommended Items based on Association Rules:**")
        user_filtered_rules = user_filtered_rules.sort_values(by="confidence", ascending=False)
        top_rules = user_filtered_rules.head(5)
        for _, row in top_rules.iterrows():
            recommended_items = list(row['consequents'])
            st.write(f"- Items: {recommended_items}, Confidence: {row['confidence']:.2f}, Lift: {row['lift']:.2f}")

    # --- Cluster-based Recommendations ---
    if user_input in clusters['item'].values:
        user_cluster = clusters.loc[clusters['item'] == user_input, 'Cluster'].iloc[0]
        st.write("---")
        st.write(f"**{user_input}** belongs to cluster {user_cluster}.")
        similar_items = clusters[clusters['Cluster'] == user_cluster]['item']
        # Show other items from the same cluster (up to 5, excluding the original)
        similar_items_sample = similar_items[similar_items != user_input].sample(
            min(len(similar_items[similar_items != user_input]), 5)
        )
        st.write("Other items in the same cluster:")
        for item in similar_items_sample:
            st.write(f"- {item}")
    else:
        st.write(f"The item '{user_input}' does not appear in the cluster data.")
