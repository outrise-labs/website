"""Builds the site from src.html: English at the root, Portuguese under pt/, plus the privacy pages.
Usage: python3 build.py [supabase_url] [publishable_key]"""
import sys, os, re
URL = sys.argv[1] if len(sys.argv) > 1 else ""
KEY = sys.argv[2] if len(sys.argv) > 2 else ""
ORBIT = open("orbit_path.txt").read().strip()
src = open("src.html").read().replace("__ORBIT__", ORBIT).replace("__WL_URL__", URL).replace("__WL_KEY__", KEY)

EN = [
 # head
 ('<html lang="pt-PT">', '<html lang="en">'),
 ('<meta property="og:image:alt" content="Outrise: construímos soluções de IA em que podes confiar">', '<meta property="og:image:alt" content="Outrise: AI agents that take care of the work for you">'),
 ('<meta property="og:locale:alternate" content="en_GB">', '<meta property="og:locale:alternate" content="pt_PT">'),
 ('<meta name="twitter:title" content="Outrise · Construímos soluções de IA em que podes confiar">', '<meta name="twitter:title" content="Outrise · AI solutions you can trust">'),
 ('<meta name="twitter:image" content="https://www.outrise.technology/media/og.png">', '<meta name="twitter:image" content="https://www.outrise.technology/media/og-en.png">'),
 ('<link rel="canonical" href="https://www.outrise.technology/pt/">', '<link rel="canonical" href="https://www.outrise.technology/">'),
 ('<meta property="og:locale" content="pt_PT">', '<meta property="og:locale" content="en_GB">'),
 ('<meta property="og:url" content="https://www.outrise.technology/pt/">', '<meta property="og:url" content="https://www.outrise.technology/">'),
 ('content="Outrise · Construímos soluções de IA em que podes confiar"', 'content="Outrise · AI solutions you can trust"'),
 ('media/og.png"', 'media/og-en.png"'),
 ('<a class="lang" href="../" hreflang="en" lang="en">EN<span class="sr"> English version</span></a>', '<a class="lang" href="pt/" hreflang="pt" lang="pt">PT<span class="sr"> Versão em português</span></a>'),
 # long sentences first
 ('Construímos soluções de IA', 'We build AI solutions'),
 ('em que podes confiar', 'you can trust'),
 ('Trabalho que queremos tirar das tuas mãos', 'Work we want to take off your hands'),
 ('O que construímos, para quem e com que princípios. Narrado em inglês.', 'What we build, for whom, and the principles behind it.'),
 ('Agentes de IA que tratam do trabalho por ti.', 'AI agents that take care of the work for you.'),
 ('Vê como funciona.', 'See how it works.'),
 ('Ver a apresentação da Outrise', 'Watch the film about Outrise'),
 ('Ver a apresentação', 'Watch the film'),
 ('Há trabalho que ninguém quer fazer.', 'Some work nobody wants to do.'),
 ('Os nossos agentes fazem-no.', 'Our agents do it.'),
 ('Agentes que trabalham sozinhos, com tudo à vista', 'Agents that work on their own, in plain sight'),
 ('Fazer, e não só responder.', 'Doing, not just answering.'),
 ('Um agente nosso acaba a tarefa. Se não consegue, diz onde parou e porquê.', 'Our agents finish the task. If one can’t, it tells you where it stopped and why.'),
 ('Mostrar o trabalho.', 'Showing the work.'),
 ('Tudo o que um agente faz fica registado, para poderes ver, corrigir e confiar.', 'Everything an agent does is logged, so you can check it, correct it and trust it.'),
 ('Cada tarefa passa por ler, fazer e verificar antes de ser entregue.', 'Every task is read, done and checked before it is delivered.'),
 ('Números de exemplo, para mostrar o painel.', 'Example figures, to show the dashboard.'),
 ('3 emails do cliente e a encomenda', '3 customer emails and the order'),
 ('Fatura corrigida e reenviada', 'Invoice corrected and resent'),
 ('O total confere com a encomenda', 'The total matches the order'),
 ('Resumo enviado para ti', 'Summary sent to you'),
 ('Registo de exemplo. É isto que vês depois de um agente trabalhar.', 'Example log. This is what you see after an agent has worked.'),
 ('Rigor em cada passo.', 'Rigour at every step.'),
 ('Confiança em cada resultado.', 'Confidence in every result.'),
 ('O símbolo da Outrise feito de partículas a rodar: uma órbita aberta de onde sai um ponto azul.', 'The Outrise symbol made of moving particles: an open orbit with a blue dot leaving it.'),
 ('Exemplo de registo de um agente: leu três emails e a encomenda, corrigiu e reenviou a fatura, verificou o total e entregou um resumo.', 'Example agent log: read three emails and the order, corrected and resent the invoice, checked the total and delivered a summary.'),
 ('Exemplo de pedido', 'Example request'),
 ('Outrise, voltar ao início', 'Outrise, back to top'),
 ('Outrise, início', 'Outrise, home'),
 # demo tabs
 ('"Trata das faturas com erro deste mês"', '"Sort out this month’s wrong invoices"'),
 ('"A cruzar 42 faturas com as encomendas"', '"Matching 42 invoices against orders"'),
 ('"3 faturas com o total errado, corrigidas"', '"3 invoices with wrong totals, corrected"'),
 ('"Clientes avisados e registo guardado"', '"Customers notified and log saved"'),
 # script messages
 ('"Email copiado"', '"Email copied"'), ('"Não deu para copiar"', '"Couldn’t copy"'), ('"Copiar email"', '"Copy email"'),
 ('"Fechar menu"', '"Close menu"'), ('"Abrir menu"', '"Open menu"'),
 ('badEmail:"Escreve um email válido."', 'badEmail:"Enter a valid email."'),
 ('consent:"Para te contactarmos precisamos do teu consentimento."', 'consent:"We need your consent to contact you."'),
 ('sending:"A enviar…"', 'sending:"Sending…"'),
 ('fail:"Não conseguimos guardar. Tenta outra vez ou escreve para ola@outrise.technology."', 'fail:"We couldn’t save that. Try again or write to ola@outrise.technology."'),
 # subtitles: English page shows no subtitles by default
 ('<track kind="subtitles" srclang="pt" label="Português" src="media/outrise-film.pt.vtt" default><track kind="captions" srclang="en" label="English" src="media/outrise-film.en.vtt">', '<track kind="captions" srclang="en" label="English" src="media/outrise-film.en.vtt"><track kind="subtitles" srclang="pt" label="Português" src="media/outrise-film.pt.vtt">'),
 # company copy
 ('<title>Outrise · Agentes de IA à medida para empresas</title>', '<title>Outrise · Custom AI agents for businesses</title>'),
 ('Aceitamos novos projetos. Fala connosco.', 'Now taking on new projects. Talk to us.'),
 ('Desenhamos e construímos agentes de IA que tratam do trabalho repetitivo das empresas.', 'We design and build AI agents that take repetitive work off businesses.'),
 ('<p>Desenhamos e construímos agentes que entram nos processos que já existem e trabalham com as ferramentas da tua equipa.</p>', '<p>We design and build agents that fit into the processes you already have and work with your team’s tools.</p>'),
 ('<p>Olhamos para o trabalho da tua equipa e dizemos-te onde um agente compensa, quanto tempo poupa e onde ainda não vale a pena.</p>', '<p>We look at your team’s work and tell you where an agent pays off, how much time it saves, and where it isn’t worth it yet.</p>'),
 ('Uma pessoa decide o que importa.', 'A person signs off on what matters.'),
 ('Pagamentos, mensagens a clientes e decisões sensíveis passam primeiro pela aprovação de alguém da tua equipa.', 'Payments, messages to customers and sensitive decisions go to someone on your team for approval first.'),
 ('Acesso só ao necessário.', 'Access only to what’s needed.'),
 ('Cada agente acede apenas às ferramentas e aos dados de que a tarefa precisa, e cada acesso fica registado.', 'Each agent only reaches the tools and data the task needs, and every access is logged.'),
 ('Do primeiro pedido a um agente em produção.', 'From the first request to an agent in production.'),
 ('Começamos pequeno, provamos com o teu trabalho real e só pomos em produção quando o agente faz o trabalho sozinho.', 'We start small, prove it on your real work, and only go live once the agent does the job on its own.'),
 ('Percebemos o processo e onde um agente compensa.', 'We map the process and where an agent pays off.'),
 ('Um agente a trabalhar sobre casos reais, ao lado da equipa.', 'An agent working on real cases, alongside your team.'),
 ('Ligado às vossas ferramentas, com aprovações onde importa.', 'Connected to your tools, with sign-offs where they matter.'),
 ('Medimos resultados e afinamos o agente com o tempo.', 'We measure results and keep tuning the agent over time.'),
 ('Do pedido à produção', 'From request to production'),
 ('<h2 class="h2"><b>Fala connosco sobre um projeto.</b></h2>', '<h2 class="h2"><b>Talk to us about a project.</b></h2>'),
 ('Conta-nos que trabalho gostavas de tirar das mãos da tua equipa. Respondemos com uma primeira opinião sobre se um agente compensa.', 'Tell us what work you’d like to take off your team’s hands. We’ll reply with a first view on whether an agent pays off.'),
 ('<span>Empresa <i>Opcional</i></span>', '<span>Company <i>Optional</i></span>'),
 ('O que gostavas de entregar a um agente? <i>Opcional</i>', 'What would you like to hand to an agent? <i>Optional</i>'),
 ('Aceito que a Outrise guarde estes dados para responder ao meu contacto. Ver a <a href="privacidade.html">política de privacidade</a>.', 'I agree that Outrise may keep these details to reply to my message. See the <a href="privacy.html">privacy policy</a>.'),
 ('done:"Obrigado. Recebemos o teu contacto e respondemos em breve."', 'done:"Thank you. We’ve got your message and will reply soon."'),
 ('subject:"Contacto pelo site da Outrise"', 'subject:"Message from the Outrise website"'),
 # team
 ('content="A Outrise ajuda empresas a desenhar e construir agentes de IA que tratam do trabalho repetitivo: faturas, marcações, apoio ao cliente. Do diagnóstico à entrega."', 'content="Outrise helps businesses design and build AI agents that take on repetitive work: invoices, bookings, customer support. From assessment to delivery."'),
 ('<meta name="twitter:description" content="Ajudamos empresas a construir agentes de IA à medida. Fala connosco sobre um projeto.">', '<meta name="twitter:description" content="We help businesses build custom AI agents. Talk to us about a project.">'),
 ('content="Ajudamos empresas a construir agentes de IA à medida. Fala connosco sobre um projeto."', 'content="We help businesses build custom AI agents. Talk to us about a project."'),
 ('Do diagnóstico à entrega, ao lado da tua equipa.', 'From assessment to delivery, alongside your team.'),
 ('Ajudamos-te do princípio ao fim: percebemos onde um agente compensa, construímo-lo à medida e mantemo-lo a funcionar.', 'We help from start to finish: we find where an agent pays off, build it to fit, and keep it running.'),
 ('Onde está a encomenda 4521?', 'Where is order 4521?'),
 ('Enviada hoje. O cliente já tem o código de seguimento.', 'Shipped today. The customer already has the tracking code.'),
 ('<p>Depois de entregue, mantemos o agente a funcionar, medimos o tempo que poupa e afinamo-lo à medida que o negócio muda.</p>', '<p>Once it’s live, we keep the agent running, measure the time it saves and tune it as your business changes.</p>'),
 ('pessoas: ["Responde aos emails sobre o estado das encomendas de hoje", ["A ler 18 emails e a consultar as encomendas", "16 respondidos com o estado e o código de envio", "2 casos passados à equipa, com resumo"]]', 'pessoas: ["Answer today’s emails about order status", ["Reading 18 emails and checking the orders", "16 answered with status and tracking code", "2 cases handed to the team, with a summary"]]'),
 ('Criou a Outrise para ajudar empresas a tirar das mãos das equipas o trabalho repetitivo que ninguém quer fazer. Escolhe com cada cliente que problemas vale a pena resolver e acompanha cada projeto, do primeiro pedido ao lançamento.', 'Started Outrise to help businesses take the repetitive work nobody wants off their teams’ hands. Works with each client to choose which problems are worth solving, and follows every project from the first request to launch.'),
 ('<b>A aceitar novos projetos.</b> Conta-nos o que a tua equipa gostava de deixar de fazer à mão.', '<b>Taking on new projects.</b> Tell us what your team would like to stop doing by hand.'),
 ('<p class="about">Ajudamos empresas a construir agentes de IA à medida.</p>', '<p class="about">We help businesses build custom AI agents.</p>'),
 ('<b>Quem está por trás.</b> Pessoas, não só agentes.', '<b>Who is behind it.</b> People, not just agents.'),
 # footer
 ('<a href="privacidade.html">Privacidade</a>', '<a href="privacy.html">Privacy</a>'),
 ('Feito em Portugal', 'Made in Portugal'),
 ('© 2026 Outrise', '© 2026 Outrise'),
]
# short labels: only whole text nodes or exact attribute values
SHORT = {
 'Como trabalhamos':'How we work',
 'Falar connosco':'Talk to us',
 'NOVO':'NEW',
 'Marcações':'Bookings',
 'Faturas':'Invoices',
 'Apoio ao cliente':'Customer support',
 'Relatórios':'Reports',
 'Encomendas':'Orders',
 'Apresentação':'Film',
 'Pedido':'Request',
 'Agente':'Agent',
 'Trabalho':'Work',
 'Registo':'Log',
 'Como trabalham':'How they work',
 'Passo a passo':'Step by step',
 'a ler':'reading',
 'a fazer':'doing',
 'a verificar':'checking',
 'Tarefas feitas':'Tasks done',
 'Seg':'Mon',
 'Sex':'Fri',
 'Registo de cada passo':'Every step logged',
 'Lido':'Read',
 'Feito':'Done',
 'Verificado':'Checked',
 'Entregue':'Delivered',
 'O que nos guia':'What guides us',
 'Fiabilidade':'Reliability',
 'Transparência':'Transparency',
 'Robustez':'Robustness',
 'Simplicidade':'Simplicity',
 'Qualidade':'Quality',
 'Resultados':'Results',
 'Nome':'Name',
 'Não preencher':'Leave empty',
 'Copiar email':'Copy email',
 'Empresa':'Company',
 'Quem somos':'About us',
 'Fundador':'Founder',
 'Contacto':'Contact',
 'O que fazemos':'What we do',
 'Agentes à medida':'Custom agents',
 'Diagnóstico':'Assessment',
 'Falar sobre um projeto':'Talk about a project',
 'Pedir um diagnóstico':'Ask for an assessment',
 'O teu processo?':'Your process?',
 'Protótipo':'Prototype',
 'Entrega':'Delivery',
 'Acompanhamento':'Ongoing support',
 'Enviar':'Send',
 'Menu':'Menu',
 'Respondido':'Answered',
 'Ver como trabalhamos':'See how we work',
}
en = src
for a, b in EN:
    if a not in en: raise SystemExit("missing: " + a[:80])
    en = en.replace(a, b)
