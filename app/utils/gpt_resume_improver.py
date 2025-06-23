import json

from openai import OpenAI

from app.config import settings

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENAI_API_KEY,
)


def improve_resume_with_ai(resume_text: str):
    system_prompt = (
        "You are an expert resume writer, career coach, and ATS (Applicant Tracking System) specialist. "
        "Your task is to thoroughly analyze resumes, identify areas for improvement, and rewrite them "
        "to maximize clarity, professionalism, and impact while ensuring ATS compatibility. "
        "Focus on achievements, quantifiable results, and industry-specific best practices."
    )

    user_prompt = f"""
I have the following resume:

\"\"\"
{resume_text}
\"\"\"

Perform a comprehensive analysis and provide:
1. Detailed section-by-section improvements
2. A completely rewritten resume optimized for both human readers and ATS systems

Return ONLY a clean JSON object with this exact structure (no markdown, no additional text, no code block formatting):
{{
    "analysis": [
        {{
            "section": "section_name",
            "current_content": "current content summary",
            "strengths": ["list of strengths"],
            "weaknesses": ["list of weaknesses"],
            "suggestions": ["specific improvement suggestions"],
            "ats_compatibility": {{
                "score": "1-10",
                "issues": ["list of ATS compatibility issues"],
                "keywords_missing": ["list of relevant keywords to include"]
            }}
        }}
    ],
    "improved_resume": {{
        "content": "full rewritten resume text",
        "summary": "brief description of key improvements made",
        "style_used": "e.g., modern, traditional, executive, etc.",
        "optimization_focus": ["list of optimization focuses"]
    }},
    "additional_recommendations": {{
        "target_roles": ["suggested job titles based on content"],
        "industry_adaptations": ["how to tailor for different industries"],
        "formatting_tips": ["visual presentation suggestions"]
    }}
}}

IMPORTANT:
- Do NOT wrap the response in markdown code blocks (no ```json or ```)
- Do NOT escape quotes (use " not \")
- Return pure JSON that can be parsed directly with json.loads()

Guidelines:
- Prioritize achievement-oriented language with quantifiable results
- Ensure consistent formatting and professional tone
- Optimize for relevant keywords without keyword stuffing
- Remove any placeholder text or vague statements
- Suggest powerful action verbs and industry-specific terminology
- Maintain a balance between conciseness and completeness
- Highlight transferable skills where relevant
- Ensure chronological consistency
"""
    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5,
            response_format={"type": "json_object"},
            extra_headers={
                "X-Title": "ResumeAnalyzerApp"
            }
        )
        raw_response = completion.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {str(e)}")
        raise

    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        if raw_response.startswith("```json"):
            cleaned = raw_response[7:-3]  # Remove ```json and trailing ```
        elif raw_response.startswith("```"):
            cleaned = raw_response[3:-3]  # Remove ``` and trailing ```
        else:
            cleaned = raw_response

        cleaned = cleaned.replace('\\"', '"')
        return json.loads(cleaned)
