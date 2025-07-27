import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/generate_resume_ai', methods=['POST'])
def generate_resume_ai():
    data = request.form
    prompt = f"""
    Generate a professional resume based on the following details:
    Name: {data['name']}
    Email: {data['email']}, Phone: {data['phone']}
    Skills: {data['skills']}
    Experience: {data['experience']}
    Career Goals: {data['goals']}
    Target Job Role: {data['job_role']}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )
    result = response.choices[0].message['content']
    return jsonify({'result': result})

@app.route('/generate_cover_letter_ai', methods=['POST'])
def generate_cover_letter_ai():
    data = request.form
    prompt = f"""
    Write a tailored, professional cover letter for the job role '{data['job_role']}'.
    Name: {data['name']}
    Email: {data['email']}, Phone: {data['phone']}
    Skills: {data['skills']}
    Experience Summary: {data['experience']}
    Career Goals: {data['goals']}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )
    result = response.choices[0].message['content']
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
