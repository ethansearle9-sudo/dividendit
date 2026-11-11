"""Decision-stage pages.

These target the questions an owner actually types at the moment they are
deciding, rather than the vocabulary an IT buyer would use. The ICP has no
in-house IT person, so they do not search "managed service provider". They
search the decision in front of them.

Every figure on these pages is sourced and dated in the copy. If a number
cannot be sourced, it does not go on the page.
"""

PARENT = ('Insights', '/insights')


PAGES = [
dict(
    kind='service', slug='do-i-need-an-it-manager',
    service_name='Do You Need an IT Manager?',
    card_kind='Decision guide', card_title='Do You Need an IT Manager?',
    card_desc="What an IT manager really costs, and when hiring one is the right call.",
    eyebrow='Decision guide',
    trail=[PARENT, ('Do You Need an IT Manager?', '/do-i-need-an-it-manager')],

    title="Do You Need an IT Manager? What One Really Costs",
    meta="What an IT manager costs in Ireland in 2026, the full cost of the hire once everything is counted, and when hiring is the right answer.",
    h1="Do you need an <em>IT manager</em>?",
    lead="Most owners ask this at a particular moment: something broke, or the person who quietly handles IT is leaving. Here is the arithmetic, including the cases where hiring is the right answer.",

    glance=[('Median IT manager salary, Ireland', '€90,000 (roleup.ie, November 2026)'),
            ('System administrator, 3 to 5 years', '€40,000 to €55,000 (Hero IT Salary Guide 2026)'),
            ('True cost of the hire', 'Roughly 1.3 to 1.5 times salary once everything is counted'),
            ('When hiring wins', 'Above roughly 80 to 100 staff, or when IT is your product')],

    problem_label='The honest arithmetic',
    problem_h="The salary is the part everybody quotes. It is rarely the expensive part.",
    problem=[
        "An IT manager in Ireland has a median salary of <strong>€90,000</strong>, with most falling between €80,000 and €99,375, according to <a href=\"https://www.roleup.ie/salaries/role/it-manager/\" rel=\"nofollow\">roleup.ie</a> as of November 2026. Dublin typically pays 10 to 25 per cent above Cork, Galway and Limerick for the same role.",
        "But most businesses of 10 to 50 people do not actually need an IT manager. They need a competent system administrator, which the <a href=\"https://www.hero.ie/info-hub/it-salary-guide-ireland-2026\" rel=\"nofollow\">Hero IT Salary Guide 2026</a> puts at <strong>€40,000 to €55,000</strong> for someone with three to five years of experience, and €55,000 to €70,000 above that.",
        "Then add what the salary line does not include: employer PRSI of roughly 11 per cent, recruitment fees of 15 to 20 per cent of first-year salary, software and tooling that a managed provider would otherwise bundle, training to keep skills current, and cover for annual leave and illness. <strong>Count it properly and the real cost lands somewhere between 1.3 and 1.5 times the salary.</strong>",
        "So a €50,000 system administrator is realistically a €65,000 to €75,000 commitment in year one. That is the number to compare against, not €50,000.",
    ],

    included_h="What the salary line leaves out",
    included_intro="None of these are hidden. They are simply not in the number people quote when they say what an IT person costs.",
    included=[
        ("Employer PRSI", "Roughly 11 per cent on top of salary. On a €50,000 hire that is about €5,500 a year before anything else."),
        ("Recruitment", "Typically 15 to 20 per cent of first-year salary through an agency. Paid again each time the role turns over."),
        ("Tooling", "Remote monitoring, patching, antivirus, backup, ticketing and documentation. A managed provider buys these at scale and includes them. Alone, you pay list price."),
        ("Training and certification", "The skills decay. Keeping one person current costs money and takes them off the desk while they do it."),
        ("Cover", "Annual leave, illness, and the gap between someone resigning and their replacement being productive. For one person, that gap is total."),
        ("Single-person risk", "One individual holds every password, every supplier relationship and every undocumented decision. This is the cost nobody prices until the day it lands."),
    ],

    steps_h="How to decide, in four questions",
    steps=[
        ("Does an IT failure stop you earning?", "If an outage means orders are not placed and customers are not served, IT is revenue infrastructure and needs real cover, not one person with a mobile phone. If you could invoice on paper for a day, the urgency is genuinely lower."),
        ("How many people are you supporting?", "Below roughly 50 staff there is rarely enough work to keep a good person busy and interested. They either leave from boredom or stay and become expensive overhead. Above 80 to 100, the maths turns and a hire starts to make sense."),
        ("Can you actually hire and keep them?", "This is where most plans fail, particularly in Dublin, where you are bidding against multinationals who set the price. Being able to afford the salary is not the same as being able to win the candidate."),
        ("Who covers the other 16 hours?", "A single hire covers roughly a third of the week. Incidents do not respect that. Decide now what happens at 2am on a Saturday, because that is when it will matter."),
    ],

    value_h="What each option actually gives you",
    value_intro="This is not a case for outsourcing in every situation. It is a case for counting honestly.",
    value=[
        ("A hire gives you presence and context", "Someone in the building who knows your business, your people and your quirks. That is real and it matters. It is also one person, with one set of skills, who goes on holiday."),
        ("An outsourced team gives you coverage and depth", "A team does not resign, does not go on leave, and covers nights and weekends. You get a broader skill set than any one salary buys: security, networking, cloud and strategy from different specialists."),
        ("Co-managed gives you both", "If you already have an IT person, this is usually the right answer rather than replacing them. They keep the relationship with the business and stop being the single point of failure. They get out-of-hours cover and someone to escalate to."),
        ("Cost behaves differently", "A salary is a fixed commitment that rises with the market and carries redundancy risk. A per-user fee moves with headcount and can be stopped. Neither is automatically cheaper. They fail differently."),
    ],

    fit=[
        "You have between 10 and 150 staff, and the sweet spot for this question is 10 to 50.",
        "Nobody currently owns IT, or one person owns all of it and you know what that means.",
        "An IT failure costs you revenue rather than just inconvenience.",
        "You want the arithmetic done honestly, including the case for hiring.",
    ],

    faqs=[
        ("What does an IT manager cost in Ireland?",
         "The median is €90,000, with most between €80,000 and €99,375, according to roleup.ie as of November 2026. Dublin typically runs 10 to 25 per cent above Cork, Galway and Limerick. Most businesses of 10 to 50 people do not need that role: a system administrator at €40,000 to €55,000 for three to five years' experience is the realistic comparison, per the Hero IT Salary Guide 2026."),
        ("Is it cheaper to outsource IT than to hire?",
         "Usually, below about 80 staff, but compare honestly. Set the full cost of the hire against the fee: salary, employer PRSI of roughly 11 per cent, recruitment at 15 to 20 per cent of first-year salary, tooling, training and cover. That lands at roughly 1.3 to 1.5 times salary. Above roughly 80 to 100 staff the arithmetic starts to favour hiring, and above that it clearly does."),
        ("When should I hire an IT person instead of outsourcing?",
         "Three situations. When you are large enough to keep a good person genuinely busy, which is usually north of 80 staff. When technology is your product rather than your plumbing, so the knowledge has to be in-house. And when you have specialised systems that nobody outside the business will ever understand well enough. If none of those apply, you are usually buying presence rather than capability."),
        ("We have someone who 'does the IT' alongside their real job. Is that enough?",
         "It works until it does not, and it tends to fail in two ways. The person is doing two jobs badly and resents one of them. And the things that prevent incidents, patching, backup testing, access reviews, are exactly the tasks that get postponed when someone is busy with their actual role. It is not a competence problem. It is a time problem."),
        ("What happens if our one IT person leaves?",
         "Usually more than people expect. Passwords, supplier relationships, undocumented fixes and the reasoning behind past decisions all leave with them. Plan for it before it happens: insist on documentation, make sure credentials live somewhere the business controls, and know who you would call on day one."),
        ("Can we keep our IT person and still get help?",
         "Yes, and it is often the better answer. Co-managed means your person stays and stops being the only one who knows anything. They get cover for nights, weekends and leave, a second opinion on bigger decisions, and someone to escalate to. You stop carrying single-person risk without losing the person who knows your business."),
    ],

    related=['outsourced-it-cost', 'co-managed-it', 'fully-managed-it'],
    cta_h="Want the arithmetic run on your numbers?",
    cta_p="Twenty minutes, your staff count and what you spend now, and an honest answer on whether you should hire or outsource. If the answer is hire, that is what you will hear.",
),
]

