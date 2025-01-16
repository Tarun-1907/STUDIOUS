# import streamlit as st 
# from phi.agent import Agent
# from phi.model.google import Agent
# from phi.tools.duckduckgo import Agent
# import google.generativeai as genai
# from google.generativeai import upload_file, get_file
 
# import time
# from pathlib import Path
# import tempfile
# from dotenv import load_dotnev
# load_dotnev()
# import os

# API_KEY=os.getenv("GOOGLE_API_KEY")
# if API_KEY:
#     genai.configure(api_key=API_KEY)
    
# # Page configuration
# st.set_page_config(
#     page_title="STUDIOUS",
#     page_icon="",
#     layout="wide"
# )

# st.title("STUDIOUS")
# st.header("Powered by Gemini")


# @st.cache_resource
# def initialize_agent():
#     return Agent(
#         name="STUDIOUS",
#         model=Gemini(id="gemini-2.0-flash-exp"),
#         tools=[DuckDuckGo()],
#         markdown=True,
#     )
    
# ## Initialize the agent
# multimodal_agent=initialize_agent()

# # File uploader
# video_file=st.file_uploader(
#     "Upload a Video file",type=['mp4','mov','avi'], help="Upload a video for AI analysis"
# )

# if video_file:
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
#         temp_video.write(video_file.read())
#         video_path=temp_video.name
    
    
#     st.video(video_path, format="video/mp4", start_time=0)
    
#     user_quiey=st.text_area(
#             "what insights are you seeking?",
#     placeholder="Ask anything",
#     help= "provide specific questions or")
    
#     if st.button("analyze",key="analyze"):
#         if not user_query:
#             st.warning("please enter question")
#         else:
#             try:
#                 with st.spinner("processing video and gathering insights")
                
#                     processed_video=upload_file(video_path)
#                     while processed_video.state.name=="PROCESSING":
#                         time.sleep(1)
#                         processed_video=get_file(processed_video.name)
                        
#                     analyze_prompt=(
#                         f"""
#                         {user_query}
#                         """
#                     )
                    
#                     response=multimodal_Agent.run(analysis_prompt,videos=[processed_video])
                    
#                 st.subheader("result")
#                 st.markdown(response.content)
                
#             except Exception as error:
#                 st.error(f"{error}")
#             finally:
#                 Path(video_path).unlink(missing_ok=True)
# else:
#     st.info("Upload Video to start")
    
# st.markdown(
#     """
#     <style>
#     .stTextArea textarea{
#         height:100px;
#     }
#     <style>
#     """,
#     unsafe_allow_html=True
# )

# import streamlit as st 
# from phi.agent import Agent
# from phi.model.google import Gemini
# from phi.tools.duckduckgo import DuckDuckGo
# import google.generativeai as genai
# from google.generativeai import upload_file, get_file
 
# import time
# from pathlib import Path
# import tempfile
# from dotenv import load_dotenv

# load_dotenv()
# import os

# API_KEY = os.getenv("GOOGLE_API_KEY")
# if API_KEY:
#     genai.configure(api_key=API_KEY)
    
# # Page configuration
# st.set_page_config(
#     page_title="STUDIOUS",
#     page_icon="📚",
#     layout="wide"
# )

# st.title("STUDIOUS - Ask me Anything from a video")
# # st.header("Powered by Gemini")

# @st.cache_resource
# def initialize_agent():
#     return Agent(
#         name="STUDIOUS",
#         model=Gemini(id="gemini-2.0-flash-exp"),
#         tools=[DuckDuckGo()],
#         markdown=True,
#     )
    
# # Initialize the agent
# multimodal_agent = initialize_agent()

# # File uploader
# video_file = st.file_uploader(
#     "Upload a Video file", type=['mp4', 'mov', 'avi'], help="Upload a video for analysis"
# )

# if video_file:
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
#         temp_video.write(video_file.read())
#         video_path = temp_video.name
    
#     st.video(video_path, format="video/mp4", start_time=0)
    
#     user_query = st.text_area(
#         "What insights are you seeking for ?",
#         placeholder="Ask anything",
#         help="Provide specific questions or insights you're looking for."
#     )
    
#     if st.button("Analyze", key="analyze"):
#         if not user_query:
#             st.warning("Please enter your question.")
#         else:
#             try:
#                 with st.spinner("Processing video and gathering insights..."):
#                     processed_video = upload_file(video_path)
#                     while processed_video.state.name == "PROCESSING":
#                         time.sleep(1)
#                         processed_video = get_file(processed_video.name)
                        
#                     analysis_prompt = f"{user_query}"
#                     response = multimodal_agent.run(analysis_prompt, videos=[processed_video])
                    
#                 st.subheader("Result")
#                 st.markdown(response.content)
                
#             except Exception as error:
#                 st.error(f"Error: {error}")
#             finally:
#                 Path(video_path).unlink(missing_ok=True)
# else:
#     st.info("Upload a video to get the insights")

# st.markdown(
#     """
#     <style>
#     .stTextArea textarea {
#         height: 100px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )



# import streamlit as st
# from phi.agent import Agent
# from phi.model.google import Gemini
# from phi.tools.duckduckgo import DuckDuckGo
# import google.generativeai as genai
# from google.generativeai import upload_file, get_file
# from transformers import pipeline
# from rake_nltk import Rake
# import time
# from pathlib import Path
# import tempfile
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Configure Google Generative AI API
# API_KEY = os.getenv("GOOGLE_API_KEY")
# if API_KEY:
#     genai.configure(api_key=API_KEY)

