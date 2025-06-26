from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
script=ytt_api.fetch("uV4L-wcnK3Y")
paragraph=[]
for lines in script:
    paragraph.append(lines.text)

corpus=" ".join(paragraph)
print(corpus)