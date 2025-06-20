import openai

from app.config import settings

openai.api_key = settings.OPENAI_API_KEY


def improve_resume_with_chatgpt(resume_text: str):
    system_prompt = (
        "You are a professional resume editor. "
        "Your task is to improve resumes and return structured suggestions."
    )

    user_prompt = f"""
This is a resume:
\"\"\"
{resume_text}
\"\"\"

Please do the following:
1. Suggest improvements for each section (summary, experience, skills, etc.)
2. Point out any missing or weak sections
3. Return an improved version of the resume
4. Format the result as JSON with fields:
  - 'suggestions': list of section-wise suggestions
  - 'improved_resume': improved version of the resume (plain text)
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    # Extract the result
    content = response['choices'][0]['message']['content']

    # (Optional) You can use `json.loads()` if GPT returns valid JSON
    return content
