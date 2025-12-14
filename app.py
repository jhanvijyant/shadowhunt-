from flask import Flask, render_template, request
from urllib.parse import urlparse
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
def normalize_url(url: str) -> str:
    """Ensure URL has a scheme so requests() doesn't silently fail."""
    if not url.startswith(('http://', 'https://')):
        return 'https://' + url
    return url
def url_analysis(url: str) -> int:
    score = 0
    if not url:
        return 2

    if len(url) > 75:
        score += 1
    if '@' in url:
        score += 1
    netloc = urlparse(url).netloc
    if '-' in netloc:
        score += 1
    if re.match(r"http://\d+\.\d+\.\d+\.\d+", url):
        score += 1
    if not url.startswith('https'):
        score += 1

    return score
def content_analysis(url: str) -> int:
    score = 0
    try:
        r = requests.get(url, timeout=4)
        soup = BeautifulSoup(r.text, 'html.parser')

        if soup.find('input', {'type': 'password'}):
            score += 1

        keywords = ['verify', 'login', 'update', 'secure', 'confirm', 'urgent']
        text = soup.get_text().lower()
        for k in keywords:
            if k in text:
                score += 1

    except Exception:
        score += 2

    return score
def final_decision(u: int, c: int):
    total = u + c
    if total >= 6:
        return 'Phishing Website', total
    elif total >= 3:
        return 'Suspicious Website', total
    else:
        return 'Safe Website', total
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    score = 0
    scanned_url = ''

    if request.method == 'POST':
        scanned_url = request.form.get('url', '').strip()
        scanned_url = normalize_url(scanned_url)

        u_score = url_analysis(scanned_url)
        c_score = content_analysis(scanned_url)
        result, score = final_decision(u_score, c_score)

    return render_template(
        'index.html',
        result=result,
        score=score,
        scanned_url=scanned_url
    )
def _run_basic_tests():
    assert normalize_url('google.com').startswith('https://')
    assert url_analysis('https://google.com') >= 0
    assert final_decision(0, 0)[0] == 'Safe Website'
    assert final_decision(3, 0)[0] == 'Suspicious Website'
    assert final_decision(4, 3)[0] == 'Phishing Website'
    print('All basic tests passed.')

if __name__ == '__main__':
    _run_basic_tests()
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