# # Initialize summarizer and keyword extractor
# summarizer = pipeline("summarization")
# rake = Rake()

# # Streamlit page configuration
# st.set_page_config(
#     page_title="STUDIOUS",
#     page_icon="📚",
#     layout="wide"
# )

# st.title("STUDIOUS - Ask me Anything from a Video")

# @st.cache_resource
# def initialize_agent():
#     return Agent(
#         name="STUDIOUS",
#         model=Gemini(id="gemini-2.0-flash-exp"),
#         tools=[DuckDuckGo()],
#         markdown=True,
#     )

# # Initialize the agent
# multimodal_agent = initialize_agent()

# # File uploader for video
# video_file = st.file_uploader(
#     "Upload a Video file", type=['mp4', 'mov', 'avi'], help="Upload a video for analysis"
# )

# # Simulated transcription function (replace with actual transcription logic)
# def transcribe_video(video_path):
#     return "This is a simulated transcription of the video content."

# # Function to summarize text
# def summarize_text(text):
#     summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
#     return summary[0]['summary_text']

# # Function to extract keywords
# def extract_keywords(text):
#     rake.extract_keywords_from_text(text)
#     return rake.get_ranked_phrases()

# if video_file:
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
#         temp_video.write(video_file.read())
#         video_path = temp_video.name

#     st.video(video_path, format="video/mp4", start_time=0)

#     user_query = st.text_area(
#         "What insights are you seeking?",
#         placeholder="Ask anything",
#         help="Provide specific questions or insights you're looking for."
#     )

#     if st.button("Analyze", key="analyze"):
#         if not user_query:
#             st.warning("Please enter your question.")
#         else:
#             try:
#                 with st.spinner("Processing video and gathering insights..."):
#                     processed_video = upload_file(video_path)
#                     while processed_video.state.name == "PROCESSING":
#                         time.sleep(1)
#                         processed_video = get_file(processed_video.name)

#                     analysis_prompt = f"{user_query}"
#                     response = multimodal_agent.run(analysis_prompt, videos=[processed_video])

#                 st.subheader("Result")
#                 st.markdown(response.content)

#                 st.subheader("Transcription")
#                 transcription = transcribe_video(video_path)
#                 st.write(transcription)

#                 st.subheader("Summary")
#                 summary = summarize_text(transcription)
#                 st.write(summary)

#                 st.subheader("Keywords")
#                 keywords = extract_keywords(transcription)
#                 st.write(", ".join(keywords))

#             except Exception as error:
#                 st.error(f"Error: {error}")
#             finally:
#                 Path(video_path).unlink(missing_ok=True)
# else:
#     st.info("Upload a video to get the insights")

# st.markdown(
#     """
#     <style>
#     .stTextArea textarea {
#         height: 100px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import google.generativeai as genai
from google.generativeai import upload_file, get_file
import yt_dlp as youtube_dl
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google API
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Streamlit page configuration
st.set_page_config(
    page_title="STUDIOUS",
    page_icon="📚",
    layout="wide"
)

st.title("STUDIOUS - Ask me Anything from a video")

# Initialize RAKE for keyword extraction and agent for multimodal AI
@st.cache_resource
def initialize_agent():
    return Agent(
        name="STUDIOUS",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

# Initialize the agent
multimodal_agent = initialize_agent()

# Function to fetch video from URL (YouTube)
def fetch_video_from_url(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': tempfile.mktemp(suffix='.mp4'),  # Output path for video
        'noplaylist': True,  # Avoid downloading entire playlists
        'quiet': False,  # Turn off quiet mode to get more info
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info_dict)
            return video_path
    except youtube_dl.DownloadError as e:
        st.error(f"Error fetching video: {str(e)}")
        return None

# Layout with increased left and right margins
st.markdown("<style> .main {padding-left: 15%; padding-right: 15%;} </style>", unsafe_allow_html=True)
with st.container():
    # File uploader for local video file
    video_file = st.file_uploader(
        "Upload a Video file", type=['mp4', 'mov', 'avi'], help="Upload a video for analysis"
    )

    # Input for YouTube URL
    youtube_url = st.text_input("Or enter a YouTube video URL", help="Paste the YouTube video URL here.")

    # Process video if uploaded or URL is provided
    if video_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
            temp_video.write(video_file.read())
            video_path = temp_video.name

        st.video(video_path, format="video/mp4", start_time=0)

    elif youtube_url:
        video_path = fetch_video_from_url(youtube_url)
        if video_path:
            st.video(video_path, format="video/mp4", start_time=0)

    # User query input
    user_query = st.text_area(
        "What insights are you seeking for?",
        placeholder="Ask anything",
        help="Provide specific questions or insights you're looking for."
    )

    # Button to trigger analysis
    if st.button("Analyze", key="analyze"):
        if not user_query:
            st.warning("Please enter your question.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Upload video to the cloud
                    processed_video = upload_file(video_path)
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

                    # Get response from multimodal agent
                    analysis_prompt = f"{user_query}"
                    response = multimodal_agent.run(analysis_prompt, videos=[processed_video])

                st.subheader("Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"Error: {error}")

            finally:
                Path(video_path).unlink(missing_ok=True)

    else:
        st.info("Upload a video or provide a YouTube URL to get insights")

# Custom styling for textarea
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
