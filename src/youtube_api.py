from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

class api:
    def fetch_transcript(self,link):
        video_id=link.split("v=")[1].split("&")[0]
        fetched_data=ytt_api.fetch(video_id)
        paragraph=[]
        for lines in fetched_data:
            paragraph.append(lines.text)
        corpus=" ".join(paragraph)
        return corpus
    
    
    def fetch_thumbnail(self,link):
        video_id=link.split("v=")[1].split("&")[0]
        image=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return image