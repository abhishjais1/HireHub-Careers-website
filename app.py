from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'Loaction':"bengaluru, India",
    'Salary': 'Rs 10,00,000'
  },
    {
    'id':2,
    'title':'Data Scientist',
    'Loaction':"Delhi, India",
    'Salary': 'Rs 15,00,000'
  },
    {
    'id':3,
    'title':'Fronted engineer',
    'Loaction':"Remote",
    'Salary': 'Rs 12,00,000'
  },
    {
    'id':4,
    'title':'Backend Engineer',
    'Loaction':"bsan Francisco, USA",
    'Salary': '$120,000'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                          company_name='HireHub')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)