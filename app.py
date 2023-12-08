from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Mumbai,Maharashtra',
    'salary': 'Rs. 5,00,000'
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Pune,Maharashtra',
    'salary': 'Rs. 8,00,000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 6,00,000'
  },
  {
    'id': 4,
    'title': 'Fullstack Developer',
    'location': 'Bangalore,Karnataka',
    'salary': 'Rs. 8,00,000'
  },
  {
    'id': 5,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 6,
    'title': 'Frontend Developer',
    'location': 'Bangalore,Karnataka',
    'salary': 'Rs. 8,00,000'
  },
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)  

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080 ,debug=True)