import requests
from flask import Flask,request,render_template

app = Flask(__name__)

def security_headers(url):
    response = requests.get(url)
    headers = response.headers

    security_headers_list = ["Strict-Transport-Security","Content-Security-Policy","X-Content-Type-Options","X-Frame-Options","X-XSS-Protection"]

    print(f"Security headers for {url}")

    results = []
    for header in security_headers_list:
        if header in headers:
            result = f"{header}: {headers[header]}"
        else:
            result = f"{header}: Not Found"
        results.append(result)

    return results


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_security', methods=['GET','POST'])
def check_security():
    if request.method == 'POST':
        urls = request.form.get('urls')
        urls_list = [url.strip() for url in urls.split(',')]
        results = []
        for url in urls_list:
            result = security_headers(url)
            results.append({'url': url, 'results': result})


    #target_url = request.args.get('url')
    #output_file = "results.txt"

    #results = security_headers(target_url,output_file)
        return render_template('results.html',results=results)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


