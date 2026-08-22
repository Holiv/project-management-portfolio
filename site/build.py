#!/usr/bin/env python3
"""Gera docs/index.html a partir dos .md do portfolio. Uso: python3 site/build.py"""
import re, html, pathlib, datetime
ROOT = pathlib.Path(__file__).parent.parent
OUT = ROOT / "docs"

CRIACOES = [
    ("ecossistema-de-acompanhamento-de-obras", "ecossistema", "Ecossistema de acompanhamento de obras", "Plataforma web de project controls · em produção"),
    ("comparador-de-cronogramas", "comparador", "Comparador de cronogramas", "Motor VBA Excel ↔ MS Project · em uso semanal"),
    ("analise-critica-de-cronogramas", "analise", "Análise crítica de cronogramas", "Auditoria executável dentro do MS Project · em uso"),
    ("gestao-de-equipe", "equipe", "Gestão de equipe e competências", "Sistema com série longitudinal de dados · em uso pela equipe"),
]
ANCORAS = {d: f"#{a}" for d, a, _, _ in CRIACOES}
ANCORAS.update({"linha-do-tempo.md": "#linha-do-tempo", "capacidades.md": "#capacidades"})

def resolve(dest):
    if dest.startswith("http"): return dest
    for k, v in ANCORAS.items():
        if k in dest: return v
    return None

def inline(s):
    s = html.escape(s)
    def _lnk(m):
        txt, dest = m.group(1), html.unescape(m.group(2))
        alvo = resolve(dest)
        if alvo and alvo.startswith("http"):
            return f'<a href="{html.escape(alvo)}" target="_blank" rel="noopener">{txt}</a>'
        return f'<a href="{alvo}">{txt}</a>' if alvo else txt
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _lnk, s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    return s

def md(body):
    out, i, lines = [], 0, body.split("\n")
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells): rows.append(cells)
                i += 1
            if rows:
                head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
                body_r = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
                out.append(f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{body_r}</tbody></table></div>')
            continue
        if m := re.match(r"^(#{2,4})\s+(.*)$", ln):
            lvl = len(m.group(1)) + 1
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if ln.startswith("#"): i += 1; continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"): buf.append(lines[i].lstrip("> ").rstrip()); i += 1
            out.append("<blockquote>" + inline(" ".join(x for x in buf if x)) + "</blockquote>"); continue
        if re.match(r"^\s*[-*]\s+", ln):
            items = []
            while i < len(lines):
                if re.match(r"^\s*[-*]\s+", lines[i]):
                    items.append(re.sub(r"^\s*[-*]\s+", "", lines[i])); i += 1
                elif items and lines[i].startswith((" ", "\t")) and lines[i].strip():
                    items[-1] += " " + lines[i].strip(); i += 1
                else: break
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        if ln.strip() == "---": i += 1; continue
        if ln.strip().startswith("→"):
            i += 1; continue  # os "ver arquitetura" viram <details> na página
        if ln.strip():
            buf = [lines[i]]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|\s*[-*]\s)", lines[i]) and lines[i].strip() != "---":
                buf.append(lines[i]); i += 1
            out.append("<p>" + inline(" ".join(buf)) + "</p>"); continue
        i += 1
    return "\n".join(out)

def corpo(p):
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"^#\s+.*\n", "", t, count=1)
    return md(t)

sec_criacoes = []
for pasta, anc, titulo, sub in CRIACOES:
    d = ROOT / "criacoes" / pasta
    narrativa = corpo(d / "README.md")
    arq = d / "arquitetura.md"
    det = ""
    if arq.exists():
        det = (f'<details class="arq"><summary>Arquitetura e decisões técnicas</summary>'
               f'<div class="arq-body">{corpo(arq)}</div></details>')
    sec_criacoes.append(f'''<section id="{anc}" class="criacao">
<header><h2>{html.escape(titulo)}</h2><p class="sub">{html.escape(sub)}</p></header>
{narrativa}{det}</section>''')

linha = corpo(ROOT / "linha-do-tempo.md")
caps = corpo(ROOT / "capacidades.md")
hoje = datetime.date.today().strftime("%d/%m/%Y")

page = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Helton Oliveira — Portfólio de Gerenciamento de Projetos</title>
<meta name="description" content="Engenheiro civil e analista de planejamento sênior que constrói as ferramentas que o planejamento usa — quatro sistemas em uso real, documentados do problema ao resultado.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono&display=swap" rel="stylesheet">
<style>
:root{{--paper:#FAF9F6;--card:#FFFFFF;--ink:#20242A;--mute:#5F6672;--rule:#E4E2DC;--accent:#275D8C;--accent-ink:#1C4468;--accent-soft:#E6EEF5;--band:#20242A;--band-ink:#F4F3EF}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--paper);color:var(--ink);font:400 16.5px/1.65 "IBM Plex Sans",system-ui,sans-serif}}
.wrap{{max-width:46rem;margin:0 auto;padding:0 20px}}
.band{{background:var(--band);color:var(--band-ink);padding:52px 0 44px}}
.band .kicker{{font:600 12px/1 "IBM Plex Sans";letter-spacing:.14em;text-transform:uppercase;color:#9DB8D2;margin:0 0 14px}}
.band h1{{font:600 clamp(30px,6vw,44px)/1.08 "Fraunces",Georgia,serif;margin:0 0 10px;letter-spacing:-.01em;text-wrap:balance}}
.band .lede{{font-size:18px;max-width:38rem;margin:0 0 20px;color:#D8D6D0}}
.band .links a{{color:#fff;font-weight:600;text-decoration:none;border-bottom:1.5px solid #4E7096;margin-right:18px;font-size:14.5px}}
nav.toc{{position:sticky;top:0;background:var(--paper);border-bottom:1px solid var(--rule);z-index:5}}
nav.toc .wrap{{display:flex;gap:4px;overflow-x:auto;padding:0 20px}}
nav.toc a{{font:600 12.5px/1 "IBM Plex Sans";letter-spacing:.04em;color:var(--mute);text-decoration:none;padding:13px 10px;white-space:nowrap;border-bottom:2px solid transparent}}
nav.toc a:hover{{color:var(--accent-ink);border-color:var(--accent)}}
.numeros{{padding:34px 0 6px}}
.numeros h2, section>header h2, .bloco>h2{{font:600 24px/1.2 "Fraunces",Georgia,serif;margin:0 0 4px}}
.numeros .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:16px}}
.numeros .n{{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--accent);border-radius:8px;padding:13px 15px}}
.numeros .n strong{{display:block;font:600 21px/1.25 "Fraunces",Georgia,serif;color:var(--accent-ink)}}
.numeros .n span{{font-size:13.5px;color:var(--mute)}}
.numeros .ress{{font-size:13px;color:var(--mute);margin-top:12px}}
section.criacao{{padding:34px 0 8px;border-top:1px solid var(--rule);margin-top:28px}}
section.criacao .sub{{color:var(--accent-ink);font-weight:600;font-size:13.5px;letter-spacing:.02em;margin:2px 0 0}}
h3{{font:600 13px/1.4 "IBM Plex Sans";letter-spacing:.1em;text-transform:uppercase;color:var(--accent-ink);margin:24px 0 8px}}
h4{{font-size:16.5px;margin:18px 0 6px}}
p{{margin:0 0 12px}}
ul{{margin:0 0 12px;padding-left:1.3em}}li{{margin:0 0 6px}}
a{{color:var(--accent-ink)}}
blockquote{{margin:0 0 14px;padding:12px 16px;background:var(--accent-soft);border-radius:8px;font-size:15.5px}}
code{{font:400 .88em "IBM Plex Mono",monospace;background:#EFEDE8;padding:1px 5px;border-radius:4px}}
.tw{{overflow-x:auto;margin:0 0 14px}}
table{{border-collapse:collapse;width:100%;font-size:14.5px}}
th,td{{text-align:left;padding:8px 12px 8px 0;border-bottom:1px solid var(--rule);vertical-align:top}}
th{{font-weight:600;font-size:11.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--mute)}}
details.arq{{margin:18px 0 6px;border:1px solid var(--rule);border-radius:9px;background:var(--card)}}
details.arq>summary{{cursor:pointer;padding:13px 16px;font-weight:600;font-size:14.5px;color:var(--accent-ink);list-style:none}}
details.arq>summary::-webkit-details-marker{{display:none}}
details.arq>summary::before{{content:"▸ ";color:var(--mute)}}
details.arq[open]>summary::before{{content:"▾ "}}
.arq-body{{padding:2px 16px 14px;border-top:1px solid var(--rule)}}
.bloco{{padding:34px 0 8px;border-top:1px solid var(--rule);margin-top:28px}}
footer{{margin-top:44px;background:var(--band);color:#B9B7B1;padding:30px 0 40px;font-size:13.5px}}
footer a{{color:#fff}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style></head><body>
<div class="band"><div class="wrap">
<p class="kicker">Portfólio · Gerenciamento de Projetos &amp; Project Controls</p>
<h1>Helton da Silva de Oliveira</h1>
<p class="lede">Engenheiro civil (CREA-RJ) e analista de planejamento sênior que <strong>constrói as ferramentas que o planejamento usa</strong> — quatro sistemas em uso real num programa de concessão rodoviária, documentados do problema ao resultado.</p>
<p class="links"><a href="https://www.linkedin.com/in/helton-so/" target="_blank" rel="noopener">LinkedIn</a><a href="https://github.com/Holiv" target="_blank" rel="noopener">GitHub</a><a href="https://github.com/Holiv/project-management-portfolio" target="_blank" rel="noopener">Este portfólio no GitHub</a></p>
</div></div>
<nav class="toc"><div class="wrap">
<a href="#numeros">Em números</a><a href="#ecossistema">Ecossistema</a><a href="#comparador">Comparador</a><a href="#analise">Análise crítica</a><a href="#equipe">Equipe</a><a href="#linha-do-tempo">Linha do tempo</a><a href="#capacidades">Capacidades</a>
</div></nav>
<main class="wrap">
<section id="numeros" class="numeros"><h2>Em números</h2>
<div class="grid">
<div class="n"><strong>4 sistemas</strong><span>concebidos e implementados, todos em uso real</span></div>
<div class="n"><strong>329 commits · 2 meses</strong><span>maior sistema: ~11 domínios funcionais, 48 migrations</span></div>
<div class="n"><strong>6.483 atividades</strong><span>maior cronograma processado — rateio no tempo reproduzindo o MS Project ao centavo</span></div>
<div class="n"><strong>2 cliques</strong><span>para qualquer gestor acessar avanço e desvio, de onde estiver</span></div>
<div class="n"><strong>510 → 5.251 atividades</strong><span>auditadas com os mesmos critérios — método provado à mão, depois codificado, relatório em um comando</span></div>
<div class="n"><strong>25 usuários reais</strong><span>em dois setores, ~6 semanas de operação — medido no banco em 22/08/2026</span></div>
<div class="n"><strong>~193 mil registros</strong><span>de avanço físico no acervo, incluindo a carga do histórico legado</span></div>
<div class="n"><strong>0 → 1, sozinho</strong><span>concepção, arquitetura, implementação e operação por uma pessoa</span></div>
</div>
<p class="ress">Números de operação medidos em 22/08/2026 por consulta ao banco de produção, com dados de teste excluídos. Comparativos de tempo (antes × depois) entrarão como estimativa rotulada, com o método — nunca como medição que não houve.</p>
</section>
{"".join(sec_criacoes)}
<section id="linha-do-tempo" class="bloco"><h2>Linha do tempo</h2>{linha}</section>
<section id="capacidades" class="bloco"><h2>Capacidades</h2>{caps}</section>
</main>
<footer><div class="wrap">
<p><strong style="color:#fff">Nota de integridade.</strong> Este portfólio referencia sistemas em produção corporativa. Os repositórios privados são citados como existentes e de minha autoria — verificável pelo histórico de commits — sem exposição de código proprietário. Nenhum dado contratual, financeiro ou pessoal de terceiros aparece aqui.</p>
<p>Versão em português · versão bilíngue em preparação · atualizado {hoje} · <a href="https://github.com/Holiv/project-management-portfolio">fonte</a></p>
</div></footer>
</body></html>"""
OUT.mkdir(exist_ok=True)
(OUT / "index.html").write_text(page, encoding="utf-8")
(OUT / ".nojekyll").write_text("", encoding="utf-8")
print(f"docs/index.html gerado — {len(page)//1024} KB")
