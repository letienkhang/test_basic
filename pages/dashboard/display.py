import streamlit as st


def display_apps(filtered_apps):
    selected_apps = []
    detailed_app = None
    recent_checked_apps = []

    cols = st.columns(5)

    for index, app in enumerate(filtered_apps):
        col = cols[index % 5]
        with col:
            container = st.container(border=True)
            with container:
                st.code(f'''
                # Tên element
                {app['name']}

                # Tags
                {", ".join(app['tags'])}
                            ''', language='python')
                checkbox_col, button_col = st.columns(2)
                with checkbox_col:
                    checkbox = st.checkbox("Select", key=f"checkbox_{app['name']}_{index}")
                with button_col:
                    if st.button("View Details", key=f"info_button_{app['name']}_{index}"):
                        detailed_app = app

                if checkbox:
                    selected_apps.append(app)
                    recent_checked_apps.insert(0, app)

    if detailed_app is None and filtered_apps:
        detailed_app = filtered_apps[0]

    return selected_apps, detailed_app, recent_checked_apps


def display_detailed_view(col1, detailed_app):
    with col1:
        if detailed_app:
            st.write("### Detailed View")
            st.write(f"**Name:** {detailed_app['name']}")
            st.write(f"**Element:** {detailed_app['element']}")
            st.write(f"**XPath:** [Link]({detailed_app['xpath']})")
            st.write(f"**Type:** {detailed_app['type']}")
            st.write(f"**Screen Type:** {detailed_app['typescreen']}")
            st.write(f"**Related:** {', '.join(detailed_app['related'])}")

            tags_html = "".join([f'<span class="tags-box">{tag}</span>' for tag in detailed_app['tags']])
            st.markdown(tags_html, unsafe_allow_html=True)

            if 'image' in detailed_app and detailed_app['image']:
                st.image(detailed_app['image'], caption=f"Image of {detailed_app['name']}", use_column_width=True)
            else:
                st.write("No image available.")

            st.markdown('</div>', unsafe_allow_html=True)


def display_recent_checked(col2, recent_checked_apps):
    with col2:
        st.write("### Recently Checked Items")
        if recent_checked_apps:
            for app in recent_checked_apps:
                st.markdown('<div class="item-box">', unsafe_allow_html=True)
                st.write(f"**{app['name']}**")
                tags_html = "".join([f'<span class="tags-box">{tag}</span>' for tag in app['tags']])
                st.markdown(tags_html, unsafe_allow_html=True)
                st.markdown("---")
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.write("No items checked yet.")
