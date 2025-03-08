# audio-to-text

So, I was brainstorming for inspiration for one of my daily videos as part of my 100 Days of AI challenge. 
I needed a transcription from a video to get things rolling. But, of course, I hit a wall. 
I tried several websites, but all of them wanted me to either create an account (seriously, for a one-time task?) or pay for some premium subscription. 
Like, come on, I'm just an AI newbie who posted my first Python "Hello World" last week, and these sites want me to fork out cash just to transcribe some audio? Nah.

So, instead of giving in to the paywall or logging into some random site, I decided to take matters into my own hands. 
I used some open-source libraries, coded it up myself, and got the transcription done locally on my laptop.
Sure, it's not a massive achievement, but for me, this is huge. 
Right after my "Hello World" moment, I hit a roadblock, figured it out, and solved it by writing some code. It's not just about the solution; it's about learning and applying those lessons.

And you know what? I'm throwing this on my GitHub because why not? Sharing this journey is part of the fun.

Cheers to the hustle! 🥂


# How to run it

To use Whisper, OpenAI's powerful audio-to-text transcription model, on your laptop, follow these steps. Whisper works well for transcribing speech to text and is available as an open-source library.

Here's a quick guide on how to get started:

1. Install Dependencies
First, you'll need to install Whisper and the necessary libraries. Make sure you have Python installed on your system (preferably Python 3.7+).

Open your terminal (Command Prompt, PowerShell, or terminal on Mac/Linux) and run:
pip install openai-whisper
Additionally, you’ll need ffmpeg to process audio files like MP3s, WAVs, etc.

For Windows: Download the ffmpeg zip from ffmpeg.org and follow installation instructions.
For Mac: You can install it via Homebrew by running:
brew install ffmpeg
For Linux: You can install it with:
sudo apt update
sudo apt install ffmpeg
2. Use Whisper to Transcribe Audio
Once you've installed Whisper and ffmpeg, you can use it to transcribe audio to text.

Example Python Script:

Create a Python file (e.g., transcribe.py) and paste the following code:
