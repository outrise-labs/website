"""Builds the site from src.html: Portuguese at the root, English under en/, plus the privacy pages.
Usage: python3 build.py [supabase_url] [publishable_key]"""
import sys, os, re
URL = sys.argv[1] if len(sys.argv) > 1 else ""
KEY = sys.argv[2] if len(sys.argv) > 2 else ""
ORBIT = open("orbit_path.txt").read().strip()
src = open("src.html").read().replace("__ORBIT__", ORBIT).replace("__WL_URL__", URL).replace("__WL_KEY__", KEY)

EN = [
 # head
 ('<html lang="pt-PT">', '<html lang="en">'),
 ('<title>Outrise · Produtos com agentes de IA</title>', '<title>Outrise · AI agent products</title>'),
 ('content="A Outrise cria produtos com agentes de IA que resolvem problemas reais de pessoas e empresas. Primeiros produtos em construção."', 'content="Outrise builds AI agent products that solve real problems for people and businesses. First products in the works."'),
 ('<link rel="canonical" href="https://www.outrise.technology/">', '<link rel="canonical" href="https://www.outrise.technology/en/">'),
 ('<meta property="og:locale" content="pt_PT">', '<meta property="og:locale" content="en_GB">'),
 ('<meta property="og:url" content="https://www.outrise.technology/">', '<meta property="og:url" content="https://www.outrise.technology/en/">'),
 ('content="Outrise · Construímos soluções de IA em que podes confiar"', 'content="Outrise · AI solutions you can trust"'),
 ('content="Produtos com agentes de IA para pessoas e empresas. Pede acesso antecipado."', 'content="AI agent products for people and businesses. Request early access."'),
 ('media/og.png"', 'media/og-en.png"'),
 ('<a class="lang" href="en/" hreflang="en" lang="en">EN<span class="sr"> English version</span></a>', '<a class="lang" href="../" hreflang="pt" lang="pt">PT<span class="sr"> Versão em português</span></a>'),
 # long sentences first
 ('Primeiros produtos em construção. Pede acesso antecipado.', 'First products in the works. Request early access.'),
 ('Construímos soluções de IA', 'We build AI solutions'),
 ('em que podes confiar', 'you can trust'),
 ('Transformamos problemas reais em produtos com agentes de IA.', 'We turn real problems into products built on AI agents.'),
 ('Fiáveis, robustos e simples de usar.', 'Reliable, robust and simple to use.'),
 ('Trabalho que queremos tirar das tuas mãos', 'Work we want to take off your hands'),
 ('O que construímos, para quem e com que princípios. Narrado em inglês.', 'What we build, for whom, and the principles behind it.'),
 ('Agentes de IA que tratam do trabalho por ti.', 'AI agents that take care of the work for you.'),
 ('Vê como funciona.', 'See how it works.'),
 ('Ver a apresentação da Outrise', 'Watch the film about Outrise'),
 ('Ver a apresentação', 'Watch the film'),
 ('Há trabalho que ninguém quer fazer.', 'Some work nobody wants to do.'),
 ('Os nossos agentes fazem-no.', 'Our agents do it.'),
 ('Cada produto nasce de um problema concreto e é construído à volta de agentes que tratam dele até ao fim.', 'Every product starts from a concrete problem and is built around agents that see it through.'),
 ('Marca a revisão do carro para a próxima semana.', 'Book my car service for next week.'),
 ('Terça, às 10h00. A confirmação está no teu email.', 'Tuesday at 10:00. The confirmation is in your inbox.'),
 ('Pedes em linguagem normal e recebes a coisa feita, sem formulários nem menus.', 'Ask in plain language and get it done, with no forms or menus.'),
 ('Agentes que entram nos processos que já existem e trabalham com as ferramentas da equipa.', 'Agents that fit into the processes you already have and work with your team’s tools.'),
 ('Não fazemos um produto só. Se tens um problema que merecia um agente, pode ser o próximo.', 'We don’t make just one product. If you have a problem that deserves an agent, it could be the next one.'),
 ('Agentes que trabalham sozinhos, com tudo à vista', 'Agents that work on their own, in plain sight'),
 ('Fazer, e não só responder.', 'Doing, not just answering.'),
 ('Um agente nosso acaba a tarefa. Se não consegue, diz onde parou e porquê.', 'Our agents finish the task. If one can’t, it tells you where it stopped and why.'),
 ('Mostrar o trabalho.', 'Showing the work.'),
 ('Tudo o que um agente faz fica registado, para poderes ver, corrigir e confiar.', 'Everything an agent does is logged, so you can check it, correct it and trust it.'),
 ('Simples por fora.', 'Simple on the outside.'),
 ('A complexidade fica do nosso lado. Tu pedes em linguagem normal e recebes a coisa feita.', 'The complexity stays on our side. You ask in plain language and get it done.'),
 ('Cada tarefa passa por ler, fazer e verificar antes de ser entregue.', 'Every task is read, done and checked before it is delivered.'),
 ('Números de exemplo, para mostrar o painel.', 'Example figures, to show the dashboard.'),
 ('3 emails do cliente e a encomenda', '3 customer emails and the order'),
 ('Fatura corrigida e reenviada', 'Invoice corrected and resent'),
 ('O total confere com a encomenda', 'The total matches the order'),
 ('Resumo enviado para ti', 'Summary sent to you'),
 ('Registo de exemplo. É isto que vês depois de um agente trabalhar.', 'Example log. This is what you see after an agent has worked.'),
 ('Rigor em cada passo.', 'Rigour at every step.'),
 ('Confiança em cada resultado.', 'Confidence in every result.'),
 ('A base de como um produto sai daqui.', 'How a product leaves our hands.'),
 ('Partimos de um pedido real, pomos um agente a tratar dele e só lançamos quando faz o trabalho sozinho.', 'We start from a real request, put an agent on it, and only launch once it does the work on its own.'),
 ('Deixa o teu contacto e avisamos-te quando os primeiros produtos estiverem prontos. Se nos contares o problema, dizemos-te se um agente o resolve.', 'Leave your details and we’ll let you know when the first products are ready. Tell us the problem and we’ll tell you whether an agent can solve it.'),
 ('Pede acesso antecipado.', 'Request early access.'),
 ('Que trabalho gostavas de entregar a um agente? <i>Opcional</i>', 'What work would you hand to an agent? <i>Optional</i>'),
 ('Aceito que a Outrise guarde estes dados para me contactar sobre o acesso antecipado. Ver a <a href="privacidade.html">política de privacidade</a>.', 'I agree that Outrise may keep these details to contact me about early access. See the <a href="privacy.html">privacy policy</a>.'),
 ('Produtos com agentes de IA para pessoas e empresas.', 'AI agent products for people and businesses.'),
 ('O símbolo da Outrise feito de partículas a rodar: uma órbita aberta de onde sai um ponto azul.', 'The Outrise symbol made of moving particles: an open orbit with a blue dot leaving it.'),
 ('Exemplo de registo de um agente: leu três emails e a encomenda, corrigiu e reenviou a fatura, verificou o total e entregou um resumo.', 'Example agent log: read three emails and the order, corrected and resent the invoice, checked the total and delivered a summary.'),
 ('Do problema ao produto', 'From problem to product'),
 ('Exemplo de pedido', 'Example request'),
 ('Outrise, voltar ao início', 'Outrise, back to top'),
 ('Outrise, início', 'Outrise, home'),
 # demo tabs
 ('"Marca a revisão do carro para a próxima semana"', '"Book my car service for next week"'),
 ('"A ver a tua agenda e os horários da oficina"', '"Checking your calendar and the garage’s slots"'),
 ('"Terça às 10h00 está livre nos dois lados"', '"Tuesday at 10:00 works for both"'),
 ('"Marcação feita e confirmada por email"', '"Booked and confirmed by email"'),
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
 ('done:"Obrigado. Estás na lista e falamos contigo em breve."', 'done:"Thank you. You’re on the list and we’ll be in touch soon."'),
 ('fail:"Não conseguimos guardar. Tenta outra vez ou escreve para ola@outrise.technology."', 'fail:"We couldn’t save that. Try again or write to ola@outrise.technology."'),
 ('subject:"Acesso antecipado à Outrise"', 'subject:"Outrise early access"'),
 # subtitles: English page shows no subtitles by default
 ('<track kind="subtitles" srclang="pt" label="Português" src="media/outrise-film.pt.vtt" default><track kind="captions" srclang="en" label="English" src="media/outrise-film.en.vtt">', '<track kind="captions" srclang="en" label="English" src="media/outrise-film.en.vtt"><track kind="subtitles" srclang="pt" label="Português" src="media/outrise-film.pt.vtt">'),
 # team
 ('<b>Quem está por trás.</b> Pessoas, não só agentes.', '<b>Who is behind it.</b> People, not just agents.'),
 ('Criou a Outrise para tirar das mãos de pessoas e empresas o trabalho repetitivo que ninguém quer fazer. Escolhe que problemas vale a pena resolver e acompanha cada produto, do primeiro pedido ao lançamento.', 'Started Outrise to take the repetitive work nobody wants off the hands of people and businesses. Chooses which problems are worth solving and follows every product from the first request to launch.'),
 ('<b>Primeiro produto em construção.</b> Os primeiros acessos abrem por convite, a partir da lista de espera.', '<b>First product in the works.</b> Early access opens by invitation, starting with the waitlist.'),
 # footer
 ('<a href="privacidade.html">Privacidade</a>', '<a href="privacy.html">Privacy</a>'),
 ('Feito em Portugal', 'Made in Portugal'),
 ('© 2026 Outrise', '© 2026 Outrise'),
]
# short labels: only whole text nodes or exact attribute values
SHORT = {
 'Como trabalhamos':'How we work', 'Falar connosco':'Talk to us', 'Produtos':'Products', 'Agentes':'Agents', 'NOVO':'NEW',
 'Ver como funciona':'See how it works', 'Marcações':'Bookings', 'Faturas':'Invoices', 'Apoio ao cliente':'Customer support',
 'Relatórios':'Reports', 'Encomendas':'Orders', 'Apresentação':'Film', 'Porquê a Outrise':'Why Outrise', 'Pedido':'Request',
 'Marcado':'Booked', 'Para pessoas':'For people', 'Quero experimentar':'I want to try it', 'Agente':'Agent', 'Trabalho':'Work',
 'Registo':'Log', 'Para empresas':'For businesses', 'Falar com a equipa':'Talk to the team', 'Em construção':'In the works',
 'O teu problema?':'Your problem?', 'Uma casa de produtos':'A house of products', 'Propor um problema':'Suggest a problem',
 'Como trabalham':'How they work', 'Passo a passo':'Step by step', 'a ler':'reading', 'a fazer':'doing', 'a verificar':'checking',
 'Tarefas feitas':'Tasks done', 'Seg':'Mon', 'Sex':'Fri', 'Registo de cada passo':'Every step logged', 'Lido':'Read', 'Feito':'Done',
 'Verificado':'Checked', 'Entregue':'Delivered', 'O que nos guia':'What guides us', 'Fiabilidade':'Reliability',
 'Transparência':'Transparency', 'Robustez':'Robustness', 'Simplicidade':'Simplicity', 'Qualidade':'Quality', 'Resultados':'Results',
 'Problema real':'Real problem', 'Agente a trabalhar':'Agent at work', 'Produto lançado':'Product launched', 'Pessoas':'People',
 'Empresas':'Businesses', 'Acesso antecipado':'Early access', 'Nome':'Name', 'É para':'It’s for', 'Mim':'Me',
 'A minha empresa':'My company', 'Não preencher':'Leave empty', 'Pedir acesso':'Request access', 'Copiar email':'Copy email',
 'Empresa':'Company', 'Quem somos':'About us', 'Fundador':'Founder', 'Contacto':'Contact', 'Menu':'Menu',
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
# en/ lives one folder down
for d in ("fonts/", "media/", "favicon.svg", "favicon-32.png", "apple-touch-icon.png"):
    en = en.replace('"' + d, '"../' + d).replace("'" + d, "'../" + d)
left = [w for w in ("Construímos","Fiáveis","Pede ","Copiar","Feito em","agentes de IA que tratam","Narrado","conta-nos","Preferes") if w in en]
if left: raise SystemExit("untranslated: " + ", ".join(left))
open("index.html", "w").write(src)
os.makedirs("en", exist_ok=True)
open("en/index.html", "w").write(en)

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
PT_P = '''<!DOCTYPE html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Privacidade · Outrise</title><meta name="robots" content="noindex"><link rel="icon" href="favicon.svg" type="image/svg+xml">%s<script defer src="/_vercel/insights/script.js"></script></head><body><main>
<a class="back" href="./">%s outrise</a>
<h1>Política de privacidade</h1><p class="meta">Última atualização: 21 de novembro de 2026 · <a href="en/privacy.html" lang="en">English</a></p>
<p>Esta página explica que dados a Outrise recolhe neste site, para quê e que direitos tens.</p>
<h2>Quem é responsável</h2><p>A Outrise é responsável pelos dados recolhidos em outrise.technology. Para qualquer questão sobre privacidade, escreve para <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>.</p>
<h2>Que dados recolhemos</h2><ul><li><b>Lista de espera:</b> o nome (se o indicares), o email, se o pedido é para ti ou para uma empresa, a mensagem opcional, a língua da página e a data do pedido.</li><li><b>Estatísticas de visitas:</b> usamos o Vercel Web Analytics, que conta visitas de forma agregada, sem cookies e sem identificar quem visita.</li></ul>
<h2>Para que os usamos</h2><p>Usamos os dados da lista de espera apenas para te contactar sobre o acesso antecipado aos produtos da Outrise e para perceber que problemas as pessoas querem resolver. Não vendemos nem partilhamos estes dados para publicidade.</p>
<h2>Base legal</h2><p>O teu consentimento, dado quando marcas a caixa no formulário. Podes retirá-lo a qualquer momento, sem afetar o que foi feito antes.</p>
<h2>Onde ficam guardados</h2><p>Os dados da lista de espera ficam numa base de dados gerida pela Supabase, alojada na União Europeia. O site é servido pela Vercel.</p>
<h2>Durante quanto tempo</h2><p>Até pedires para os apagar, ou no máximo 24 meses depois do último contacto.</p>
<h2>Os teus direitos</h2><p>Podes pedir acesso, correção ou eliminação dos teus dados, opor-te ao tratamento e pedir a portabilidade, escrevendo para <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>. Se achares que os teus direitos não foram respeitados, podes apresentar queixa à Comissão Nacional de Proteção de Dados (<a href="https://www.cnpd.pt">cnpd.pt</a>).</p>
</main></body></html>'''
EN_P = '''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Privacy · Outrise</title><meta name="robots" content="noindex"><link rel="icon" href="../favicon.svg" type="image/svg+xml">%s<script defer src="/_vercel/insights/script.js"></script></head><body><main>
<a class="back" href="./">%s outrise</a>
<h1>Privacy policy</h1><p class="meta">Last updated: 21 November 2026 · <a href="../privacidade.html" lang="pt">Português</a></p>
<p>This page explains what data Outrise collects on this site, why, and what rights you have.</p>
<h2>Who is responsible</h2><p>Outrise is responsible for the data collected on outrise.technology. For any privacy question, write to <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>.</p>
<h2>What we collect</h2><ul><li><b>Waitlist:</b> your name (if you give it), your email, whether the request is for you or a company, the optional message, the page language and the date of the request.</li><li><b>Visit statistics:</b> we use Vercel Web Analytics, which counts visits in aggregate, without cookies and without identifying visitors.</li></ul>
<h2>What we use it for</h2><p>We use waitlist data only to contact you about early access to Outrise products and to understand which problems people want solved. We do not sell this data or share it for advertising.</p>
<h2>Legal basis</h2><p>Your consent, given when you tick the box on the form. You can withdraw it at any time, without affecting anything done before.</p>
<h2>Where it is stored</h2><p>Waitlist data is kept in a database run by Supabase, hosted in the European Union. The site is served by Vercel.</p>
<h2>How long we keep it</h2><p>Until you ask us to delete it, or at most 24 months after our last contact.</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data, object to its use and ask for portability by writing to <a href="mailto:ola@outrise.technology">ola@outrise.technology</a>. If you believe your rights were not respected, you can complain to the Portuguese data protection authority, CNPD (<a href="https://www.cnpd.pt">cnpd.pt</a>).</p>
</main></body></html>'''
open("privacidade.html", "w").write(PT_P % (STYLE % ("", ""), LOGO))
open("en/privacy.html", "w").write(EN_P % (STYLE % ("../", "../"), LOGO))
print("built", len(src), len(en))
