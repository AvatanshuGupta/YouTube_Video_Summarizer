# YouTube Video Summarizer & Analyzer

This is an AI-powered web application built with **Streamlit** that takes a YouTube video link, fetches its transcript, and generates a detailed, structured summary using **Google Gemini (Generative AI)**. The app also displays the video’s thumbnail for a better user experience.

---


## Features

**Paste YouTube Link**  
- Enter any public YouTube video URL that has captions/subtitles.

**Transcript Extraction**  
- Automatically extracts and processes the video transcript using the `youtube-transcript-api`.

**Gemini AI Summarizer**  
- Sends the transcript to **Google Gemini 1.5 Flash** to generate a comprehensive, multi-section summary, including:
  - Title
  - Speaker/Channel Info
  - 400–600 word main summary
  - Key insights in bullet points
  - Referenced materials
  - Additional commentary or real-world context

**Thumbnail Display**  
- Shows the YouTube video thumbnail using the video ID.

**Interactive UI with Streamlit**  
- Simple, clean interface using `streamlit`
- Summary is rendered with full Markdown (headers, bold, lists, and code blocks)

---

## Tech Stack

| Technology         | Description                                           |
|--------------------|-------------------------------------------------------|
| Python             | Core language used for backend logic and APIs        |
| Streamlit          | Web framework used to build interactive UI           |
| Google Gemini      | LLM used for intelligent summarization               |
| python-dotenv      | Securely loads API keys from `.env` files            |
| youtube-transcript-api | Fetches video transcripts from YouTube         |
| Requests (optional)| For any future API integrations                      |

---

## Installation and Setup

1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/YouTube_Video_Summarizer.git
   cd YouTube_Video_Summarizer
   
2. Installating requirements  
Add the following requirements-
- streamlit
- google-generativeai
- youtube_transcript_api
- python-dotenv
- pathlib

Then run the following command.
 ```bash
     pip install -r requirements.txt