for a, b in SHORT.items():
    n = en.count(">" + a + "<") + en.count('"' + a + '"')
    if not n: raise SystemExit("missing short: " + a)
    en = en.replace(">" + a + "<", ">" + b + "<").replace('aria-label="' + a + '"', 'aria-label="' + b + '"')
en = en.replace('Preferes email?', 'Prefer email?')
# pt/ lives one folder down
pt = src
for d in ("fonts/", "media/", "favicon.svg", "favicon-32.png", "apple-touch-icon.png", "site.webmanifest"):
    pt = pt.replace('"' + d, '"../' + d).replace("'" + d, "'../" + d)
left = [w for w in ("Construímos","Fiáveis","Pede ","Copiar","Feito em","agentes de IA que tratam","Narrado","conta-nos","Preferes") if w in en]
if left: raise SystemExit("untranslated: " + ", ".join(left))
import json
def ld(lang):
    pt = lang == "pt"
    url = "https://www.outrise.technology/" + ("pt/" if pt else "")
    org = {"@type": "Organization", "@id": "https://www.outrise.technology/#org", "name": "Outrise", "url": "https://www.outrise.technology/",
           "logo": "https://www.outrise.technology/apple-touch-icon.png", "email": "ola@outrise.technology",
           "description": "Ajudamos empresas a construir agentes de IA à medida." if pt else "We help businesses build custom AI agents.",
           "knowsAbout": ["AI agents", "Automation", "Artificial intelligence"],
           "founder": {"@type": "Person", "name": "Nuno Namora", "image": "https://www.outrise.technology/media/nuno-600.jpg", "jobTitle": "Fundador" if pt else "Founder"},
           "foundingLocation": {"@type": "Place", "name": "Portugal"}, "areaServed": "PT",
           "sameAs": ["https://github.com/outrise-labs"]}
    site = {"@type": "WebSite", "@id": url + "#site", "url": url, "name": "Outrise", "inLanguage": "pt-PT" if pt else "en", "publisher": {"@id": "https://www.outrise.technology/#org"}}
    page = {"@type": "WebPage", "@id": url + "#page", "url": url, "name": "Outrise", "inLanguage": "pt-PT" if pt else "en", "isPartOf": {"@id": url + "#site"},
            "about": {"@id": "https://www.outrise.technology/#org"}, "primaryImageOfPage": "https://www.outrise.technology/media/" + ("og.png" if pt else "og-en.png")}
    video = {"@type": "VideoObject", "name": "Outrise", "description": ("Apresentação da Outrise: agentes de IA que tratam do trabalho por ti. Narrado em inglês." if pt else "Outrise in 32 seconds: AI agents that take care of the work for you."),
             "thumbnailUrl": "https://www.outrise.technology/media/outrise-film-poster.webp", "uploadDate": "2026-11-21", "duration": "PT32S",
             "contentUrl": "https://www.outrise.technology/media/outrise-film.mp4", "inLanguage": "en"}
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [org, site, page, video]}, ensure_ascii=False) + '</script>'
en = en.replace("<!--LD-->", ld("en"))
pt = pt.replace("<!--LD-->", ld("pt"))
open("index.html", "w").write(en)
os.makedirs("pt", exist_ok=True)
open("pt/index.html", "w").write(pt)

