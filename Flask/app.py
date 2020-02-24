from flask import Flask, render_template, request
from Category import  SVM_Predict

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        get_data = request.form['news']
        category=SVM_Predict(get_data)

        data= {
            'category':category[0],
            
        }

        return render_template('index.html', data=data)
    else:
        return render_template('index.html',data=[])


if __name__ == "__main__":
    app.run(debug=True)
