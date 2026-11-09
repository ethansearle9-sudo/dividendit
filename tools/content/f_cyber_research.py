HISCOX = 'Hiscox Cyber Readiness Report 2026, a survey of 6,800 security decision-makers in the UK, Europe and the US, as reported by <a href="https://www.infosecurity-magazine.com/news/cyberattacks-cost-organizations/" target="_blank" rel="noopener">Infosecurity Magazine</a>.'
CSBS = '<a href="https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2025/cyber-security-breaches-survey-2025" target="_blank" rel="noopener">UK Government, Cyber Security Breaches Survey 2025</a>.'
DBIR = 'Verizon, <a href="https://www.verizon.com/business/resources/infographics/2025-dbir-smb-snapshot.pdf" target="_blank" rel="noopener">2025 Data Breach Investigations Report: SMB Snapshot</a>.'
IC3 = 'FBI Internet Crime Complaint Center, 2024 Internet Crime Report, as summarised by <a href="https://www.proofpoint.com/us/blog/email-and-cloud-threats/email-attacks-drive-record-cybercrime-losses-2024" target="_blank" rel="noopener">Proofpoint</a>.'
AFP = 'Association for Financial Professionals, <a href="https://www.financialprofessionals.org/about/learn-more/press-releases/Details/survey-79-percent-of-organizations-were-victims-of-attempted-or-actual-payments-fraud-activity-in-2024" target="_blank" rel="noopener">2025 Payments Fraud and Control Survey</a>.'
SOPHOS = 'Sophos, <a href="https://www.sophos.com/en-us/blog/the-state-of-ransomware-2025" target="_blank" rel="noopener">The State of Ransomware 2025</a>, a survey of 3,400 organisations hit by ransomware in 17 countries.'