# sitemap, robots and web manifest
open("sitemap.xml", "w").write('''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>https://www.outrise.technology/</loc><lastmod>2026-11-21</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="https://www.outrise.technology/"/>
    <xhtml:link rel="alternate" hreflang="pt-PT" href="https://www.outrise.technology/pt/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.outrise.technology/"/></url>
  <url><loc>https://www.outrise.technology/pt/</loc><lastmod>2026-11-21</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="https://www.outrise.technology/"/>
    <xhtml:link rel="alternate" hreflang="pt-PT" href="https://www.outrise.technology/pt/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.outrise.technology/"/></url>
</urlset>
''')
open("robots.txt", "w").write("User-agent: *\nAllow: /\n\nSitemap: https://www.outrise.technology/sitemap.xml\n")
open("site.webmanifest", "w").write(json.dumps({"name": "Outrise", "short_name": "Outrise", "start_url": "/", "display": "standalone",
  "background_color": "#050506", "theme_color": "#050506",
  "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, indent=2))

# privacy pages
STYLE = '''<style>@font-face{font-family:"Outrise Sans";font-weight:400;src:url("%sfonts/OutriseSans-Regular.woff2") format("woff2")}@font-face{font-family:"Outrise Sans";font-weight:500;src:url("%sfonts/OutriseSans-Medium.woff2") format("woff2")}
body{margin:0;background:#fff;color:#050506;font:400 1.0625rem/1.6 "Outrise Sans","Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased}
main{max-width:720px;margin:0 auto;padding:56px 24px 96px}
a{color:#2B3BFF;text-underline-offset:3px}
.back{display:inline-flex;align-items:center;gap:8px;color:#050506;text-decoration:none;font-weight:500}
.back svg{width:30px;height:25px}
h1{font-weight:500;font-size:clamp(2rem,5vw,2.8rem);line-height:1.1;letter-spacing:-.03em;margin:48px 0 8px}
h2{font-weight:500;font-size:1.25rem;letter-spacing:-.01em;margin:36px 0 6px}
p,li{color:#33343B} .meta{color:#6A6A76;font-size:.9375rem}
.note{margin-top:40px;padding:16px 18px;border-radius:10px;background:#F4F4F7;color:#4B4F58;font-size:.9375rem}</style>'''
LOGO = '<svg viewBox="9.46 18.72 87.85 73.24" aria-hidden="true"><path fill="#050506" d="%s"/><circle fill="#050506" cx="73.77" cy="48.22" r="7.46"/><circle fill="#050506" cx="64.22" cy="34.06" r="4.54"/><circle fill="#2B3BFF" cx="87.11" cy="28.92" r="10.2"/></svg>' % ORBIT
PT_P = '''<!DOCTYPE html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Privacidade · Outrise</title><meta name="robots" content="noindex"><link rel="icon" href="../favicon.svg" type="image/svg+xml">%s<script defer src="/_vercel/insights/script.js"></script></head><body><main>
<a class="back" href="./">%s outrise</a>
<h1>Política de privacidade</h1><p class="meta">Última atualização: 21 de novembro de 2026 · <a href="../privacy.html" lang="en">English</a></p>
<p>Esta página explica que dados a Outrise recolhe neste site, para quê e que direitos tens.</p>
<h2>Quem é responsável</h2><p>A Outrise é responsável pelos dados recolhidos em outrise.technology. Para qualquer questão sobre privacidade, escreve para <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>.</p>
<h2>Que dados recolhemos</h2><ul><li><b>Formulário de contacto:</b> o nome (se o indicares), o email, a empresa (opcional), a mensagem opcional, a língua da página e a data do pedido.</li><li><b>Estatísticas de visitas:</b> usamos o Vercel Web Analytics, que conta visitas de forma agregada, sem cookies e sem identificar quem visita.</li></ul>
<h2>Para que os usamos</h2><p>Usamos estes dados apenas para responder ao teu contacto e falar contigo sobre o teu projeto. Não vendemos nem partilhamos estes dados para publicidade.</p>
<h2>Base legal</h2><p>O teu consentimento, dado quando marcas a caixa no formulário. Podes retirá-lo a qualquer momento, sem afetar o que foi feito antes.</p>
<h2>Onde ficam guardados</h2><p>Os pedidos chegam-nos por email, para ola@outrise.technology. Se passarmos a guardá-los numa base de dados, será alojada na União Europeia e atualizamos esta página. O site é servido pela Vercel.</p>
<h2>Durante quanto tempo</h2><p>Até pedires para os apagar, ou no máximo 24 meses depois do último contacto.</p>
<h2>Os teus direitos</h2><p>Podes pedir acesso, correção ou eliminação dos teus dados, opor-te ao tratamento e pedir a portabilidade, escrevendo para <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>. Se achares que os teus direitos não foram respeitados, podes apresentar queixa à Comissão Nacional de Proteção de Dados (<a href="https://www.cnpd.pt">cnpd.pt</a>).</p>
</main></body></html>'''
EN_P = '''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Privacy · Outrise</title><meta name="robots" content="noindex"><link rel="icon" href="favicon.svg" type="image/svg+xml">%s<script defer src="/_vercel/insights/script.js"></script></head><body><main>
<a class="back" href="./">%s outrise</a>
<h1>Privacy policy</h1><p class="meta">Last updated: 21 November 2026 · <a href="pt/privacidade.html" lang="pt">Português</a></p>
<p>This page explains what data Outrise collects on this site, why, and what rights you have.</p>
<h2>Who is responsible</h2><p>Outrise is responsible for the data collected on outrise.technology. For any privacy question, write to <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>.</p>
<h2>What we collect</h2><ul><li><b>Contact form:</b> your name (if you give it), your email, your company (optional), the optional message, the page language and the date of the request.</li><li><b>Visit statistics:</b> we use Vercel Web Analytics, which counts visits in aggregate, without cookies and without identifying visitors.</li></ul>
<h2>What we use it for</h2><p>We use this data only to reply to your message and talk with you about your project. We do not sell this data or share it for advertising.</p>
<h2>Legal basis</h2><p>Your consent, given when you tick the box on the form. You can withdraw it at any time, without affecting anything done before.</p>
<h2>Where it is stored</h2><p>Requests reach us by email, at ola@outrise.technology. If we start keeping them in a database, it will be hosted in the European Union and we will update this page. The site is served by Vercel.</p>
<h2>How long we keep it</h2><p>Until you ask us to delete it, or at most 24 months after our last contact.</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data, object to its use and ask for portability by writing to <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>. If you believe your rights were not respected, you can complain to the Portuguese data protection authority, CNPD (<a href="https://www.cnpd.pt">cnpd.pt</a>).</p>
</main></body></html>'''
open("pt/privacidade.html", "w").write(PT_P % (STYLE % ("../", "../"), LOGO))
open("privacy.html", "w").write(EN_P % (STYLE % ("", ""), LOGO))
print("built", len(src), len(en))
