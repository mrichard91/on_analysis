# Common Cyber Threat Intel Biases
I've been working in and around cyber threat intelligence for about 25 years, and over that time, I've found myself saying some phrases repeatedly. I often try to convey biases, blind spots, and systematic weaknesses in how teams evaluate and write about threat intelligence. Each phrase could use a whole post, so I'll summarize each here. Feel free to steal anything useful and ignore what isn't.

## Analytical Biases
### Hindsight is 50/50
 Not a typo - we often look into the past where we have a lot of data and think we have 20/20 vision, but the truth is the past is often hazy, and we're telling a story about the past rather than faithfully recalling it. Rarely do we see the past with the clarity that we believe.

### Omniscience fallacy 
I have worked for and with threat intel teams with a lot of visibility into threat activity. This analytical fallacy occurs when analysts unconsciously think that their extensive visibility represents all actions rather than just a subset. I see a lot of activity; therefore, I see almost all activity; hence I know all there is to know about a threat.

### Threat narrative fallacy 
This fallacy mirrors the traditional narrative fallacy - fitting threat activity into a clean story that fits our existing beliefs instead of objectively weighing the facts. Stories that fit broader geopolitical narratives about countries, political parties, and past objectives often absorb new data since it aligns with the existing story.

### "Malicious" colored glasses
Most threat intel analysts spend their days looking at malicious activity and very little time looking at benign activity. Over time this begins to bias analysts toward believing that any activity they choose to look into is malicious without considering the context objectively. On the Internet scale, only a very small set of activities is malicious. Hence, it's essential to objectively evaluate data rather than see it through the lens of "probably malicious."

### There are no laws of physics on the Internet
Part of what makes threat intelligence so exciting is that the Internet is just a series of bits in various circuits - adversaries and defenders can manipulate this environment in unexpected ways. The challenge comes when analysts assume that because a technology is "supposed" to work a specific way, it *must* work that way, like physics. I've worked on incidents where we had to explicitly ignore how things should work to get to the root cause. For example, a VPN client with split tunneling turned off should route all packets over VPN… unless the adversary has shimmed the client to send the bad traffic out of your view…

### Omnipotent adversary fallacy
When evaluating courses of defensive action against adversaries, analysts often devolve into perfectionism based on how an omnipotent adversary would respond. For example, saying that blocking a specific port used by malware won't be effective because it would be simple for an adversary to change. It is easy to overlook that adversaries have many constraints, including time, visibility, money, and developers, that limit their available responses. For various reasons, adversaries also don't always take actions that the analyst considers obvious or rational.

### Little a vs. big A attribution
In cyber threat intel, we spend a fair amount of time discussing who is responsible for events. I have found two useful standards for attribution - little a and big A. Little a attribution involves the preponderance of evidence, including circumstantial, cui bono, diamond model, and other inferences from observations. Big A Attribution requires a higher standard - proof beyond a reasonable doubt. Big A attribution is complex, often requiring national means to collect the needed intelligence, and is almost always out of the reach of private firms. In 2018 I helped Alex Stamos write this article articulating our decision not to try and provide attribution despite having some circumstantial evidence https://about.fb.com/news/2018/11/investigating-threats/#whos-behind-cyber-threats. Analysts should carefully consider what they can prove and caveat attribution statements, almost always with "little a."