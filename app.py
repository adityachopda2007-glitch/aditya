from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form fields into a structured dict
        data = {}
        data['name'] = request.form.get('name', '').strip()
        data['title'] = request.form.get('title', '').strip()
        data['email'] = request.form.get('email', '').strip()
        data['phone'] = request.form.get('phone', '').strip()
        data['location'] = request.form.get('location', '').strip()
        data['summary'] = request.form.get('summary', '').strip()

        # Education: we'll accept multiple lines separated by \n
        raw_edu = request.form.get('education', '').strip()
        data['education'] = [line.strip() for line in raw_edu.split('\n') if line.strip()]

        # Experience: multiple entries separated by blank line. Each entry can be multiple lines.
        raw_exp = request.form.get('experience', '').strip()
        # Split by two newlines into entries, or single newline if user used single-line entries
        if '\n\n' in raw_exp:
            entries = [e.strip() for e in raw_exp.split('\n\n') if e.strip()]
        else:
            entries = [line.strip() for line in raw_exp.split('\n') if line.strip()]
        data['experience'] = entries

        # Skills: comma separated
        raw_skills = request.form.get('skills', '').strip()
        data['skills'] = [s.strip() for s in raw_skills.split(',') if s.strip()]

        # Projects: similar to experience
        raw_projects = request.form.get('projects', '').strip()
        data['projects'] = [p.strip() for p in raw_projects.split('\n') if p.strip()]

        return render_template('resume.html', data=data)

    # GET -> show form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)