PAGES = [
dict(
    kind='article', slug='cyber-risk',
    title='Cyber Attack Statistics for Small Businesses | Dividend IT',
    og_title='The cyber risk facing small and medium businesses: what the data says',
    meta='The cyber risk facing small and medium businesses, from the most reliable recent data: how often businesses are hit, how attackers get in and what it costs.',
    card_kind='Research', card_title='The Cyber Risk Facing SMBs: What the Data Says',
    card_desc='How often businesses are hit, how attackers get in and what it costs.',
    trail=[('Insights', '/insights'), ('The cyber risk facing SMBs', '/cyber-risk')],
    eyebrow='Cybersecurity research', read=7,
    h1='The cyber risk facing small and medium businesses: <em>what the data says</em>',
    sub='Nearly a third of businesses suffered a successful cyber attack in the past year. This is not a large-company problem, and the most reliable recent research makes that very clear. Here is what it shows, without the scare tactics.',
    sections=[
        ('scale', 'The scale of the problem', '''
<p>For years, cyber security was treated as something for banks and governments to worry about. The data has comprehensively overturned that view.</p>
<ul>
<li><strong>29% of businesses suffered at least one successful cyber attack in the past twelve months</strong>, and those that were hit were hit four times on average, according to the Hiscox Cyber Readiness Report 2026.</li>
<li>The UK Government's 2025 survey found that <strong>43% of businesses identified a breach or attack</strong> in the previous year, rising to <strong>67% of medium-sized businesses</strong>.</li>
</ul>
<p>The two surveys measure slightly different things, successful attacks in one and all identified breaches or attacks in the other, but they point the same way. For a business of any size, being targeted is now routine. The useful question is no longer whether it will happen. It is whether you will notice, and how ready you will be.</p>
'''),
        ('why-smb', 'Why smaller businesses are the target', '''
<p>Attackers go where the defences are weakest and the money still moves. Large enterprises have invested heavily in security teams and round-the-clock monitoring. Smaller businesses usually have limited IT budgets, no dedicated security staff and nobody watching outside office hours, and they still pay suppliers and hold customer data.</p>
<p>Verizon's 2025 Data Breach Investigations Report, the largest annual study of real incidents, shows the result:</p>
<ul>
<li>Small and medium organisations accounted for <strong>roughly three times as many incidents as large ones</strong> in its dataset: 3,049 against 982.</li>
<li><strong>99% of breaches of smaller organisations were financially motivated.</strong> This is organised crime, not mischief.</li>
<li><strong>Ransomware was present in 88% of breaches at smaller organisations</strong>, compared with 39% at large ones.</li>
</ul>
'''),
        ('how', 'How attackers actually get in', '''
<p>The routes in are consistent year after year, and none of them is exotic.</p>
<div class="tbl-wrap"><table class="cmp">
<tr><th>Route</th><th>What happens</th><th>What the data says</th></tr>
<tr><td>Phishing</td><td>A convincing email leads someone to a fake login page or a malicious file</td><td>Experienced by 85% of UK businesses that identified a breach or attack</td></tr>
<tr><td>Stolen passwords</td><td>Credentials taken by phishing, or reused from another site, are simply used to log in</td><td>The most common hacking technique in breaches of smaller organisations</td></tr>
<tr><td>Unpatched systems</td><td>A known weakness in software or a firewall is exploited before the fix is applied</td><td>The top technical root cause of ransomware attacks, at 32%</td></tr>
<tr><td>Suppliers</td><td>An attacker comes in through a trusted third party's access or software</td><td>Third-party involvement in breaches doubled to 30%</td></tr>
</table></div>
<p>Around 60% of breaches involve a human element: someone clicking, approving or being talked into something. That is not a criticism of staff. It is a reminder that controls have to work even when a busy person makes an ordinary mistake.</p>
<p>The most expensive version for smaller businesses is payment fraud by email. See <a href="/invoice-fraud">how invoice fraud works</a> and <a href="/how-to-spot-a-phishing-email">how to spot a phishing email</a>.</p>
'''),
        ('consequences', 'The consequences go well beyond the clean-up', '''
<p>Hiscox asked businesses that had been attacked what it did to them. The answers are the part most relevant to a shareholder.</p>
<ul>
<li><strong>30% reported a negative effect on financial performance, valuation or credit rating.</strong></li>
<li>32% said growth, expansion or new initiatives were delayed.</li>
<li>29% lost business opportunities or partnerships.</li>
<li>28% faced financial penalties, and 26% suffered negative publicity.</li>
<li>The average downtime after an incident was just under 33 hours.</li>
</ul>
<p>The average cost of cyber incidents to a business over the year was around <strong>$52,000</strong>. For the full breakdown of where that money goes, and why the true figure is usually higher, see <a href="/true-cost">the true cost of a cyber attack</a>.</p>
'''),
        ('good', 'What good looks like', '''
<p>The encouraging part of the data is how preventable most of this is. The routes in are well known, and a small number of well-run controls close them:</p>
<ul class="check">
<li>Multi-factor sign-in on every account</li>
<li>Protected email, and staff who know what a fraud attempt looks like</li>
<li>Managed detection and response on every device, with people watching</li>
<li>Updates applied everywhere, on time</li>
<li>Backups that are separate, protected and tested</li>
<li>A written plan for the first hour of an incident</li>
</ul>
<p>None of that requires a large budget or an internal security team. Our <a href="/outsourced-cyber">owner's guide to cyber security for small business</a> explains each one and how to decide whether to run them yourself or outsource them.</p>
'''),
        ('bottom-line', 'The bottom line', '''
<p>Over any meaningful period, a cyber attack on your business is a near certainty. Whether it becomes a non-event, a bad week or a threat to the value of what you have built depends on decisions made beforehand.</p>
<p>The cost of prevention is known and modest. The cost of an incident is neither. For owners who have spent years building something valuable, that is a straightforward calculation.</p>
'''),
    ],
    faqs=[
        ('What percentage of small businesses experience a cyber attack?', 'It depends on the survey and the definition. Hiscox found 29% of businesses suffered a successful attack in the past twelve months. The UK Government found 43% of all businesses, and 67% of medium-sized businesses, identified a breach or attack in a year.'),
        ('Why do hackers target small businesses?', 'Because smaller businesses typically have weaker defences and no round-the-clock monitoring, while still moving money and holding valuable data. Verizon found that 99% of breaches of smaller organisations were financially motivated.'),
        ('What is the most common cyber attack on small businesses?', 'Phishing. It was experienced by 85% of UK businesses that identified a breach or attack, and it is the usual starting point for stolen passwords, invoice fraud and ransomware.'),
    ],
    sources=[HISCOX, CSBS, DBIR, SOPHOS],
    related=['true-cost', 'outsourced-cyber', 'been-hacked-first-24-hours', 'invoice-fraud', 'signs-your-business-has-been-hacked', 'cyber-risk-assessment'],
    cta_h='Is your business protected?',
    cta_p='A 20-minute call for an honest read on your current security. No jargon, no obligation, just clarity on where you stand.',
    cta_secondary=('See a cyber risk assessment', '/cyber-risk-assessment'),
),
dict(
    kind='article', slug='true-cost',
    title='The True Cost of a Cyber Attack on a Business | Dividend IT',
    og_title='The true cost of a cyber attack on a business',
    meta='The true cost of a cyber attack on a business: direct recovery, payment fraud, downtime, lost opportunities and the effect on what the business is worth.',
    card_kind='Research', card_title='The True Cost of a Cyber Attack',
    card_desc='Where the money actually goes: recovery, fraud, downtime and business value.',
    trail=[('Insights', '/insights'), ('The true cost of a cyber attack', '/true-cost')],
    eyebrow='Financial impact research', read=7,
    h1='The true cost of a cyber attack on a business: <em>beyond the headline figure</em>',
    sub='Cyber incidents cost the average business around $52,000 a year. That number is real, and it still understates the problem, because the largest costs are the ones that never appear on an invoice. Here are the five places the money goes.',
    sections=[
        ('headline', 'The headline figure is only the beginning', '''
<p>The Hiscox Cyber Readiness Report 2026 puts the average cost of cyber incidents to a business at around <strong>$52,000 over twelve months</strong>. It is a useful anchor. It is also an average across thousands of businesses, many of which had a minor incident and a few of which had a catastrophic one.</p>
<p>For an owner, the more useful view is to look at the five categories of cost separately, because they behave very differently, and because the last one is the one that matters most when the business is valued.</p>
'''),
        ('remediation', 'Cost 1: Direct recovery', '''
<p>This is the visible bill: specialists to investigate and contain the incident, rebuilding systems, restoring data, replacing equipment and paying for legal and regulatory advice.</p>
<p>Where ransomware is involved, the numbers climb quickly. Across organisations of all sizes, Sophos found the average cost of recovering from a ransomware attack, before any ransom, was <strong>$1.53 million</strong>. Smaller businesses will usually be well below that, but the ratio to turnover can be just as painful.</p>
<p>The single largest factor in the size of this bill is whether there are clean, tested backups. See <a href="/backup-dr">backup and disaster recovery</a>.</p>
'''),
        ('fraud', 'Cost 2: Payment fraud', '''
<p>For most smaller businesses, this is the largest direct loss, and it often involves no damage to systems at all. An attacker gets into a mailbox, waits for a large payment and redirects it.</p>
<ul>
<li>The FBI recorded <strong>$2.77 billion in reported losses to business email compromise in 2024</strong>, from more than 21,000 complaints.</li>
<li><strong>79% of organisations experienced attempted or actual payments fraud in 2024</strong>, and business email compromise was the most common route, according to the Association for Financial Professionals.</li>
<li>Getting the money back is becoming harder. Only <strong>22% of organisations recovered 75% or more</strong> of the funds they lost, down from 41% the year before.</li>
</ul>
<p>A single diverted supplier payment can exceed everything else on this page. See <a href="/invoice-fraud">how invoice fraud works and how to stop it</a>.</p>
'''),
        ('downtime', 'Cost 3: Downtime and lost productivity', '''
<p>When systems are down, people are paid to wait, orders are not shipped and invoices are not sent. Hiscox found the average downtime after an incident was <strong>just under 33 hours</strong>, most of a working week.</p>
<p>The cost of an hour depends entirely on your business, so work out your own:</p>
<div class="note"><p><strong>A rough formula:</strong> (annual revenue &divide; working hours in a year) + (number of affected staff &times; their average hourly cost). Multiply by the hours you would be down. For a distribution or manufacturing business working to tight schedules, add any penalties for late delivery.</p></div>
<p>Then ask a harder question: how many hours would it actually take to restore your systems today? If nobody can answer, that is the first thing to find out.</p>
'''),
        ('opportunity', 'Cost 4: Lost opportunities and penalties', '''
<p>The effects carry on after systems are restored. Among businesses that had been attacked, Hiscox found:</p>
<ul>
<li>32% delayed growth, expansion or new business initiatives</li>
<li>31% faced higher costs for staff or outside expertise</li>
<li>29% lost business opportunities or partnerships</li>
<li>28% faced financial penalties</li>
<li>26% suffered negative publicity</li>
</ul>
<p>In sectors built on trust, such as financial services and professional advice, clients do not easily forgive a firm that loses control of their information. That loss rarely appears in any incident estimate and can outlast all the others.</p>
'''),
        ('value', 'Cost 5: What it does to the value of the business', '''
<p>This is the cost most owners never calculate. In the same Hiscox research, <strong>30% of businesses that were attacked reported a negative effect on their financial performance, valuation or credit rating</strong>.</p>
<p>The mechanics are simple. A business is valued on a multiple of its earnings. An incident hits both halves of that equation:</p>
<ul>
<li><strong>Earnings fall</strong> in the year of the incident, through every cost above.</li>
<li><strong>The multiple can fall too.</strong> A buyer who finds a recent breach, or weak controls, prices the risk in: a lower offer, a retention held back, or a deal that stalls in due diligence.</li>
</ul>
<p>If the incident lands in the year a buyer bases their offer on, a $50,000 hit to earnings is not a $50,000 problem. At a five times multiple it can mean a quarter of a million off the price, before any discount for risk. Our <a href="/value-calculator">value calculator</a> shows the effect for your own numbers.</p>
'''),
        ('prevention', 'The prevention calculation', '''
<div class="tbl-wrap"><table class="cmp">
<tr><th>Cost</th><th>How it behaves</th></tr>
<tr><td>Direct recovery</td><td>Tens of thousands for a contained incident, far more with ransomware and no usable backups</td></tr>
<tr><td>Payment fraud</td><td>The size of your largest supplier payment, and increasingly hard to recover</td></tr>
<tr><td>Downtime</td><td>Your hourly cost multiplied by days, not hours</td></tr>
<tr><td>Lost opportunities</td><td>Delayed plans, lost customers and penalties, lasting months</td></tr>
<tr><td>Business value</td><td>Lost earnings multiplied at exit, plus any discount for risk</td></tr>
</table></div>
<p>Against that, the cost of properly managed security is known in advance, fixed each month and a small fraction of any one of these lines. The business case is not a matter of opinion. It is arithmetic.</p>
<p>The controls that prevent most of it are set out in our <a href="/outsourced-cyber">owner's guide to cyber security for small business</a>.</p>
'''),
    ],
    faqs=[
        ('How much does a cyber attack cost a small business?', 'Hiscox puts the average cost of cyber incidents to a business at around $52,000 a year, but the range is very wide. A contained incident may cost a few thousand. A diverted payment or a ransomware attack without usable backups can cost many times the average.'),
        ('What is the biggest cost of a cyber attack?', 'For smaller businesses the largest direct loss is usually payment fraud, where a genuine payment is redirected to a criminal. The largest indirect cost is often the effect on business value, through lost earnings and a lower valuation multiple.'),
        ('Does cyber insurance cover the cost of an attack?', 'It can cover much of the direct cost, including incident response, restoration and business interruption, subject to the policy terms. Payment fraud is often excluded or covered at a lower limit. See our <a href="/cyber-insurance">guide to cyber insurance</a>.'),
    ],
    sources=[HISCOX, SOPHOS, IC3, AFP],
    related=['cyber-risk', 'invoice-fraud', 'cyber-insurance', 'outsourced-cyber', 'backup-dr', 'value-calculator'],
    cta_h='Know your real exposure.',
    cta_p='A 20-minute call for a clear, plain-English picture of where your business is exposed and what it would take to fix it.',
),
]