PAGES.append(dict(
    kind='service', slug='outsourced-it-cost',
    service_name='What Outsourced IT Costs',
    card_kind='Decision guide', card_title='What Outsourced IT Costs',
    card_desc="How managed IT is priced, what moves the number, and what a fair quote looks like.",
    eyebrow='Decision guide',
    trail=[('Insights', '/insights'), ('What Outsourced IT Costs', '/outsourced-it-cost')],
    title="How Much Does Outsourced IT Cost? A Plain Answer",
    meta="How outsourced IT is priced, what moves the number up or down, what should be included, and how to compare two quotes that look nothing alike.",
    h1="How much does <em>outsourced IT</em> cost?",
    lead="Almost every provider answers this with \u201cit depends\u201d and then asks for a meeting. Here is what it actually depends on, so you can work out your own number before you talk to anyone.",
    glance=[('How it is priced', 'Per user, per month, almost universally'),
            ('What moves it', 'Servers, security depth, licensing, and how much is already in place'),
            ('What should be included', 'Tools and licensing, not billed separately on top'),
            ('What to watch', 'Onboarding fees, minimum terms, and out-of-scope charges')],
    problem_label='How the pricing actually works',
    problem_h="Per user, per month. The question is what that user price contains.",
    problem=[
        "Managed IT is sold per user, per month. That part is near-universal. What differs enormously between providers is what sits inside the number, and that is where two quotes that look like they are for the same thing turn out not to be.",
        "The honest drivers are straightforward. <strong>How many people</strong> you have, because the per-user price usually falls as headcount rises. <strong>Whether you run servers</strong>, since physical or virtual servers add real work that user counts do not capture. <strong>How much security</strong> you want: a basic protective baseline costs considerably less than round-the-clock monitored detection and response. <strong>Whether Microsoft licensing is included</strong> or billed separately, which alone can move a quote by a third. And <strong>what state things are in now</strong>, because an environment that has been neglected for five years takes work to stabilise before it becomes routine.",
        "What should not drive it is a long contract. A provider confident in the service does not need to lock you in for three years to deliver it.",
    ],
    included_h="What to check is included before you compare prices",
    included_intro="Two quotes are only comparable once you know these answers for both.",
    included=[
        ("Is licensing in or out?", "Microsoft 365 licensing is a significant cost. A quote that includes it and one that does not are not comparable, and the gap is often around a third."),
        ("Are the security tools included?", "Endpoint protection, email security, backup and monitoring should be in the per-user price. If a provider sells you a tool and then charges separately for anyone to watch it, you are buying software, not a service."),
        ("Is anyone actually watching?", "Detection without response is a dashboard. Ask who looks at alerts, when, and what they are empowered to do at 3am."),
        ("What is out of scope?", "Projects, migrations, hardware and on-site visits are often quoted separately. Fair enough, but you want to know before, not after."),
        ("Is there an onboarding fee?", "Some charge it, some fold it in. Neither is wrong. Not knowing is."),
        ("What is the term?", "Rolling monthly versus a twelve or thirty-six month commitment materially changes what you are agreeing to."),
    ],
    steps_h="How to work out your own number",
    steps=[
        ("Count users, not devices", "A person with a laptop and a phone is one user. This is the figure every quote keys off."),
        ("Count servers separately", "Physical or virtual, on site or hosted. These are priced on top of users almost everywhere."),
        ("Decide your security level", "Protective baseline, or monitored detection and response around the clock. This is the single biggest lever on the number."),
        ("Decide on licensing", "If you want Microsoft 365 bundled, say so when asking, so every quote is built the same way."),
    ],
    value_h="What a fair arrangement looks like",
    value_intro="Price is only half of it. These are the terms that tell you how confident a provider is.",
    value=[
        ("One number that includes the tools", "You should not be buying a service and then separately buying the things that make it work."),
        ("No lock-in", "Rolling monthly says the provider expects to keep earning it. Annual terms are reasonable if they come with a discount and you choose them."),
        ("Clear scope boundaries", "What is included and what is a project, agreed in advance and in writing."),
        ("Reporting you can read", "A monthly account of what happened and what it meant, not a dashboard you have to interpret."),
    ],
    fit=["You are comparing quotes and they do not look comparable.",
         "You want to know the drivers before you sit in a sales meeting.",
         "You have roughly 10 to 150 people.",
         "You would rather a predictable monthly number than a surprise."],
    faqs=[
        ("How much does outsourced IT cost per user per month?",
         "It is priced per user, per month, and the range is wide because what sits inside the number varies so much. The honest drivers are headcount, whether you run servers, how deep the security goes, whether Microsoft licensing is bundled, and the state of the environment today. Anyone quoting a precise figure without knowing those is guessing, and anyone refusing to explain the drivers is stalling."),
        ("Why will nobody publish a price?",
         "Partly because the drivers genuinely vary, and partly because a meeting is easier to sell than a number. The drivers are not a secret, which is why they are set out on this page. You should be able to narrow your own range before speaking to anyone."),
        ("Is Microsoft 365 licensing usually included?",
         "Sometimes, and it matters enormously. Licensing is a large component, so a quote that bundles it will look much higher than one that does not for identical service. Ask every provider to quote the same way or you are comparing nothing."),
        ("Should I pay an onboarding fee?",
         "It is reasonable. Taking over an environment properly, documenting it and fixing what is wrong is real work. What is not reasonable is discovering it after you have agreed the monthly figure."),
        ("What should I avoid?",
         "Three things. A long lock-in with no discount attached. Security tools sold without anybody monitoring them. And a quote so much cheaper than the others that something has clearly been left out, which is usually the monitoring or the licensing."),
        ("What does Dividend IT charge?",
         "Per user, per month, with tools included and contracts rolling monthly. The number depends on the drivers above. Twenty minutes and a look at what you have gives you a real figure rather than a range, and if we are not the right fit we will say so."),
    ],
    related=['outsourced-it', 'do-i-need-an-it-manager', 'cost-calculator'],
    cta_h="Want a real number rather than a range?",
    cta_p="Twenty minutes, your headcount and what you have now, and you will get an honest figure. If we are not the right fit, you will hear that too.",
))
