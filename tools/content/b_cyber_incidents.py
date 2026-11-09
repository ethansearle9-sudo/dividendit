PAGES = [
dict(
    kind='article', slug='been-hacked-first-24-hours',
    title='Been Hacked? What to Do in the First 24 Hours | Dividend IT',
    og_title='Think your business has been hacked? The first 24 hours',
    meta='A calm, step-by-step plan for business owners who think they have been hacked: what to do in the first hour, who to call, what to report and what not to do.',
    card_kind='Incident guide', card_title='Been Hacked? What to Do in the First 24 Hours',
    card_desc='A calm, hour-by-hour plan for owners who think something is wrong.',
    trail=[('Insights', '/insights'), ('Been hacked? The first 24 hours', '/been-hacked-first-24-hours')],
    eyebrow='Incident guide', read=9,
    h1='We think we\'ve been hacked. <em>What do we do in the first 24 hours?</em>',
    sub='A plain-English plan for the owner or director who has just had that sinking feeling. Follow it in order. Most of the damage in a cyber incident is done by panic, delay and well-meant mistakes in the first few hours, not by the attacker.',
    urgent='<strong>If it is happening right now</strong><ol><li>If money has left the account, call your bank\'s fraud line immediately. Minutes matter.</li><li>Unplug affected computers from the network or switch off their WiFi, but leave them powered on.</li><li>Call your IT or security provider. Then come back to this page.</li></ol>',
    sections=[
        ('dont', 'First: three things not to do', '''
<p>Before you do anything, avoid the three mistakes that make incidents worse.</p>
<ul>
<li><strong>Do not switch everything off or wipe machines.</strong> It feels like the safe move, but it destroys the evidence that tells you how they got in and what they took. Disconnect from the network instead.</li>
<li><strong>Do not use the system you think is compromised to talk about the incident.</strong> If a mailbox has been taken over, the attacker may be reading your emails about them. Use phones and a separate messaging app.</li>
<li><strong>Do not pay anyone or agree to anything yet.</strong> Not a ransom, not a "recovery specialist" who contacts you out of the blue. You do not have enough information to make that decision.</li>
</ul>
'''),
        ('hour-1', 'The first hour: contain it', '''
<p>The goal of the first hour is simple: stop it getting worse.</p>
<ol class="tl">
<li><span class="t">Money</span><strong>Call your bank if any payment might be affected.</strong> Ask for the fraud team, explain that a payment may have gone to a criminal account and ask them to attempt a recall. The faster the bank acts, the better the chance of getting money back.</li>
<li><span class="t">Machines</span><strong>Isolate affected devices.</strong> Unplug the network cable or turn off WiFi on any computer that is behaving strangely or showing a ransom message. Leave it switched on.</li>
<li><span class="t">Accounts</span><strong>Lock compromised accounts.</strong> From a device you trust, reset the password of any account you think has been taken over, sign it out of all sessions, and check that the multi-factor sign-in method has not been changed to the attacker's phone.</li>
<li><span class="t">People</span><strong>Call your IT or security provider.</strong> Tell them what you saw, when, and what you have already done. If you do not have one, call your insurer's incident line first, because many policies provide responders.</li>
</ol>
<div class="note"><p>Write down the time and what you see as you go: screenshots of ransom notes, the email that looked wrong, the account that was locked. A simple timeline is one of the most valuable things you can hand to responders, insurers and, if needed, the police.</p></div>
'''),
        ('hours-1-4', 'Hours one to four: get the right people involved', '''
<p>Once the bleeding has stopped, put a small team around the problem.</p>
<ul>
<li><strong>One person in charge.</strong> Usually the owner or a director. They make the calls, approve spending and decide what to say to whom.</li>
<li><strong>Your technical responders.</strong> Your IT partner or an incident response firm. If you have cyber insurance, check whether the policy requires you to use their approved responders. Using someone else can affect your cover.</li>
<li><strong>Your insurer.</strong> Most cyber policies require prompt notice. Call the incident line on the policy, not just your broker.</li>
<li><strong>Legal advice if personal data may be involved.</strong> Your insurer can often arrange this. It helps you get notifications right first time.</li>
</ul>
<p>Agree how the team will communicate. A phone call at set times and a messaging group outside your normal systems works well.</p>
'''),
        ('hours-4-12', 'Hours four to twelve: understand what happened', '''
<p>Now the responders work out the scope. As the owner, you need answers to four questions, in plain English:</p>
<ol>
<li><strong>How did they get in?</strong> A phished password, an unpatched system, a supplier's access?</li>
<li><strong>What could they reach?</strong> One mailbox, the file server, the finance system, everything?</li>
<li><strong>What did they take or change?</strong> Data copied out, inbox rules created, bank details altered, backups deleted?</li>
<li><strong>Are they still in?</strong> And how will we know when they are gone?</li>
</ol>
<p><strong>Do not restore from backup until you know how they got in.</strong> If you restore systems with the same weakness still open, they will simply come back. This is the most common reason businesses get hit twice.</p>
'''),
        ('hours-12-24', 'Hours twelve to twenty-four: notify and communicate', '''
<p>By the end of the first day you will need to decide who must be told. Take advice, but know the broad rules.</p>
<h3>Regulators</h3>
<p>If personal data may have been exposed, data protection law usually applies. Under GDPR in the EU and the UK, a reportable breach must be notified to the regulator <strong>within 72 hours of becoming aware of it</strong>, unless it is unlikely to result in a risk to people. In South Africa, POPIA requires notification to the Information Regulator and affected people as soon as reasonably possible. The clock starts when you know, not when you finish investigating, so start early and update later.</p>
<h3>Police and national cyber authorities</h3>
<p>Report fraud and cyber crime to the police and, where one exists, your national cyber security centre. It helps them, and your bank and insurer will often ask for a reference number.</p>
<h3>Customers and suppliers</h3>
<p>If your email was taken over, the attacker may have sent fake invoices or bank details to people you do business with. Call your key customers and suppliers, by phone, and tell them not to act on any payment change that appears to come from you.</p>
<h3>Your team</h3>
<p>Tell staff what has happened, what to do and what not to do, and who to send questions to. Silence breeds rumours and mistakes.</p>
'''),
        ('ransom', 'If there is a ransom demand', '''
<p>Ransomware groups want you to feel you have no choice. You usually have more options than they let you believe.</p>
<ul>
<li>Do not contact the criminals yourself. If negotiation is ever considered, it is done by specialists, with legal advice.</li>
<li>Paying does not guarantee you get your data back, or that copies are deleted. It also marks you as a business that pays.</li>
<li>Paying certain groups can breach sanctions law. That is a legal question, not a technical one.</li>
<li>If your backups are separate from your main systems and recently tested, you may be able to recover without engaging at all. This is exactly why we treat <a href="/backup-dr">backup and recovery</a> as a security control, not an IT chore.</li>
</ul>
'''),
        ('after', 'After the first day: recover properly', '''
<p>Recovery is where good businesses separate themselves. Restore cleanly, from known-good backups, onto systems with the original weakness fixed. Then make the changes that stop it happening again, typically stronger sign-in protection, monitoring that someone actually watches, and a tested plan.</p>
<p>Finally, hold a short, blame-free review. What did we see, what did we do, what would we do differently? Write it down. If you are ever selling the business, a buyer will ask about past incidents. "Here is what happened, here is what we changed, here is the evidence" is a strong answer.</p>
'''),
        ('checklist', 'The one-page checklist', '''
<p>Print this and keep it somewhere you can find it when your systems are down.</p>
<ul class="check">
<li>Bank fraud line number: ______________________</li>
<li>IT or security provider out-of-hours number: ______________________</li>
<li>Cyber insurer incident line and policy number: ______________________</li>
<li>Who is in charge if the owner is away: ______________________</li>
<li>Disconnect affected devices; leave them powered on</li>
<li>Reset compromised accounts from a trusted device; check sign-in methods</li>
<li>Keep a timeline with times and screenshots</li>
<li>Do not restore until you know how they got in</li>
<li>Personal data involved? Take advice; 72-hour regulator clock under GDPR</li>
<li>Phone key customers and suppliers about any payment changes</li>
</ul>
'''),
    ],
    howto=dict(name='What to do in the first 24 hours after a suspected cyber attack', steps=[
        ('Contain', 'Call your bank if money may be affected, disconnect affected devices from the network without switching them off, lock compromised accounts from a trusted device, and call your IT or security provider.'),
        ('Mobilise', 'Put one person in charge, involve technical responders, notify your cyber insurer and take legal advice if personal data may be involved.'),
        ('Investigate', 'Establish how the attackers got in, what they could reach, what they took or changed, and whether they are still present. Do not restore from backup until the entry point is closed.'),
        ('Notify', 'Notify regulators where required (within 72 hours under GDPR), report to police, and phone customers and suppliers about any payment changes.'),
        ('Recover', 'Restore cleanly from known-good backups with the weakness fixed, then hold a blame-free review and record what changed.')]),
    faqs=[
        ('Should I turn off a computer I think has been hacked?', 'No. Disconnect it from the network by unplugging the cable or turning off WiFi, but leave it powered on. Switching it off can destroy evidence responders need to understand what happened.'),
        ('Should we pay a ransom?', 'Not without specialist and legal advice. Payment does not guarantee recovery, may breach sanctions law depending on who is behind the attack, and marks you as a business that pays. Tested backups are what give you a real alternative.'),
        ('Do we have to report a cyber attack?', 'If personal data may have been exposed, data protection law usually requires you to notify the regulator. Under GDPR that is within 72 hours of becoming aware, unless the breach is unlikely to put people at risk. In-scope businesses under the EU NIS2 Directive have their own, shorter reporting deadlines. Take advice early.'),
        ('Can the bank get our money back?', 'Sometimes, if you act fast. Banks can attempt to recall a payment or freeze funds at the receiving bank, but once money has been moved on, recovery becomes much harder. Call the fraud line the moment you suspect a problem.'),
        ('Will our cyber insurance cover it?', 'It depends on the policy and on following its conditions, which often include notifying the insurer promptly and using its approved responders. Call the incident line on the policy as early as possible.'),
    ],
    related=['signs-your-business-has-been-hacked', 'invoice-fraud', 'detection-response', 'backup-dr', 'cyber-insurance', 'outsourced-cyber'],
    cta_h='Want a plan in place before you need it?',
    cta_p='We will help you write a one-page incident plan, check your backups actually restore and make sure someone is watching when it matters. Twenty minutes to start.',
    cta_secondary=('See detection and response', '/detection-response'),
),
dict(
    kind='article', slug='signs-your-business-has-been-hacked',
    title='How to Tell If Your Business Has Been Hacked | Dividend IT',
    og_title='How to tell if your business has been hacked: 12 warning signs',
    meta='How do you know if your computer systems have been compromised? Twelve warning signs in email, devices, money and accounts, and a 15-minute check any owner can run.',
    card_kind='Incident guide', card_title='How to Tell If Your Business Has Been Hacked',
    card_desc='Twelve warning signs and a 15-minute check you can run today.',
    trail=[('Insights', '/insights'), ('Signs your business has been hacked', '/signs-your-business-has-been-hacked')],
    eyebrow='Incident guide', read=8,
    h1='How to tell if your business <em>has been hacked</em>',
    sub='Most businesses do not find out they have been compromised from a ransom note. They find out weeks later, from a supplier asking why they have not been paid. These are the warning signs that show up earlier, and how to check for them.',
    sections=[
        ('quiet', 'Why compromise is usually quiet', '''
<p>Modern attackers rarely announce themselves. If they get into a mailbox, the valuable thing is not to break it but to watch it: who pays whom, when, and how. If they get into a network, they spend time finding the backups and the most important data before doing anything visible.</p>
<p>That means the question "how do I know if our systems have been compromised?" is really "what small signs do attackers leave while they are watching?" Here are the twelve we see most.</p>
'''),
        ('email', 'Signs in email', '''
<ol>
<li><strong>Inbox rules nobody created.</strong> Rules that move emails containing words like "invoice", "payment" or "bank" to an obscure folder, or forward copies to an outside address. This is the most reliable sign of mailbox takeover.</li>
<li><strong>Sent emails nobody remembers sending,</strong> or replies to conversations the mailbox owner has never seen.</li>
<li><strong>Multi-factor sign-in prompts nobody asked for.</strong> If someone receives approval requests out of the blue, their password is probably already known.</li>
<li><strong>Password reset or "new sign-in" alerts</strong> from Microsoft, Google, banks or other services that the person did not trigger.</li>
</ol>
'''),
        ('devices', 'Signs on computers and servers', '''
<ol start="5">
<li><strong>Security software switched off or uninstalled.</strong> Attackers disable protection before they act. It should never switch itself off.</li>
<li><strong>New programs, especially remote access tools,</strong> that nobody installed. Legitimate remote support software is a favourite way for attackers to keep access.</li>
<li><strong>Files that will not open or have strange new extensions.</strong> This can be the start of ransomware encrypting data.</li>
<li><strong>Unusual activity at odd hours:</strong> servers busy at 3am, large amounts of data leaving the network, a machine that is suddenly slow with its fan running hard.</li>
</ol>
'''),
        ('money', 'Signs in money and accounts', '''
<ol start="9">
<li><strong>A supplier says they have not been paid</strong> for an invoice you paid. Check where the money went before anything else.</li>
<li><strong>Customers say they received new bank details from you.</strong> If you did not send them, your mailbox or your domain is being used against you.</li>
<li><strong>New user accounts, especially administrators,</strong> or existing accounts given more access than before.</li>
<li><strong>Sign-ins from unexpected countries or at impossible times,</strong> such as the same user in Dublin and Lagos within an hour.</li>
</ol>
'''),
        ('check', 'A 15-minute check any owner can run', '''
<p>If you use Microsoft 365, you or your IT provider can check the most important signs today. Google Workspace has equivalents.</p>
<ul class="check">
<li><strong>Inbox rules:</strong> in Outlook, open Settings, then Mail, then Rules, for directors and anyone in finance. Anything you do not recognise is a red flag.</li>
<li><strong>Forwarding:</strong> in the same settings, check that email is not being forwarded to an outside address.</li>
<li><strong>Sign-in methods:</strong> at mysignins.microsoft.com, check the phone numbers and authenticator apps registered against each finance and director account.</li>
<li><strong>Recent sign-ins:</strong> the same page shows recent sign-in locations. Look for countries you do not operate in.</li>
<li><strong>Admin accounts:</strong> ask your IT provider for a list of everyone with administrator access, and question every name.</li>
</ul>
<div class="note"><p><strong>Found something?</strong> Do not delete it yet. Take screenshots, then follow <a href="/been-hacked-first-24-hours">what to do in the first 24 hours</a>.</p></div>
'''),
        ('watching', 'Why someone needs to be watching', '''
<p>Every one of these twelve signs shows up in logs and alerts long before a supplier calls about a missing payment. The problem in most smaller businesses is not that the warning is missing, it is that nobody is looking at it, especially outside office hours.</p>
<p>That is the job of <a href="/detection-response">detection and response</a>: tooling that collects the signals from email, devices and accounts, and people who look at the alerts around the clock and act within minutes. It is the difference between finding out in an hour and finding out in a month.</p>
'''),
    ],
    faqs=[
        ('How do I know if my computer system has been compromised?', 'Look for security software being disabled, programs nobody installed, files that will not open, unusual activity at odd hours, and in email, inbox rules or forwarding nobody set up. Any one of these deserves an immediate check by your IT or security provider.'),
        ('What is the most common sign of a hacked business email account?', 'An inbox rule that hides or forwards messages about invoices or payments. Attackers create them so they can watch payment conversations without the account owner noticing replies.'),
        ('Can a business be hacked without anyone noticing?', 'Yes, and it is common. Attackers often stay hidden for days or weeks to learn how the business pays suppliers or where its data and backups are. Continuous monitoring is what shortens that window.'),
        ('Who should I call if I find signs of a hack?', 'Your IT or security provider first, and your bank immediately if any payment could be affected. If you have cyber insurance, call the incident line on the policy as well.'),
    ],
    related=['been-hacked-first-24-hours', 'invoice-fraud', 'email-interception-man-in-the-middle', 'detection-response', 'iam', 'outsourced-cyber'],
    cta_h='Not sure what you would find?',
    cta_p='We can run these checks with you, across every mailbox and device, and tell you plainly what we see. Twenty minutes to agree the scope.',
    cta_secondary=('See a cyber risk assessment', '/cyber-risk-assessment'),
),
dict(
    kind='article', slug='invoice-fraud',
    title='Invoice Fraud: How It Works and How to Stop It | Dividend IT',
    og_title='Invoice fraud and payment diversion: how it works and how to stop it',
    meta='Invoice fraud and business email compromise explained for owners: how criminals redirect supplier payments, why it works and the controls that stop it.',
    card_kind='Fraud guide', card_title='Invoice Fraud and Payment Diversion',
    card_desc='How criminals redirect supplier payments, and the controls that stop it.',
    trail=[('Insights', '/insights'), ('Invoice fraud', '/invoice-fraud')],
    eyebrow='Fraud guide', read=10,
    h1='Invoice fraud and payment diversion: <em>how it works and how to stop it</em>',
    sub='The most expensive cyber incident most smaller businesses will ever face is not ransomware. It is a real invoice, paid on time, into the wrong bank account. Here is exactly how it happens, why good people fall for it, and the handful of controls that stop it.',
    sections=[
        ('what', 'What invoice fraud is', '''
<p>Invoice fraud, also called payment diversion, mandate fraud or business email compromise, is when a criminal persuades a business to send a legitimate payment to an account they control. There is usually no malware involved and nothing to see on your computers. The attack is on your process, through email.</p>
<p>It is also enormous. The FBI's Internet Crime Complaint Center recorded <strong>$2.77 billion in reported losses to business email compromise in 2024</strong>, from more than 21,000 complaints, and those are only the cases that were reported.</p>
'''),
        ('how', 'How a typical attack unfolds', '''
<ol class="tl">
<li><span class="t">Week 1</span><strong>A password is stolen.</strong> Someone in your business, or at a supplier, enters their email password on a convincing fake login page.</li>
<li><span class="t">Weeks 1 to 4</span><strong>The attacker watches.</strong> They read the mailbox quietly, learn who pays whom, how invoices look, who approves payments and when large amounts are due. They often create an inbox rule to hide replies.</li>
<li><span class="t">The moment</span><strong>The request arrives.</strong> Just before a large payment is due, an email arrives in the real thread, from the real address or a near-identical one: "Please note our bank details have changed. Updated letterhead attached."</li>
<li><span class="t">Payment</span><strong>The money goes.</strong> The invoice is genuine, the amount is expected, the timing is right. Finance updates the details and pays.</li>
<li><span class="t">Weeks later</span><strong>The supplier chases.</strong> They have not been paid. By now the money has been moved through several accounts and is very hard to recover.</li>
</ol>
'''),
        ('why', 'Why it works on smart people', '''
<p>Owners often assume their team would never fall for it. The people who get caught are usually careful, conscientious and busy. The attack works because it removes every normal warning sign:</p>
<ul>
<li>The email sits in a real conversation with a real supplier.</li>
<li>The invoice is genuine and the amount is expected.</li>
<li>The timing matches when payment is due.</li>
<li>There is often gentle pressure: a director copied in, or a reminder that the account will be on hold.</li>
</ul>
<p>That is why the answer is not "tell people to be careful". It is a process that does not rely on anyone spotting the fake.</p>
'''),
        ('variants', 'Three versions to watch for', '''
<h3>Supplier impersonation</h3>
<p>The attacker poses as a supplier and asks you to pay a new account. Their mailbox may be the compromised one, not yours, which is why your own security alone cannot stop it.</p>
<h3>Director impersonation</h3>
<p>An urgent email appears to come from the owner or finance director asking for a quick payment, a transfer to a new supplier or gift cards. It often arrives when the director is known to be travelling.</p>
<h3>Your customers get targeted in your name</h3>
<p>If your mailbox is compromised, the attacker can send your customers fake bank details from your real address. They pay the criminal, you are not paid, and the conversation about who is responsible is very uncomfortable.</p>
'''),
        ('stop', 'The controls that stop it', '''
<h3>Process controls (the ones that matter most)</h3>
<ul class="check">
<li><strong>Call-back verification.</strong> Any new payee or change of bank details is confirmed by phone, on a number taken from your own records, not from the email. No exceptions, regardless of who asks.</li>
<li><strong>Two people for new payees and changed details.</strong> One person sets them up, a second approves.</li>
<li><strong>Payee name checks.</strong> Use your bank's account name verification where available, such as Confirmation of Payee in the UK and Verification of Payee in the eurozone, and treat a mismatch as a stop sign.</li>
<li><strong>A no-blame culture for pausing payments.</strong> Staff must know they will never be criticised for delaying a payment to check it.</li>
<li><strong>Tell your customers how you will never contact them.</strong> A line on every invoice: "We will never change our bank details by email."</li>
</ul>
<h3>Technical controls</h3>
<ul>
<li><strong>Multi-factor sign-in</strong> on every mailbox, so a stolen password is not enough. See <a href="/iam">identity and access management</a>.</li>
<li><strong>Alerts on suspicious inbox rules and forwarding,</strong> watched by someone who acts on them.</li>
<li><strong>Email authentication (SPF, DKIM and DMARC)</strong> set to enforce, so criminals cannot send email that appears to come from your exact domain.</li>
<li><strong>Lookalike domain detection and external sender warnings,</strong> so an email from "dividend-it.co" instead of "dividendit.com" stands out.</li>
</ul>
'''),
        ('paid', 'If you have already paid', '''
<ol>
<li><strong>Call your bank's fraud line now.</strong> Ask them to recall the payment and contact the receiving bank. Hours matter.</li>
<li><strong>Report it to the police</strong> and get a reference number.</li>
<li><strong>Check whose mailbox was compromised.</strong> Yours, the supplier's, or both. Look for inbox rules and recent sign-ins.</li>
<li><strong>Phone the genuine supplier or customer</strong> so they know what happened and can check their own systems.</li>
<li><strong>Tell your insurer.</strong> Some cyber and crime policies cover this kind of loss, often with a separate limit.</li>
</ol>
<p>Then follow the wider plan in <a href="/been-hacked-first-24-hours">what to do in the first 24 hours</a>.</p>
'''),
    ],
    faqs=[
        ('What is business email compromise?', 'Business email compromise is fraud where criminals use a hacked or impersonated email account to trick a business into sending money or sensitive information. Invoice fraud and payment diversion are the most common forms.'),
        ('How do I know if an email asking to change bank details is fraudulent?', 'Assume any request to change bank details could be fraudulent, however genuine it looks. Confirm it by phone on a number you already had before the email arrived. If the email discourages you from calling, treat that as a red flag.'),
        ('Can the bank recover money lost to invoice fraud?', 'Sometimes, if the fraud is reported quickly. Banks can try to recall the payment or freeze funds at the receiving bank, but once the money has been moved on, recovery is unlikely. Speed is everything.'),
        ('Does cyber insurance cover invoice fraud?', 'Some policies do, often under a social engineering or funds transfer fraud section with a lower limit than the main policy. Many do not cover it by default. Check your wording with your broker.'),
    ],
    sources=['FBI Internet Crime Complaint Center, 2024 Internet Crime Report, as summarised by <a href="https://www.nacha.org/news/fbis-ic3-finds-almost-85-billion-lost-business-email-compromise-last-three-years" target="_blank" rel="noopener">Nacha</a> and <a href="https://www.proofpoint.com/us/blog/email-and-cloud-threats/email-attacks-drive-record-cybercrime-losses-2024" target="_blank" rel="noopener">Proofpoint</a>.'],
    related=['email-interception-man-in-the-middle', 'how-to-spot-a-phishing-email', 'been-hacked-first-24-hours', 'iam', 'endpoint-security', 'cyber-insurance'],
    cta_h='Close the gap before the next big payment run.',
    cta_p='We will check your mailboxes for warning signs, set up the technical controls and help you put a simple payment verification process in place. Twenty minutes to start.',
),
dict(
    kind='article', slug='how-to-spot-a-phishing-email',
    title='How to Spot a Phishing Email: A Business Guide | Dividend IT',
    og_title='How to spot a phishing email: a practical guide for business teams',
    meta='How to spot a phishing email and know if an email is fraudulent: a ten-second check for staff, real examples businesses receive, and what to do if someone clicks.',
    card_kind='Staff guide', card_title='How to Spot a Phishing Email',
    card_desc='A ten-second check your team can use on every email that asks for something.',
    trail=[('Insights', '/insights'), ('How to spot a phishing email', '/how-to-spot-a-phishing-email')],
    eyebrow='Staff guide', read=8,
    h1='How to spot a phishing email: <em>a guide for business teams</em>',
    sub='Phishing is the most common way into a business. It no longer looks like a badly spelled message from a prince. It looks like a shared document, a password expiry notice or an invoice from a supplier you use. Here is a ten-second check your team can use on every email that asks for something.',
    sections=[
        ('changed', 'Phishing has changed', '''
<p>The old advice was to look for spelling mistakes. That no longer works. Criminals use the same tools as everyone else to write clean, natural, well-formatted emails, often in your own industry's language.</p>
<p>Most phishing aimed at businesses today has one goal: to get someone to <strong>type their email password into a fake login page</strong>. Once they have it, they have the mailbox, and from there they can commit <a href="/invoice-fraud">invoice fraud</a> or move deeper into your systems. Many phishing emails have no attachment and nothing a virus scanner would catch. Just a link.</p>
'''),
        ('ten-seconds', 'The ten-second check', '''
<p>Before acting on any email that asks you to click, log in, pay, or open something, run through five questions.</p>
<ol>
<li><strong>Was I expecting this?</strong> An unexpected document, invoice, voicemail or delivery notice is the most common bait.</li>
<li><strong>Who really sent it?</strong> Look at the actual email address, not the display name. "Microsoft 365" can be sent from anything.</li>
<li><strong>Is it pushing me to act fast?</strong> Urgency, deadlines, account suspension and "the CEO needs this now" are pressure tactics.</li>
<li><strong>Where does the link actually go?</strong> Hover over it on a computer, or press and hold on a phone. If the web address is not the organisation it claims to be, stop.</li>
<li><strong>Is it asking me to log in, pay, or change payment details?</strong> These three requests deserve a second channel: open the website yourself, or phone the person on a number you already have.</li>
</ol>
<div class="note"><p><strong>The golden rule:</strong> never log in from a link in an email. Go to the site or app the way you normally would. If the request is real, it will be there.</p></div>
'''),
        ('examples', 'What phishing emails look like now', '''
<h3>The password expiry notice</h3>
<p>"Your Microsoft 365 password expires today. Keep your current password." The button leads to a perfect copy of the Microsoft login page.</p>
<h3>The shared document</h3>
<p>"A file has been shared with you: Q3 Remittance.pdf". It may genuinely come from a supplier's real account, because their mailbox was compromised first. The link asks you to sign in to view it.</p>
<h3>The invoice or payment change</h3>
<p>A real-looking invoice, or a note that bank details have changed. Covered in detail in our <a href="/invoice-fraud">invoice fraud guide</a>.</p>
<h3>The director request</h3>
<p>"Are you at your desk? I need a quick favour." Followed by a request for gift cards or an urgent transfer, usually when the director is known to be away.</p>
<h3>The QR code</h3>
<p>An email or PDF with a QR code to "verify your account" or "view your payslip". Scanning moves you to your phone, where links are harder to inspect and company protections may not apply.</p>
<h3>The fake multi-factor request</h3>
<p>A run of sign-in approval prompts on your phone you did not trigger, sometimes followed by a call from "IT support" asking you to approve one. Never approve a sign-in you did not start.</p>
'''),
        ('clicked', 'What to do if someone clicks', '''
<p>The worst outcome is someone who clicks, realises, and says nothing because they are embarrassed. Make it easy and blame-free to speak up.</p>
<ol>
<li><strong>Tell IT straight away,</strong> even if nothing seemed to happen.</li>
<li><strong>If a password was entered, change it immediately</strong> from a trusted device, and sign the account out everywhere.</li>
<li><strong>Check the account's sign-in methods and inbox rules</strong> for anything new.</li>
<li><strong>If a file was opened,</strong> disconnect the computer from the network and let your IT provider check it.</li>
</ol>
<p>If it looks more serious than a single click, follow <a href="/been-hacked-first-24-hours">what to do in the first 24 hours</a>.</p>
'''),
        ('team', 'Building a team that catches it', '''
<p>Technology filters out most phishing, but not all of it. What catches the rest is people who recognise the pattern and report it.</p>
<ul>
<li><strong>Short and regular beats long and annual.</strong> A few minutes of practical training each quarter keeps it fresh.</li>
<li><strong>Practise with realistic simulations,</strong> and use the results to coach, not to shame.</li>
<li><strong>A one-click report button</strong> in Outlook, so reporting is quicker than deleting.</li>
<li><strong>Thank people who report,</strong> including false alarms. You want more reports, not fewer.</li>
<li><strong>Directors go first.</strong> Senior people are targeted most and set the tone for everyone else.</li>
</ul>
'''),
    ],
    faqs=[
        ('How do I know if an email is fraudulent?', 'Check whether you were expecting it, look at the real sender address rather than the display name, be wary of urgency, hover over links to see where they really go, and treat any request to log in, pay or change payment details as something to verify through a second channel.'),
        ('What should I do with a phishing email?', 'Do not click links or open attachments. Report it using your report button or by forwarding it to your IT provider, then delete it. If you already clicked or entered a password, tell IT immediately.'),
        ('Can you get hacked just by opening a phishing email?', 'Opening an email on its own is very rarely enough today. The risk comes from clicking a link and entering details, opening an attachment, or approving a sign-in request. That said, report it so your provider can check whether others received it.'),
        ('What is the most common type of phishing for businesses?', 'Credential phishing: emails that lead to a fake login page for Microsoft 365, Google or another service, designed to steal a password. The stolen mailbox is then used for invoice fraud or further phishing.'),
    ],
    related=['invoice-fraud', 'signs-your-business-has-been-hacked', 'email-interception-man-in-the-middle', 'endpoint-security', 'iam', 'outsourced-cyber'],
    cta_h='Want your team to catch the ones that get through?',
    cta_p='Awareness training and email protection are part of every Dividend IT service level. Twenty minutes to see where your team stands.',
),
dict(
    kind='article', slug='email-interception-man-in-the-middle',
    title='Man-in-the-Middle Attacks and Email Interception | Dividend IT',
    og_title='Email interception and man-in-the-middle attacks, explained',
    meta='What a man-in-the-middle attack is, how criminals intercept business email and payments, why basic multi-factor sign-in is not enough and what stops it.',
    card_kind='Fraud guide', card_title='Email Interception and Man-in-the-Middle Attacks',
    card_desc='How criminals get between you and the people you pay, in plain English.',
    trail=[('Insights', '/insights'), ('Email interception explained', '/email-interception-man-in-the-middle')],
    eyebrow='Fraud guide', read=8,
    h1='Email interception and man-in-the-middle attacks, <em>in plain English</em>',
    sub='A man-in-the-middle attack is exactly what it sounds like: someone quietly placing themselves between you and the person you are dealing with, reading and changing what passes between you. Here is how it happens to businesses, and what stops it.',
    sections=[
        ('what', 'What "man in the middle" means', '''
<p>Imagine a postman who opens your letters, reads them, changes the bank details on the invoice, reseals the envelope and delivers it. Neither you nor the recipient can tell anything happened. That is a man-in-the-middle attack.</p>
<p>In business, the "letters" are emails, logins and payment instructions. The attacker's aim is almost always money: redirect a payment, or steal the access that lets them redirect one later.</p>
'''),
        ('ways', 'The three ways it happens to businesses', '''
<h3>1. Inside a compromised mailbox</h3>
<p>The most common version is not technical at all. An attacker steals a password, gets into a mailbox, and becomes the "man in the middle" of every conversation in it. They can read, reply, hide messages and change attachments. Some security people call this "man in the mailbox". It is the engine behind most <a href="/invoice-fraud">invoice fraud</a>.</p>
<h3>2. A lookalike domain slipped into the thread</h3>
<p>Having read a conversation, the attacker copies it and continues it from a near-identical address: dividendit.co instead of dividendit.com, or an "rn" that looks like an "m". Both sides think they are talking to each other. They are both talking to the criminal.</p>
<h3>3. Interception of the login itself</h3>
<p>This is the more technical version. The victim clicks a phishing link that leads to a proxy sitting between them and the real Microsoft or Google login page. They enter their password and approve their multi-factor prompt as normal, and the proxy captures the session that results. The attacker can then use the account <strong>without needing the password or the second factor again</strong>. This is often called an adversary-in-the-middle attack.</p>
<p>Public and poorly secured WiFi can also be used to intercept traffic, although widespread encryption has made that much less common than it used to be.</p>
'''),
        ('mfa', 'Why multi-factor sign-in is essential but not always enough', '''
<p>Multi-factor sign-in stops the vast majority of password attacks and is the first thing every business should have. But the third technique above is designed specifically to get around the most common forms of it, such as text codes and push approvals.</p>
<p>The answer is not to abandon it. It is to strengthen it:</p>
<ul>
<li><strong>Phishing-resistant methods</strong> such as passkeys or physical security keys for directors, finance and administrators. They will not work on a fake login page.</li>
<li><strong>Conditional access rules</strong> that only allow sign-in from managed company devices or expected locations, so a stolen session is useless from the attacker's machine.</li>
<li><strong>Monitoring for risky sign-ins</strong>, such as one account appearing in two countries at once, with someone ready to revoke the session within minutes.</li>
</ul>
<p>We cover this in more depth on our <a href="/iam">identity and access management</a> page.</p>
'''),
        ('protect', 'How to protect the business', '''
<ul class="check">
<li><strong>Verify every payment change by phone,</strong> on a number you already had. This one habit defeats all three techniques.</li>
<li><strong>Use strong multi-factor sign-in,</strong> with phishing-resistant methods for high-risk people and conditional access for everyone.</li>
<li><strong>Set up SPF, DKIM and DMARC</strong> on your domain and move DMARC to enforcement, so criminals cannot send email as your exact domain.</li>
<li><strong>Register the obvious lookalikes of your domain</strong> and monitor for new ones.</li>
<li><strong>Flag external email</strong> so a message from outside the business is clearly marked, even if the name looks familiar.</li>
<li><strong>Watch for inbox rules, forwarding and unusual sign-ins,</strong> with alerts that reach someone who acts on them, day and night.</li>
<li><strong>Use a company VPN or your phone's hotspot</strong> rather than public WiFi for anything sensitive.</li>
</ul>
'''),
        ('signs', 'Signs someone is already in the middle', '''
<ul>
<li>A supplier or customer says they never received an email you sent, or received one you did not.</li>
<li>Replies arrive from an address that is one character different from the real one.</li>
<li>Someone sees a multi-factor prompt they did not trigger, or sign-ins from places they have not been.</li>
<li>Inbox rules or forwarding appear that nobody set up.</li>
</ul>
<p>Any of these deserve an immediate check. See <a href="/signs-your-business-has-been-hacked">the twelve warning signs</a> and <a href="/been-hacked-first-24-hours">what to do in the first 24 hours</a>.</p>
'''),
    ],
    faqs=[
        ('What is a man-in-the-middle attack in simple terms?', 'It is when an attacker secretly places themselves between two parties who think they are talking directly to each other, so they can read, change or redirect what passes between them, such as emails, logins or payment instructions.'),
        ('Can multi-factor authentication stop man-in-the-middle attacks?', 'Basic multi-factor sign-in, such as text codes or push approvals, can be bypassed by adversary-in-the-middle phishing. Phishing-resistant methods such as passkeys and security keys, combined with conditional access rules, are much more effective.'),
        ('How do criminals intercept business emails?', 'Most often by stealing a password and getting into a real mailbox, then watching conversations. Sometimes they continue a stolen conversation from a lookalike domain. Less often, they intercept a login session through a phishing proxy.'),
        ('Is public WiFi safe for business email?', 'It is much safer than it once was because most connections are encrypted, but it is still wise to use a company VPN or your phone\'s hotspot for anything sensitive, and never to ignore certificate or security warnings.'),
    ],
    related=['invoice-fraud', 'how-to-spot-a-phishing-email', 'iam', 'network-security', 'signs-your-business-has-been-hacked', 'outsourced-cyber'],
    cta_h='Find out if anyone is sitting in your inbox.',
    cta_p='We will review sign-ins, inbox rules and email authentication across the business and tell you plainly what we find. Twenty minutes to agree the scope.',
),
dict(
    kind='article', slug='cyber-insurance',
    title='Cyber Insurance for Small Business Explained | Dividend IT',
    og_title='Cyber insurance for small business: what it covers and what insurers ask for',
    meta='Cyber insurance for small business explained: what policies cover and exclude, the security controls insurers ask about and how they affect your cover.',
    card_kind='Owner guide', card_title='Cyber Insurance for Small Business',
    card_desc='What it covers, what it excludes, and what insurers now expect you to have in place.',
    trail=[('Insights', '/insights'), ('Cyber insurance', '/cyber-insurance')],
    eyebrow='Owner guide', read=9,
    h1='Cyber insurance for small business: <em>what it covers and what insurers ask for</em>',
    sub='Cyber insurance has changed. It used to be a box you ticked at renewal. Now insurers ask detailed questions about your security before they will quote, and the answers shape what you pay and whether a claim is paid at all. Here is what owners need to know.',
    sections=[
        ('what', 'What cyber insurance is for', '''
<p>A cyber policy pays for the costs of a cyber incident that most business insurance does not. Wordings vary, but cover usually falls into two halves.</p>
<h3>Your own costs (first party)</h3>
<ul>
<li>Incident response: the specialists who investigate, contain and clean up</li>
<li>Restoring data and systems</li>
<li>Loss of income while the business is disrupted</li>
<li>Extortion and ransom-related costs, where legal and insurable</li>
<li>Notifying affected people and handling the public response</li>
</ul>
<h3>Claims against you (third party)</h3>
<ul>
<li>Liability to customers or partners whose data was exposed</li>
<li>Legal defence costs</li>
<li>Regulatory investigation costs and, where the law allows, fines</li>
</ul>
<p>For many smaller businesses, the most valuable part is not the money. It is the incident response team on the end of the phone when something goes wrong.</p>
'''),
        ('gaps', 'Common gaps and exclusions', '''
<p>Read the wording, or ask your broker these questions directly.</p>
<ul>
<li><strong>Is invoice fraud covered?</strong> Losses from being tricked into paying the wrong account often sit under a separate "social engineering" or "funds transfer fraud" section with a much lower limit, or are excluded entirely. See our <a href="/invoice-fraud">invoice fraud guide</a>.</li>
<li><strong>What are the conditions?</strong> Many policies require prompt notice and the use of the insurer's approved responders. Calling your own IT company first and spending money without consent can affect a claim.</li>
<li><strong>What did we declare?</strong> If the proposal form says multi-factor sign-in is enabled everywhere and it was not on the account that was breached, expect a difficult conversation.</li>
<li><strong>Improvements and known issues.</strong> Policies generally will not pay to upgrade your systems beyond where they were, or for problems you knew about before cover started.</li>
<li><strong>Waiting periods.</strong> Business interruption cover usually only starts after a set number of hours of disruption.</li>
</ul>
'''),
        ('controls', 'The controls insurers now ask about', '''
<p>Proposal forms differ, but the same handful of questions appear on almost all of them. Each one maps to a control that genuinely reduces risk.</p>
<div class="tbl-wrap"><table class="cmp">
<tr><th>Insurers ask</th><th>What it means in practice</th></tr>
<tr><td>Multi-factor authentication</td><td>On email, remote access and admin accounts, without exceptions</td></tr>
<tr><td>Endpoint detection and response</td><td>Modern protection on every device, ideally monitored around the clock</td></tr>
<tr><td>Backups</td><td>Separate from the main network, protected from deletion, and tested</td></tr>
<tr><td>Patching</td><td>Critical updates applied within a defined time</td></tr>
<tr><td>Email security</td><td>Filtering, link protection and email authentication</td></tr>
<tr><td>Privileged access</td><td>Few admin accounts, separate from everyday accounts</td></tr>
<tr><td>Training</td><td>Regular awareness training and phishing simulation</td></tr>
<tr><td>Incident response plan</td><td>Written, with contacts, and tested</td></tr>
</table></div>
<p>If you cannot answer "yes" honestly to these, fix that before renewal. It is better for the business and it is better for the conversation with your insurer.</p>
'''),
        ('value', 'How security changes what you pay', '''
<p>Security and insurance are two sides of the same risk. When you can show strong controls with evidence, rather than just ticking boxes, you widen the range of insurers willing to quote and put yourself in a stronger position on terms. When you cannot, cover can become more expensive, more restricted, or harder to find.</p>
<p>This is one of the clearest places where cyber security shows up in the financials. It is also something a buyer's advisers will look at: an insurable business with an evidenced security record is a lower-risk acquisition.</p>
<p>We help clients map their controls to the questions insurers ask and back each answer with evidence, so renewal is a short, accurate exercise and not a guessing game.</p>
'''),
        ('buy', 'How to buy it well', '''
<ul class="check">
<li><strong>Use a broker who specialises in cyber,</strong> and ask them to explain the exclusions in plain English.</li>
<li><strong>Answer the proposal form with your IT provider in the room.</strong> Accuracy matters more than looking good.</li>
<li><strong>Check the limit for social engineering and invoice fraud</strong> against the size of your typical payments.</li>
<li><strong>Know the incident line and the conditions</strong> before you need them, and add them to your incident plan.</li>
<li><strong>Review it each year</strong> as your business and your security change.</li>
</ul>
<p>We are not insurance brokers and do not sell insurance. We help you put the controls in place, evidence them and answer the technical questions accurately.</p>
'''),
    ],
    faqs=[
        ('Do small businesses need cyber insurance?', 'Most benefit from it, particularly those that hold customer data, rely on IT to trade or move significant payments by email. The most useful part is often the incident response support rather than the payout. It works best alongside good security, not instead of it.'),
        ('What does cyber insurance not cover?', 'Common exclusions include improving systems beyond their previous state, known incidents before the policy started, and losses where the policy conditions were not met. Invoice fraud is often excluded or covered only at a low limit.'),
        ('What security do I need for cyber insurance?', 'Insurers typically ask about multi-factor authentication, endpoint detection and response, protected and tested backups, patching, email security, control of admin accounts, staff training and an incident response plan.'),
        ('Can a cyber insurance claim be refused?', 'Yes. Claims can be disputed if the proposal form was inaccurate, for example if multi-factor sign-in was declared but not enabled on a breached account, or if policy conditions such as prompt notification were not followed.'),
    ],
    related=['outsourced-cyber', 'governance-cyber', 'backup-dr', 'detection-response', 'invoice-fraud', 'true-cost'],
    cta_h='Go into your next renewal with evidence.',
    cta_p='We will map your controls to the questions insurers ask, close the gaps and give you evidence you can stand behind. Twenty minutes to start.',
),
]
