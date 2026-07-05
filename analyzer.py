import ollama
from promts import PROMPT
    

def analyze_resume(resume_text):

    prompt = PROMPT.format(resume=resume_text)

    response = ollama.chat(
        model='deepseek-r1:1.5b', messages=[
            {'role': 'user', 'content': prompt}
        ])
    
    return response['message']['content']