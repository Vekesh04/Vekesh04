import json
from datetime import date, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PALETTE = ['#161f2c','#0e4429','#006d32','#26a641','#39d353']
def render(data):
    start = date.fromisoformat(data['days'][0]['date']); start -= timedelta(days=(start.weekday()+1)%7)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="860" height="238" viewBox="0 0 860 238" role="img"><title>Vekesh04 public contribution calendar</title><rect width="860" height="238" rx="16" fill="#0d1117"/><g font-family="monospace" fill="#c9d1d9"><text x="26" y="30" font-size="14">vekesh@github:~ $ ./contributions.sh</text><text x="26" y="216" font-size="12">'+str(data['total'])+' contributions · '+data['days'][0]['date']+' to '+data['through']+'</text></g>']
    for day in data['days']:
        dt = date.fromisoformat(day['date']); delta = (dt-start).days; col,row=divmod(delta,7)
        x,y=38+col*14.7,64+row*17
        if row==0: out.append(f'<text x="{x}" y="52" fill="#8b949e" font-size="10" font-family="monospace">{dt.strftime("%b") if dt.day<=7 else ""}</text>')
        out.append(f'<rect x="{x}" y="{y}" width="11.5" height="13" rx="2.5" fill="{PALETTE[min(day["level"],4)]}"><title>{day["date"]}: {day["count"]} contributions</title><animate attributeName="opacity" values="0;1" dur=".25s" begin="{(col+row)*.025:.3f}s" fill="freeze"/></rect>')
    out.append('<text x="671" y="216" fill="#8b949e" font-size="10" font-family="monospace">Less</text>')
    for i,c in enumerate(PALETTE): out.append(f'<rect x="{704+i*15}" y="206" width="11" height="11" rx="2" fill="{c}"/>')
    out.append('<text x="785" y="216" fill="#8b949e" font-size="10" font-family="monospace">More</text></svg>')
    return ''.join(out)
if __name__ == '__main__': (ROOT/'contrib-heatmap.svg').write_text(render(json.loads((ROOT/'data/contributions.json').read_text())))
