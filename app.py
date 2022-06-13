from flask import Flask, render_template, request, send_file
from Service import createReportFromInput, getAllReportsFromInput, downloadReportFromInput

app = Flask(__name__)


@app.route('/create', methods=['POST', 'GET'])
def create_report():
    if request.method == 'POST':
        createReportFromInput(request.form)
        return "Successfully create the report."
    return render_template('create.html')


@app.route('/get', methods=['POST', 'GET'])
def get_all_reports():
    if request.method == 'POST':
        res = getAllReportsFromInput(request.form)
        return res
    return render_template('get.html')


@app.route('/download', methods=['POST', 'GET'])
def download_report():
    if request.method == 'POST':
        res = downloadReportFromInput(request.form)
        return send_file(res, as_attachment=True)

    return render_template('download.html')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    print("yes")
    app.run(debug=True)
