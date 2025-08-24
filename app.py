import streamlit as st
from agent_utils import get_search_results

st.set_page_config(page_title="🔎 GenAI Search Agent", page_icon="🤖")

st.title("AI-Powered Search Agent 🔎🤖")

query = st.text_input("Enter your query:", placeholder="e.g. What are the latest trends in Generative AI?")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching..."):
            response = get_search_results(query)
        st.success("Here's what I found:")
        st.write(response)
    else:
        st.warning("Please enter a query before searching.")

# Footer / Signature
st.markdown(
    """
    <hr>
    <div style='text-align: center; font-size: 16px; color: gray;'>
        ✨ Built with ❤️ in Streamlit <br>
        <b>By Sharanya</b>
    </div>
    """,
    unsafe_allow_html=True
)
