label scene18:
scene rooftopnight

"What should have been a simple excursion to get here turned into an ordeal near the end."
"I don't think I've felt this exhausted since the day I first moved here... which shows how much I know about college in more ways than one."
"I lean against the balcony, staring out at the rest of the school as I gather my thoughts."
"..."
"It's still taking me a long while to process the last couple of days."
"It started with Kamika barging into my life at just the right time where I didn't want any more demons hanging around me."
"Then to make matters worse, she had plans to dominate the entire school, and she almost succeeded in those plans to boot."
"But in the end, we managed to prevent her from going too far..."

if route = "stacey":
    jump staceyend
elif route = "lucca":
    jump luccaend
elif route = "kamika":
    jump kamikaend
#dialogue path if on Stacey route

label staceyend:
"I think it was all because Stacey knew how to help me keep my head cool."
"She's an... eccentric girl, to put it bluntly. Sometimes I'm not even sure if she's all there or not."
"Yet when she {i}does{/i} say something, it feels more insightful than I give her credit for."
"She has a good head for writing as well; so long as she keeps that up, I'm sure she has a bright future ahead of her."
"...I could do without her being so familiar with demons, but, oh well. Beggars can't be choosers."
jump s18merge

#dialogue path if on Lucca route

label luccaend:
"I couldn't have done it without Lucca's help."
"She's timid, sure, and a bit of a crybaby, but there's a fire and a passion underneath that I've never seen before."
"She'll never hesitate to stand up for someone she's close to, either. She's a kind soul... for a demon, anyway."
"I've got no idea how far she'll go with her graffiti art... heck, I don't even know if she'll keep it up."
"But she's more serious about it than I can even imagine, so... I think she'll be fine."
jump s18merge

#dialogue path if on Kamika route

label kamikaend:
"Then we had that fight, me and her, and... I managed to learn more about her right then and there than I ever did before."
"But it doesn't feel right to me. Why would she even go to all that trouble in the first place?"
"It can't just be out of simple envy, could it? These demons base all of their friggin' identities around their assigned sin, so it's the most probable answer to me."
"But when I think back to how hard she went off... I get the feeling the root of the problem goes deeper than that."
"...Oh well, it's not like she'd ever tell me anyways. I doubt she'll even stick around my room after today."

voice "c-18-1.mp3" #Kamika (Ariane Marchese)
kam "...Hey, Yumi?"

"Hearing a familiar voice call my name, I turn around to find..."

#show kam

voice "c-18-2.mp3" #Yumi (Kathy Pfautsch)
yum "Kamika? What are you doing here?"

voice "c-18-3.mp3" #Kamika (Ariane Marchese)
kam "...Same as you. I wanted to be somewhere quiet."

"She strolls over to the balcony and stands next to me, not saying anything."
"I keep expecting her to bark orders or flaunt herself like no tomorrow, but... she just stares out over campus, same as me."

voice "c-18-4.mp3" #Kamika (Ariane Marchese)
kam "It's a nice night, isn't it?"

voice "c-18-5.mp3" #Yumi (Kathy Pfautsch)
yum "Yeah. It's a little chilly, though."

"...Things are quickly getting awkward between the two of us."
"Eventually, Kamika turns her head towards me."

#show kam sad

voice "c-18-6.mp3" #Kamika (Ariane Marchese)
kam "I... I wanna apologize to you, for... the last several days."

voice "c-18-7.mp3" #Yumi (Kathy Pfautsch)
yum "Huh?"

voice "c-18-8.mp3" #Kamika (Ariane Marchese)
kam "Yeah, it... I was so caught up in trying to prove myself, and I ended up dragging you into all of it."

voice "c-18-9.mp3" #Kamika (Ariane Marchese)
kam "I called you names, bossed you around, didn't respect your personal space... Honestly there was a lot I did wrong."

voice "c-18-10.mp3" #Yumi (Kathy Pfautsch)
yum "Well, yeah, you did. I'm surprised it took you this long to notice."

voice "c-18-11.mp3" #Kamika (Ariane Marchese)
kam "...I had a long talk with S-Tan. A-about my recent behavior, I mean..."


voice "c-18-12.mp3" #Kamika (Ariane Marchese)
kam "It's not right to put friends through that, but I was so convinced everyone was my enemy that..."

voice "c-18-13.mp3" #Yumi (Kathy Pfautsch)
yum "..."

voice "c-18-14.mp3" #Yumi (Kathy Pfautsch)
yum "...What {i}was{/i} that stuff you were talking about earlier, anyway?"

#show kam surprised

voice "c-18-15.mp3" #Kamika (Ariane Marchese)
kam "What?"

voice "c-18-16.mp3" #Yumi (Kathy Pfautsch)
yum "You know, that stuff you went on about. 'Measuring up to people's expectations' and all that."

voice "c-18-17.mp3" #Kamika (Ariane Marchese)
kam "Oh, um... did I say all that? I can barely even remember."

voice "c-18-18.mp3" #Yumi (Kathy Pfautsch)
yum "Well it's just hard for me to forget, is all."

voice "c-18-19.mp3" #Yumi (Kathy Pfautsch)
yum "...Did you want to talk about it? Maybe get something off your chest? I'm here to listen if you need to vent."

#show kam sad

voice "c-18-20.mp3" #Kamika (Ariane Marchese)
kam "I-I..."

voice "c-18-21.mp3" #Kamika (Ariane Marchese)
kam "...Very well. I suppose you deserve an explanation for all that. But where to even start..."

voice "c-18-22.mp3" #Yumi (Kathy Pfautsch)
yum "Why not just at the beginning? I feel like that's where most of this is coming from."

voice "c-18-23.mp3" #Kamika (Ariane Marchese)
kam "Y-yeah, you're right."

voice "c-18-24.mp3" #Kamika (Ariane Marchese)
kam "To tell you the truth... I'm not the powerful and popular succubus you think I am."

voice "c-18-25.mp3" #Yumi (Kathy Pfautsch)
yum "Okay, well, that much is obvious, but go on."

voice "c-18-26.mp3" #Kamika (Ariane Marchese)
kam "No, but like... I was never born that way to begin with."

voice "c-18-27.mp3" #Kamika (Ariane Marchese)
kam "You see, from a young age we succubi are expected to have a good grasp on the art of seduction. That's how we make our living."

voice "c-18-28.mp3" #Kamika (Ariane Marchese)
kam "But whenever I tried it... I was always miserable at it."

voice "c-18-29.mp3" #Kamika (Ariane Marchese)
kam "And the problem was never my poses or gestures, or how I carried myself; I got those down better than anyone."

voice "c-18-30.mp3" #Kamika (Ariane Marchese)
kam "No, the real problem... was with my pheromones."

voice "c-18-31.mp3" #Kamika (Ariane Marchese)
kam "My pheromones were never as potent as the rest of my peers, so I would always fall behind the others of my race."

voice "c-18-32.mp3" #Yumi (Kathy Pfautsch)
yum "Huh. I didn't even know there was such a thing as weak pheromones. Guess that explains a lot."

voice "c-18-33.mp3" #Yumi (Kathy Pfautsch)
yum "But, you had people to help you with that, right?"

voice "c-18-34.mp3" #Kamika (Ariane Marchese)
kam "...I didn't have anyone."

voice "c-18-35.mp3" #Kamika (Ariane Marchese)
kam "The rest of my kind had no patience for someone who couldn't keep up with everyone else. In fact, they wanted nothing to do with me."

voice "c-18-36.mp3" #Kamika (Ariane Marchese)
kam "They would always tease and taunt me over my weakness, and then they would say I'm worth nothing to anyone."

voice "c-18-37.mp3" #Kamika (Ariane Marchese)
kam "It was so frustrating to be told that over and over in my childhood... Eventually, I ended up believing what they said to me."

voice "c-18-38.mp3" #Kamika (Ariane Marchese)
kam "I thought I was absolutely worthless, to the point where I really felt like no one would miss me if I died..."

voice "c-18-39.mp3" #Yumi (Kathy Pfautsch)
yum "Kamika..."

voice "c-18-40.mp3" #Kamika (Ariane Marchese)
kam "Yet I also felt my time with my brethren couldn't go on forever... I knew I had to get away from all of them."

voice "c-18-41.mp3" #Kamika (Ariane Marchese)
kam "And that was when I found S-Tan."

voice "c-18-42.mp3" #Kamika (Ariane Marchese)
kam "We met each other at a bar years ago... and lemme tell you, we just hit it off."

voice "c-18-43.mp3" #Kamika (Ariane Marchese)
kam "She was one of the sweetest, most kind-hearted demons I had ever met, and she would always believe in me and my talents, no matter what."

voice "c-18-44.mp3" #Kamika (Ariane Marchese)
kam "But she was so busy a lot of the time, what with demon summonings and all... It was hard for us to stay together for too long."

voice "c-18-45.mp3" #Yumi (Kathy Pfautsch)
yum "Makes sense. Lots of people wanting to summon Satan for their own wants and needs."

voice "c-18-46.mp3" #Kamika (Ariane Marchese)
kam "Yeah. At some point, I was worried I was really going to lose her..."

#show kam happy

voice "c-18-47.mp3" #Kamika (Ariane Marchese)
kam "But then, when she told me she wanted to start an idol group, and that she wanted me to be a part of it... that meant more to me than anything."

voice "c-18-48.mp3" #Kamika (Ariane Marchese)
kam "We hooked up together with a bunch of other like-minded demons and started calling ourselves the Sinful Stars, hoping to take the Underworld by storm."

voice "c-18-49.mp3" #Kamika (Ariane Marchese)
kam "Not only was I gonna keep being with S-Tan, but I had a whole group of people I could call my friends. For the first time in my life, I was... truly happy."

#show kam sad

voice "c-18-50.mp3" #Kamika (Ariane Marchese)
kam "But... then again, I wasn't."

voice "c-18-51.mp3" #Kamika (Ariane Marchese)
kam "We were getting lots of attention, yes, but S-Tan was always the one people talked about the most."

voice "c-18-52.mp3" #Kamika (Ariane Marchese)
kam "No one ever brought up my accomplishments or how hard I worked; people only ever talked about what a great job S-Tan did or how nice and talented she was."

voice "c-18-53.mp3" #Kamika (Ariane Marchese)
kam "She was getting everything I wanted, while I wasn't left with anything. I felt like I was being left behind, by the one person I cared about the most..."

voice "c-18-54.mp3" #Kamika (Ariane Marchese)
kam "Then, at some point, S-Tan wanted to give us little titles named after each sin. You know, 'cuz there were seven of us and all."

voice "c-18-55.mp3" #Kamika (Ariane Marchese)
kam "I made it very clear to her that I wanted the title of Lust, and she told me she would give it some serious thought."

voice "c-18-56.mp3" #Kamika (Ariane Marchese)
kam "At the time I thought, 'this is my chance! This will show all those bitches who put me down in the past!' I couldn't wait to take my Demon of Lust title and shove it in their faces."

#show kam angry

voice "c-18-57.mp3" #Kamika (Ariane Marchese)
kam "But I never got what I wanted... and instead I got stuck with the title of Envy."

voice "c-18-58.mp3" #Yumi (Kathy Pfautsch)
yum "I mean, I can see why at least. She must have noticed how envious you were of people around you."

voice "c-18-59.mp3" #Kamika (Ariane Marchese)
kam "Yeah, but the first time she explained that and why she thought it fit me... I was so angry."

voice "c-18-60.mp3" #Kamika (Ariane Marchese)
kam "I thought that, after all the years we knew each other, she had stabbed me in the back and given me a horrible title just because she was better and more popular than me."

voice "c-18-61.mp3" #Kamika (Ariane Marchese)
kam "I began thinking she had been making fun of me this whole time. Like she thought our entire friendship was a joke... and she thought I was no better than garbage."

voice "c-18-62.mp3" #Kamika (Ariane Marchese)
kam "Then I started thinking about the others. They had so much better titles than I did; the only guy we got even got the Lust title all for himself!"

voice "c-18-63.mp3" #Kamika (Ariane Marchese)
kam "So why was I stuck with the ugliest title of all? Were they just out to get me? Did they really want to make me feel as horrible as I did all those years ago?"

voice "c-18-64.mp3" #Kamika (Ariane Marchese)
kam "I was just so angry and frustrated with the whole thing... I couldn't stand to see them so happy with themselves while I was left to suffer."

voice "c-18-65.mp3" #Kamika (Ariane Marchese)
kam "So... I let those ugly thoughts and feelings manifest into reality, and... I'm sure you heard S-Tan explain what I did."

voice "c-18-66.mp3" #Yumi (Kathy Pfautsch)
yum "Yeah, I did hear all that."

voice "c-18-67.mp3" #Kamika (Ariane Marchese)
kam "So finally, I tried one last time to appeal to S-Tan to give me the title of Lust, but do you know what she said when I asked why she couldn't do that?"

voice "c-18-68.mp3" #Kamika (Ariane Marchese)
kam "'There's nothing else that's a better fit for you~!'"

voice "c-18-69.mp3" #Kamika (Ariane Marchese)
kam "And... every single piece of rage and frustration boiled over in that moment, and I left the Sinful Stars for good."

#show kam neutral

voice "c-18-70.mp3" #Kamika (Ariane Marchese)
kam "For seven months, I drifted from place to place in the Underworld, trying desperately to make it on my own."

voice "c-18-71.mp3" #Kamika (Ariane Marchese)
kam "I wanted so bad to be noticed and acknowledged, that somewhere along the way, I began fixating on wanting the whole {i}world{/i} to love me."

voice "c-18-72.mp3" #Kamika (Ariane Marchese)
kam "That's when I decided, \"if I can't {i}earn{/i} people's love, then I just need to {i}force{/i} them to love me. That'll show them all!\""

voice "c-18-73.mp3" #Kamika (Ariane Marchese)
kam "So I put together a plan to slowly take this world, piece by piece, until it was all mine."

voice "c-18-74.mp3" #Kamika (Ariane Marchese)
kam "I integrated myself into the school without a hitch, and then... well, you pretty much know the story by that point."

voice "c-18-75.mp3" #Yumi (Kathy Pfautsch)
yum "..."

"It... does make a lot of sense why she acted the way she did."

"She was always apprehensive about her singing specifically, and she did always hate to hear me doing any better than her."

"But as Kamika pointed out... it doesn't excuse her actions. Not to me, and not to anyone else."

#show kam sad

voice "c-18-76.mp3" #Yumi (Kathy Pfautsch)
yum "Look... I get wanting to be acknowledged. There's not a day that goes by where I feel like a lot of people are passing up my work."

voice "c-18-77.mp3" #Yumi (Kathy Pfautsch)
yum "But doing what you did was unnecessary and way over the line. A lot of people could have gotten hurt because of your stupid ideas."

voice "c-18-78.mp3" #Yumi (Kathy Pfautsch)
yum "Not to mention the whole time I was with you, you were treating me like {i}crap!{/i} You were {i}never{/i} appreciative of any help I gave you!"

voice "c-18-79.mp3" #Yumi (Kathy Pfautsch)
yum "If you're really sorry for what you've done, it's gonna take more than an apology to fix this, you know."

voice "c-18-80.mp3" #Kamika (Ariane Marchese)
kam "I know, but... what do I {i}do?{/i}"

voice "c-18-81.mp3" #Kamika (Ariane Marchese)
kam "I've tried everything to get people to notice me, but nothing ever works..."

voice "c-18-82.mp3" #Yumi (Kathy Pfautsch)
yum "...Have you ever tried just singing for yourself?"

#show kam surprised

voice "c-18-83.mp3" #Kamika (Ariane Marchese)
kam "'For myself...?'"

voice "c-18-84.mp3" #Yumi (Kathy Pfautsch)
yum "Yeah, I mean, you seem to actually like singing a lot. Your first plan even revolved around singing, if... only for the wrong reasons."

voice "c-18-85.mp3" #Kamika (Ariane Marchese)
kam "Wh-why does that matter? How is that gonna help me?"

voice "c-18-86.mp3" #Yumi (Kathy Pfautsch)
yum "I'm just saying, maybe you oughta focus on what {i}you{/i} might like more than what you think everyone {i}else{/i} might like."

voice "c-18-87.mp3" #Yumi (Kathy Pfautsch)
yum "Like, take me for instance. I like painting what I see, and I end up showing people what I wanted to see in that moment."

voice "c-18-88.mp3" #Yumi (Kathy Pfautsch)
yum "If you can sing the songs that {i}you{/i} want to sing, then people might start to see you have a real love of what you do. Then you'll get fans more naturally."

voice "c-18-89.mp3" #Yumi (Kathy Pfautsch)
yum "I dunno, it was just a thought that occurred to me."

#show kam sad

voice "c-18-90.mp3" #Kamika (Ariane Marchese)
kam "...I guess I could try. But just because I'm doing what I like doesn't mean people will pay attention."

voice "c-18-91.mp3" #Kamika (Ariane Marchese)
kam "What if I do end up doing what I like, yet people still don't notice..."

voice "c-18-92.mp3" #Yumi (Kathy Pfautsch)
yum "Well, if it comes to that, then I can help you get your name out there."

#show kam surprised

