import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

class GettingResponse():
    def get_response(self,script):
        prompt="""You are an expert summarizer and researcher. Your task is to analyze a YouTube video transcript and
        produce a **comprehensive, insightful summary** that extracts and organizes as much useful information as possible.
        Please:
        1. Extract and expand on **all key ideas, arguments, examples, statistics, and quotes** from the transcript.
        2. Identify the purpose of the video, and the intended audience.
        3. Include any **referenced sources**, books, articles, names, dates, events, or organizations.
        4. If the speaker discusses **current topics**, trends, or technologies, highlight and explain them.
        5. Break down any **step-by-step guides, frameworks, or processes** mentioned.
        6. Rephrase and elaborate to ensure **clarity and completeness**, especially for technical or nuanced ideas.
        7. Structure your response professionally with appropriate headers, lists, and concise sections.
        8. Keep the tone informative, as if writing an article or briefing report.
        9. Optionally include **relevant, real-world insights** to enhance understanding, especially if the transcript lacks detail.
        ### Output format:
        **1. Title (if applicable)**  
        **2. Speaker / Channel Overview**  
        **3. Main Summary**  
        → A 400–600 word breakdown of the video's main points, fully expanded.

        **4. Key Insights**  
        → A bulleted list of the most important or surprising takeaways.

        **5. Referenced Materials**  
        → List any books, links, people, or resources mentioned.

        **6. Additional Commentary or Current Information (if relevant)**  
        → Provide relevant real-world context or recent developments to enrich understanding.

        the script is as folllows : 
        """
        response = model.generate_content(prompt+" "+script)
        return response
    