# How to do good work in Cyber Threat Intelligence
2023-05-16/mjr

In my cyber threat intelligence (CTI) career, I've mentored analysts, managed teams, and worked on high-stakes cases. Through this experience, I have picked up a few common threads that consistently produce good work in CTI. What is good work? Objectively defensible work can be easily updated to account for new information and maximize the benefit to the sponsoring organization while being frugal in the use of resources. 

Here are the ideas I find helpful:
* Get good at being wrong.
* Fight like Ironman.
* Be a historian, not an oracle. 
* Know when you are riding a bicycle chasing a train.

## Get good at being wrong. 
We have all made mistakes in our work, some big and some small. Doing good work requires discovering when you are wrong, correcting your previous work, and reducing the error rate in the future. CTI  is a discipline that requires constant vigilance, learning, and process refinement. 

Here's a scenario I have seen many times - an analyst starts with a lead on infrastructure used by a malicious actor and pivots on connections to domains, IP addresses, malware, and anything available. In the process, they are overconfident in one of the pivots; for example, thinking an IP is dedicated but instead is compromised. When they later realize this mistake, they find that some of their work was predicated on this faulty pivot. 

To get good at being wrong, ask yourself how well you can reevaluate all the dependent data and update your work after finding a mistake. What if you realize this mistake was six months ago? I have seen whole cases be thrown out and started over because an analyst couldn't untangle a single mistake made early in the investigation. Also, look at this post about the ["Joy of being wrong"](https://sanger.umich.edu/think-again-8-11-22/) and then check out the book ["Think Again"](https://adamgrant.net/book/think-again/) by Adam Grant. Check out my previous post about common cyber threat intelligence biases, which goes into more detail about specific biases to identify and correct. 

## Fight like Ironman. 
Tony Stark wasn't the physically strongest Marvel superhero. He doesn't have any innate special powers. Instead, he is a polymath with a broad skillset who has built systems and tools that combine to form a highly capable superhero. 
One of the most exciting parts about Ironman is that the suit itself can take an average human and confer superpowers on them. When I think of doing threat intelligence, I ask myself how can I make an Ironman suit that gives me and all other analysts superpowers. In my experience with teams, the ability to scale by raising all analysts is often overlooked in favor of trying to hire more superheroes. Instead, scale and fight by creating well-designed tools that are intuitive, codifying the techniques of the best analysts, and making every analyst into Ironman.

My favorite example of an Ironman suit was [Collaborative Research into Threats (CRITs)](https://crits.github.io/). When I wrote the early software that later became CRITs I was finding a way to capture my own worflow in an easy to use method that I could repeat for many new malware samples. When I started writing CRITs at MITRE, I expanded the scope to take all of the techniques and knowledge that I had and be able to give it to any other analyst. For example, you could upload an email .eml file, extract the attachments, scan the attachments with yara and other tools and quickly triage if it might be malicious. In the process, it created all of the artifacts and metadata that could later be analyzed for patterns. CRITs allowed our team to level everyone up while creating shared and consistent documentation.

## Be a historian, not an oracle. 
Nobody regrets doing a good job documenting things in the past. As an analyst I find it slow and cumbersome to write down all of my observations, make sure they are clear and understandable and published in a consistent location. The alternative is to stuff my brain full of facts and observations, quickly accessing them as needed when I come across new information. This "in your head" storage allows for very fast connections, low overhead and makes others completely dependent upon you to keep the work going. This "oracle" style of threat intel, where an analyst knows the details and can be asked questions to get the ultimate answers seems to be a default mode for many analysts.

Over the years I've instead started to think about being a historian - documenting, noting and sharing what I find to allow others to build upon it and make myself unnecessary. Doing this requires some vulnerability for an analyst because it requires releasing control of a topic, allowing others to inspect it and potentially modify it. In the end I find this leads to much better outcomes, but can create a vulnerable feeling of being a cog in a machine or unneeded. Instead I think this demonstrates real value, the analytical insights of many members can be brought to bear on a problem, new ideas and connections can be made and the work can continue during vacations and promotions.

## Know when you are using a bicycle to chase a train. 
No matter how big the CTI team is, they run into an unfortunate problem - there are a lot more adversarial actors they need to understand, track, and mitigate than they currently have the resources to address. This leads to a situation I think of as riding a bicycle at 25mph while trying to catch a train going 40mph. When will you catch the train?

I often see teams try to address this with a combination of: 
1) request and trying to hire a lot more people to account for this work; 
2) limiting the scope of what they will do to a narrow set of actors that they deem as the highest risk; 
3) work a lot harder. 

All of these approaches ignore the underlying fact that there are more threats, using more sophisticated tools and more things to track all the time - you can't catch that train on your bicycle and even if you did you can't sustain it.

The important part here is to recognize when you are in this impossible situation and plan how to change your game in a big way. Avoid thinking about ways to get incrementally better like tracking 20% more actors, or giving each analyst more tasks. Instead, think about how to scale by orders of magnitude. What would it take to track 10x the number of actors with the same number of analysts? This almost always requires automation and understanding the important outcomes. 