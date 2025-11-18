import streamlit as st
from src.extract_transcript import get_transcript
from src.summarize import summarize_long_text

st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon="🎥",
    layout="wide"
)

st.markdown("""
<style>
    .st-emotion-cache-1jicfl2 { 
        border: 2px solid #555;
        border-radius: 10px;
        padding: 20px;
    }
    .stButton>button {
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


st.title("🎥 YouTube Video Summarizer")
st.caption("Get concise AI-powered summaries from any video with a transcript.")

with st.container(border=True):
    url = st.text_input(
        "Enter YouTube URL:", 
        placeholder="https://www.youtube.com/watch?v=..."
    )
    
    summarize_button = st.button(
        "Generate Summary", 
        type="primary", 
        use_container_width=True
    )

st.divider()

if summarize_button:
    if not url:
        st.error("Please enter a valid YouTube URL to start.")
    else:
        try:
            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("Your Video:")
                st.video(url)

            with col2:
                st.subheader("Your Results:")
                
                with st.spinner("Extracting transcript..."):
                    text = get_transcript(url)
                
                if not text:
                    st.error("Could not extract transcript. The video may not have captions.")
                    st.stop()
                
                with st.spinner("🧠 Summarizing... This may take a moment."):
                    summary = summarize_long_text(text)

                tab_summary, tab_transcript = st.tabs(["Summary", "Full Transcript"])

                with tab_summary:
                    st.success("Here's the summary:")
                    st.markdown(summary) 

                with tab_transcript:
                    st.info("Full transcript:")
                    st.text_area("Transcript", text, height=350)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")