voice "c-18-93.mp3" #Kamika (Ariane Marchese)
kam "...Really? You would do that?"

voice "c-18-94.mp3" #Yumi (Kathy Pfautsch)
yum "If I see you really trying for yourself, then sure."

voice "c-18-95.mp3" #Yumi (Kathy Pfautsch)
yum "You've got a really nice voice, Kamika. You shouldn't be wasting it on just chasing after attention all the time."

voice "c-18-96.mp3" #Yumi (Kathy Pfautsch)
yum "I can guarantee you'll be a lot happier if you do it for the love of it, and if you do go that route, I'll try to get people to see just how much you love what you do."

voice "c-18-97.mp3" #Kamika (Ariane Marchese)
kam "I..."

#show kam smiling

voice "c-18-98.mp3" #Kamika (Ariane Marchese)
kam "You're too good to me, Yumi... Thank you."

"...Somehow it feels weird to see Kamika be this appreciative towards me."
"But maybe this is what she really needs; a positive approach to putting herself out there, one that will give her a lot more personal satisfaction."
"It'd certainly be a lot better than her crazy plans for world domination, at the very least..."

voice "c-18-99.mp3" #Yumi (Kathy Pfautsch)
yum "Oh, yeah, there was one other thing I was wanting to mention..."

voice "c-18-100.mp3" #Kamika (Ariane Marchese)
kam "Huh? What's that?"

voice "c-18-101.mp3" #Yumi (Kathy Pfautsch)
yum "I think I like it better when you refer to me as a friend rather than a minion."

#show kam embarrassed

voice "c-18-102.mp3" #Kamika (Ariane Marchese)
kam "Wh-wha-? D-did I say that?! I, u-um..."

voice "c-18-103.mp3" #Kamika (Ariane Marchese)
kam "I don't know what you're talking about! Y-you must have misheard!"

voice "c-18-104.mp3" #Yumi (Kathy Pfautsch)
yum "Did I? I'm a better listener than that, wouldn't you think?"

voice "c-18-105.mp3" #Kamika (Ariane Marchese)
kam "Y-y-you're..."

voice "c-18-106.mp3" #Kamika (Ariane Marchese)
kam "(sigh) You're right. You've been succeeding my expectations so much that it hardly seems fair to call you 'minion' anymore."

#show kam happy

voice "c-18-107.mp3" #Kamika (Ariane Marchese)
kam "I'll allow it."

voice "c-18-108.mp3" #Yumi (Kathy Pfautsch)
yum "You'll 'allow it?' You sound like you're still wanting to take charge."

voice "c-18-109.mp3" #Kamika (Ariane Marchese)
kam "W-well, this time it's different! I'm going to take charge of my own destiny from here on out!"

voice "c-18-110.mp3" #Kamika (Ariane Marchese)
kam "I won't let other people dictate my happiness; I'll do everything I can for my own sake!"

#show ending CG for Kamika

"She grabs me by the arm and pulls me along with renewed vigor."

voice "c-18-111.mp3" #Yumi (Kathy Pfautsch)
yum "Ah, wait! Slow down!"

voice "c-18-112.mp3" #Kamika (Ariane Marchese)
kam "Come on, Yumi! Let's go!"

voice "c-18-113.mp3" #Yumi (Kathy Pfautsch)
yum "'Go?' Go where?!"

voice "c-18-114.mp3" #Kamika (Ariane Marchese)
kam "Towards our destiny, of course!"

voice "c-18-115.mp3" #Kamika (Ariane Marchese)
kam "Together, we'll become a shining duo that express themselves for their own sake!"

voice "c-18-116.mp3" #Kamika (Ariane Marchese)
kam "People can think whatever they want; as long as we're happy, that's what really matters! I'm not gonna let anything stop us from-"

#fade CG
#scene black

"{i}BONK!{/i}"

voice "c-18-117.mp3" #Kamika (Ariane Marchese)
kam "{i}Owww...{/i}"

"Kamika ends up bonking her face right in the door."

voice "c-18-118.mp3" #Yumi (Kathy Pfautsch)
yum "H-hey! Are you alright?"

voice "c-18-119.mp3" #Kamika (Ariane Marchese)
kam "Y... yeah. I'll be fine..."

"Hoo boy. This is gonna be a loooong semester..."

label s18merge:
"I look up to the night sky, finding stars as I see them."
"Who knows what the future's gonna be like for me... for all of us."

jump credits
