import streamlit as st

def filter_apps_by_tags(apps):
    st.sidebar.header('Filters')
    selected_tags = st.sidebar.multiselect(
        'Filter by Tags',
        options=list(set(tag for app in apps for tag in app['tags'])),
        default=[]
    )
    return selected_tags
