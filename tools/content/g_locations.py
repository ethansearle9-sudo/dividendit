"""Location pages.

One page per city we genuinely want to rank in. These are NOT templated
doorway pages: each one has to say something true and specific about doing
business in that place, or it should not exist. If a city page could have
its name swapped for another city and still read correctly, it is thin and
Google will treat it as such.

The differentiator for each city is the local labour market and the local
business mix, because that is what actually changes the argument for
outsourcing IT in one place versus another.
"""

PARENT = ('Where We Work', '/outsourced-it')


def loc(slug, city, country, **kw):
    d = dict(kind='location', slug=slug, city=city, country=country,
             service_name=f'Outsourced IT and Cyber Security in {city}',
             card_kind='Location', card_title=f'{city} IT Support',
             eyebrow='Where We Work', trail=[PARENT, (city, '/' + slug)])
    d.update(kw)
    return d


PAGES = [
loc('it-support-dublin', 'Dublin', 'Ireland',
    title="IT Support Dublin: Outsourced IT and Cyber Security",
    meta="Outsourced IT support and cyber security for Dublin businesses of 10 to 150 people, for owners who cannot outbid the multinationals for IT staff.",
    card_desc="Outsourced IT and security for Dublin businesses of 10 to 150 people.",
    h1="IT support in <em>Dublin</em>",
    lead="Dublin is the hardest city in Ireland to hire an IT person into a small business, and it has very little to do with your salary band. Outsourcing is not the cheap option here. It is the only one that holds.",

    glance=[('Who we work with', 'Dublin businesses of roughly 10 to 150 people'),
            ('Where', 'City centre, the IFSC, Sandyford, Citywest, Park West and the M50 corridor'),
            ('Common sectors', 'Distribution, manufacturing, financial services, professional services'),
            ('How it works', 'Remote-first support, on site in Dublin when the problem needs hands')],

    problem_label='The Dublin problem',
    problem_h="You are not competing for IT staff with other small businesses. You are competing with Google.",
    problem=[
        "Dublin has an unusual labour market for a city its size. The multinationals cluster here, and they set the price for technical people. A capable systems administrator who would be a strong hire for a 60-person distributor is also a candidate Amazon, Meta or one of the funds in the IFSC will look at, with a package a business like yours cannot sensibly match.",
        "So one of three things tends to happen. You do not fill the role. You fill it, and lose them inside eighteen months to someone paying forty per cent more. Or you fill it with someone more junior than the job really needs, and quietly carry the risk of that for years.",
        "None of those is a failure of management. It is arithmetic. A business of your size cannot win a bidding war against companies whose IT budget is larger than your revenue, and it should not have to in order to have IT that works.",
        "The way out is not to hire harder. It is to stop needing the hire. <strong>A team you share costs less than the person you cannot keep</strong>, and it does not resign.",
    ],

    included_h="What a Dublin business actually gets",
    included_intro="The same programme we run everywhere, with the parts that matter locally called out honestly.",
    included=[
        ("People who do not resign", "You get a team rather than a person. Nobody hands in their notice, nobody takes the knowledge of your systems with them, and nobody is on annual leave the week everything breaks."),
        ("On site when it is warranted", "Most problems are solved remotely and faster that way. When something genuinely needs hands on hardware, we come to you. We cover the city and the M50 corridor, including Sandyford, Citywest, Park West and Blanchardstown."),
        ("Security sized for a real target", "Dublin businesses sit in the supply chains of much larger companies, and that makes them worth attacking. Invoice fraud and mailbox takeover are the two that actually happen, far more often than ransomware."),
        ("Answers for the people who audit you", "If you sell into financial services or supply a multinational, somebody will eventually send you a security questionnaire. We keep the evidence that answers it, so it does not become a fire drill."),
        ("Microsoft 365 run properly", "Almost every Dublin SME runs on Microsoft 365, and almost none of it is configured the way Microsoft intends. That gap is where most incidents start."),
        ("One bill, no lock-in", "Per user, per month, tools included. Contracts roll monthly. If we stop being worth it, you leave."),
    ],

    steps_h="How we start with a Dublin business",
    steps=[
        ("We look before we talk", "A short review of what you actually have: devices, sign-ins, backups, where the risk sits. You get the findings whether or not you work with us."),
        ("We fix the security basics first", "Multi-factor sign-in, device protection, a backup that has been tested by restoring from it. In place within two weeks."),
        ("We take over the day to day", "Support, patching, monitoring and the vendor chasing. Fully onboarded within 30 days."),
        ("We report in plain English", "Every month: what happened, what it cost, what it prevented, what to do next. No dashboard you have to interpret yourself."),
    ],

    value_h="Why this is worth more than the money it saves",
    value_intro="The saving against a salary is real, but it is the smaller half of the argument.",
    value=[
        ("The cost is predictable and it stops moving", "A salary plus employer PRSI plus recruitment plus tooling plus cover is not a predictable number. A per-user fee is."),
        ("The knowledge stays with the business", "When your one IT person leaves, so does everything they knew and never wrote down. A team documents because it has to."),
        ("Risk stops being one person's memory", "Patching, backups and access reviews happen because they are scheduled, not because somebody remembered."),
        ("It reads properly in due diligence", "If you ever sell, a buyer will look at how technology is run. Documented and outsourced to an accountable provider is a better answer than one trusted individual."),
    ],

    fit=[
        "You are a Dublin business of roughly 10 to 150 people.",
        "You either have no IT person, or you have one and know the risk of that.",
        "You would rather a predictable monthly cost than a hiring problem that recurs every eighteen months.",
        "You want the owner's view of technology, not a ticket queue.",
    ],

    faqs=[
        ("Do you actually come on site in Dublin, or is it all remote?",
         "Both, and in that order. Most issues are resolved remotely and considerably faster that way. When a problem needs someone physically present, we come to you. We cover Dublin city, the IFSC, and the M50 corridor including Sandyford, Citywest, Park West and Blanchardstown."),
        ("Is outsourcing really cheaper than hiring someone in Dublin?",
         "Usually, but compare it honestly. Set the full cost of the hire against the fee: salary, employer PRSI, recruitment, tooling, training, and cover for leave and illness. The sharper point is that the comparison assumes you can hire and keep the person at all, which in Dublin is the part that tends to fail."),
        ("We already have an IT person. Is this still relevant?",
         "Yes, and it is often a better fit. Co-managed means your person keeps the relationship with the business and stops being the only one who knows anything. They get out-of-hours cover, a second opinion and someone to escalate to, and you stop carrying single-person risk."),
        ("Are Dublin SMEs really a target for cyber attacks?",
         "Yes, and usually not for the reason owners expect. You are rarely attacked because of who you are. You are attacked because you are in the supply chain of someone larger, or simply because an automated scan found an opening. Invoice fraud and mailbox takeover are far more common than the ransomware that makes the news."),
        ("Do you work with businesses outside Dublin?",
         "Yes. We work across Ireland, and in the UK and South Africa. Dublin has its own page because the hiring market here changes the argument, not because it is the only place we work."),
        ("What does it cost?",
         "It is priced per user, per month, with tools included, and it depends on how many people you have and how much is already in place. The honest answer needs twenty minutes and a look at what you have. Contracts roll monthly, so there is no lock-in either way."),
    ],

    related=['outsourced-it', 'outsourced-cyber', 'fully-managed-it'],
    cta_h="Twenty minutes on your IT, no pitch",
    cta_p="An honest read on whether your technology is building value or quietly costing you. If the answer is that you are fine, we will tell you that.",
),
]
