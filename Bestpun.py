import streamlit as st
import requests
import time

# Function to fetch a random pun
st.set_page_config(page_title="Fpuns", page_icon=":laughing:")
def fetch_pun():
    url = "https://punapi.rest/api/pun"
    response = requests.get(url)
    if response.status_code == 200:
        pun_data = response.json()
        return pun_data['pun']
    else:
        return "Error: Unable to fetch pun"

# Main function
def main():
    st.title("THE WORLD OF LAUGTHER 😄😆🤣 ")
    st.subheader(" How do trees access the internet? They log on 😄.!")
    
    # Button to fetch and display a new pun
    if st.button("Get Pun 🤣🤣🤣"):
        # Display a progress bar while fetching the pun
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)  # Simulate a delay while fetching the pun
            progress_bar.progress(percent_complete + 1)
        
        pun = fetch_pun()
        # Display the pun in a card-like layout
        st.write("# Here's a pun for you ")
        st.markdown("""<div style='border: 2px solid #ccc;
                     border-radius: 5px; 
                    padding: 10px; 
                    background-color: "black"; 
                    font-size: 20px;
                    text-align: center;
                    text-decoration: uppercase;'>
                        <p style='font-size: 15px; font-weight: bold;'>{}</p>
                      </div>""".format(pun), unsafe_allow_html=True)
        
        # Adding a like button
        if st.button("❤️ Like"):
            # Placeholder for adding like functionality
            st.write("Pun Liked! ❤️")
        
        # Adding a share button
        if st.button("📤 Share"):
            # Placeholder for adding share functionality
            st.write("Pun Shared! 📤")

if __name__ == "__main__":
    main()
