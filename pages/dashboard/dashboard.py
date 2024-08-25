import streamlit as st
import data

# Set wide layout as the first Streamlit command
st.set_page_config(layout="wide")

# Fetch the data
apps = data.get_data()

# Title
st.title('Elements')

# Sidebar for filters
st.sidebar.header('Filters')
selected_tags = st.sidebar.multiselect(
    'Filter by Tags',
    options=list(set(tag for app in apps for tag in app['tags'])),
    default=[]
)

# Filter apps based on selected tags
if selected_tags:
    filtered_apps = [app for app in apps if any(tag in app['tags'] for tag in selected_tags)]
else:
    filtered_apps = apps

# Show the number of results
st.write(f"Results: {len(filtered_apps)} elements")

# Custom CSS for styling with a border around each item
st.markdown(
    """
    <style>
    .item-box {
        background-color: white;
        padding: 16px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid black;
        box-sizing: border-box;
        margin-bottom: 20px;
    }
    .tags-box {
        background-color: #eee;
        color: #333;
        padding: 3px 7px;
        border-radius: 5px;
        margin-right: 5px;
        font-size: 0.8em;
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a grid layout
cols = st.columns(5)  # Adjust the number of columns as needed

selected_apps = []
detailed_app = None
recent_checked_apps = []

# Display filtered data with checkboxes
for index, app in enumerate(filtered_apps):
    col = cols[index % 5]
    with col:
        # Create two columns for name and checkbox
        name_col, checkbox_col = st.columns([4, 1])
        with name_col:
            st.markdown(f"**{app['name']}**", unsafe_allow_html=True)
        with checkbox_col:
            checkbox = st.checkbox("Select", key=f"checkbox_{app['name']}_{index}", label_visibility="hidden")
            if checkbox:
                selected_apps.append(app)
                recent_checked_apps.insert(0, app)  # Add to the front for most recent

        # "View Details" button
        if st.button("View Details", key=f"info_button_{app['name']}_{index}"):
            detailed_app = app

        # Display tags
        tags_html = "".join([f'<span class="tags-box">{tag}</span>' for tag in app['tags']])
        st.markdown(tags_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # End of item-box

# If no detailed app is selected, show the first app in the filtered list
if detailed_app is None and filtered_apps:
    detailed_app = filtered_apps[0]

# Show the number of selected apps
st.write(f"Selected: {len(selected_apps)} apps")

# Split the layout for detailed view and checked items
col1, col2 = st.columns([2, 1])  # Adjusted column ratio to better use the screen width

# Detailed view section
with col1:
    if detailed_app:
        st.write("### Detailed View")
        st.write(f"**Name:** {detailed_app['name']}")
        st.write(f"**Element:** {detailed_app['element']}")
        st.write(f"**XPath:** [Link]({detailed_app['xpath']})")
        st.write(f"**Type:** {detailed_app['type']}")
        st.write(f"**Screen Type:** {detailed_app['typescreen']}")
        st.write(f"**Related:** {', '.join(detailed_app['related'])}")

        # Display tags
        tags_html = "".join([f'<span class="tags-box">{tag}</span>' for tag in detailed_app['tags']])
        st.markdown(tags_html, unsafe_allow_html=True)

        # Display image if available
        if 'image' in detailed_app and detailed_app['image']:
            st.image(detailed_app['image'], caption=f"Image of {detailed_app['name']}", use_column_width=True)
        else:
            st.write("No image available.")

        st.markdown('</div>', unsafe_allow_html=True)  # End the bordered box

# Recently checked items section
with col2:
    st.write("### Recently Checked Items")
    if recent_checked_apps:
        for app in recent_checked_apps:
            st.markdown('<div class="item-box">', unsafe_allow_html=True)  # Begin the bordered box
            st.write(f"**{app['name']}**")
            tags_html = "".join([f'<span class="tags-box">{tag}</span>' for tag in app['tags']])
            st.markdown(tags_html, unsafe_allow_html=True)
            st.markdown("---")  # Divider between items
            st.markdown('</div>', unsafe_allow_html=True)  # End the bordered box
    else:
        st.write("No items checked yet.")
