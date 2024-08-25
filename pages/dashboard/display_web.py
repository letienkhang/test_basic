import subprocess
import streamlit as st

# Define the environments dictionary
environments = {
    'Dev': 'https://dev.yody.io/',
    'UAT': 'https://uat.yody.io/',
    'Prod': 'https://beta.yody.vn/',
    'Dev - Unicorn': 'https://unicorn-dev.yody.io/',
    'UAT - Unicorn': 'https://unicorn-uat.yody.io/'
}

# Initialize the session state variable to track the running status
if 'is_running' not in st.session_state:
    st.session_state['is_running'] = False

def run_script(path, environment_url):
    # Disable buttons while running
    st.session_state.is_running = True
    try:
        result = subprocess.run(["python3", path, environment_url], capture_output=True, text=True)
        if result.stderr:
            st.toast(f"Error running script {path}: {result.stderr}", icon="❌")
        else:
            st.toast(f"Script {path} ran successfully in {environment_url}", icon="✅")
    except Exception as e:
        st.toast(f"Failed to run the script: {e}", icon="❌")
    finally:
        # Re-enable buttons after running
        st.session_state.is_running = False

def display_web(filtered_apps):
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

                # Create a row with two columns: one for the button and one for the dropdown
                button_col, dropdown_col = st.columns([1, 2])

                with dropdown_col:
                    option = st.selectbox("Chọn môi trường", list(environments.keys()),
                                          key=f"dropdown_{app['name']}_{index}", label_visibility="collapsed")
                    environment_url = environments[option]  # Map the selected option to the corresponding URL

                with button_col:
                    # Disable button if a script is running
                    button_disabled = st.session_state.get('is_running', False)
                    if st.button("Run", key=f"info_button_{app['name']}_{index}", disabled=button_disabled):
                        # Disable all buttons by setting is_running to True
                        st.session_state.is_running = True
                        detailed_app = app
                        run_script(app['path'], environment_url)  # Run the script with the selected environment URL

                # Add to recent checked apps (if desired)
                recent_checked_apps.insert(0, app)

    if detailed_app is None and filtered_apps:
        detailed_app = filtered_apps[0]

    return selected_apps, detailed_app, recent_checked_apps
