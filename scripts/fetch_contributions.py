"""Fetch GitHub's public calendar without credentials; never fabricate activity."""
import json, re, urllib.request
from html.parser import HTMLParser
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
class Calendar(HTMLParser):
    def __init__(self):
        super().__init__(); self.cells = {}; self.tips = {}; self.target = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('data-date') and 'data-level' in a:
            self.cells[a['id']] = {'date': a['data-date'], 'level': int(a['data-level'])}
        if tag == 'tool-tip': self.target = a.get('for'); self.tips[self.target] = ''
    def handle_data(self, text):
        if self.target: self.tips[self.target] += text
    def handle_endtag(self, tag):
        if tag == 'tool-tip': self.target = None

def parse(html):
    p = Calendar(); p.feed(html); days = []
    for key, day in p.cells.items():
        tip = p.tips.get(key, '').strip()
        m = re.search(r'([\d,]+) contributions?', tip)
        if m: day['count'] = int(m[1].replace(',', ''))
        elif re.search(r'No contributions', tip, re.I): day['count'] = 0
        else: raise ValueError('Contribution count missing: ' + day['date'])
        days.append(day)
    days.sort(key=lambda d: d['date'])
    if len(days) < 350: raise ValueError('Incomplete GitHub calendar; preserving previous data')
    return {'username': 'Vekesh04', 'through': days[-1]['date'], 'total': sum(d['count'] for d in days), 'days': days}

if __name__ == '__main__':
    req = urllib.request.Request('https://github.com/users/Vekesh04/contributions', headers={'User-Agent':'Vekesh04-profile-art'})
    with urllib.request.urlopen(req, timeout=45) as response: data = parse(response.read().decode())
    (ROOT / 'data').mkdir(exist_ok=True)
    (ROOT / 'data/contributions.json').write_text(json.dumps(data, indent=2) + '\n')
