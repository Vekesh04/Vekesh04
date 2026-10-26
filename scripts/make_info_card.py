from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[1]
rows = [('Name','Vekesh Makani'),('Role','AI Engineer / Python Developer'),('Build','Useful software across domains'),('AI','GenAI · RAG · ML · Voice'),('Stack','Python · Java · React · FastAPI'),('Data','SQLite · Firebase · MySQL'),('Study','B.Tech AI & Data Science'),('Projects','SunoSeva / JARVIS / Insurance AI'),('Also','Food Inventory / Banking / ML'),('Status','Open to opportunities')]
out=['<svg xmlns="http://www.w3.org/2000/svg" width="490" height="440" viewBox="0 0 490 440" role="img"><title>Vekesh Makani — developer information</title><rect width="490" height="440" rx="16" fill="#0d1117"/><text x="26" y="35" fill="#39d353" font-size="16" font-family="monospace">vekesh@github</text><path d="M26 51H464" stroke="#30363d"/>']
for i,(k,v) in enumerate(rows):
    out.append(f'<g font-family="monospace" font-size="12"><animate attributeName="opacity" values="0;1" dur=".4s" begin="{i*.13}s" fill="freeze"/><text x="26" y="{85+i*30}" fill="#7ee787">{k}</text><text x="103" y="{85+i*30}" fill="#c9d1d9">{escape(v)}</text></g>')
out.append('<text x="26" y="409" fill="#8b949e" font-family="monospace" font-size="11">$ turning ideas into applications _</text></svg>')
(ROOT/'info-card.svg').write_text(''.join(out))
