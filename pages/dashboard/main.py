import streamlit as st
from filters import filter_apps_by_tags
from display import display_apps, display_detailed_view, display_recent_checked

st.set_page_config(layout="wide")

import data

apps = data.get_data()

st.title('Elements')

selected_tags = filter_apps_by_tags(apps)

if selected_tags:
    filtered_apps = [app for app in apps if any(tag in app['tags'] for tag in selected_tags)]
else:
    filtered_apps = apps

st.write(f"Results: {len(filtered_apps)} elements")

selected_apps, detailed_app, recent_checked_apps = display_apps(filtered_apps)

col1, col2 = st.columns([2, 1])

display_recent_checked(col2, recent_checked_apps)
