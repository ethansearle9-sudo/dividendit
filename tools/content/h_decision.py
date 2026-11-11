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

    related=['outsourced-it', 'co-managed-it', 'fully-managed-it'],
    cta_h="Want the arithmetic run on your numbers?",
    cta_p="Twenty minutes, your staff count and what you spend now, and an honest answer on whether you should hire or outsource. If the answer is hire, that is what you will hear.",
),
]
