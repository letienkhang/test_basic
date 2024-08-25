import streamlit as st
from filters import filter_apps_by_tags
from display_web import display_web

st.set_page_config(layout="wide")
import data_web as data


apps = data.get_data_web()

st.title('YODY - WEBSITE')

selected_tags = filter_apps_by_tags(apps)

if selected_tags:
    filtered_apps = [app for app in apps if any(tag in app['tags'] for tag in selected_tags)]
else:
    filtered_apps = apps

st.write(f"Results: {len(filtered_apps)} events")

selected_apps = display_web(filtered_apps)

