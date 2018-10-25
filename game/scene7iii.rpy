label scene7iii:
scene dormhallway

#CHECK: flags for Scene 6 choice
#MIGHT NEED WORK; GONNA WRITE UP A SECTION FOR IF YUMI GOES TO SEE STACEY INSTEAD

"I get hit with a feeling of dread approaching my dorm room. I even took the long way back home to stave off the inevitable..."
"Is it just the thought that I can't leave her alone for one second without her causing trouble? Or am I just a glutton for punishment?"
"God, I can already imagine what she might say to me as soon as I get back."
"'Took you long enough, now lick my feet, peasant!' Or {i}something{/i} like that."
"I'm stuck thinking of all the possible ways she might mess with me as I make my way back to my dorm room."

if sawstacey = True:
    jump angrykamika
else:
    jump showerkamika

label showerkamika:
#BRANCH: use if opted to head to Kamika in Scene6
"But when I round the corner and head down the hall back to my room... I hear something."

kam "...lala... lalala...~"

yum "Huh...?"

"There's a pleasant sound filling the air. Not a particularly random sound, but one that's controlled and deliberate."
"It's constantly changing pitch and volume, but it never gets obnoxious. It's ebbing and flowing with all the careful precision in the world..."
"...Is that... singing?"

yum "..."

"Thinking it must be coming from someone else's room, I enter my own room in silence."

#scene dormroom

"...Except the singing only gets louder when I enter my room."
"I should be raising complaints about this, yet for some reason, I can't muster the will to. Singing like that shouldn't even be considered an inconvenience."
"Not only is there singing, but I can hear the shower in the bathroom running... and Kamika is nowhere to be found in here or my bedroom."
"Part of me wants to gag at the thought of giving her any sort of compliment, but the other half... wants to keep listening."
"I put my ear to the bathroom door, close my eyes... and listen."

#show CG of Kamika singing in the shower

kam "I know you feel the fire inside my heeeart~ It's burnin' so brightly for you~"

kam "I know how scared you are to even staaart~ Just don't ever say 'adieu~'"

kam "I want you stay, I want you to love me now and forever~"

kam "Baby pleeeease, don't let this beeee..."

kam "Our last night togetherrrr~"

"She sings with a passion and a drive that's hitherto unheard of..."
"Why was she ever talking about 'taking over the world' with singing like this?"
"...That {i}is{/i} Kamika in there, right?"
"I knock on the door and ask just to be safe."

yum "Kamika? Is that you in there?"

kam "EEP!"

kam "I-I mean, who's to say? Why don't you come on in and find out~?"

"...Yeah, no doubt about it. That's definitely her."

yum "N-no thanks, I'm good."

kam "Oh well, your loss~"

#fade CG
#scene dormroom

"I spend the next few precious moments catching up on my anatomy homework."
"What a relief it is to be able to relax in my own dorm room and not worry about some stupid demon. Even if their singing is better than I could have imagined..."
"In no time at all, however, my peace and quiet is interrupted by Kamika emerging from the bathroom."

#show kam confident, eyes closed

kam "Ahh, now {i}that{/i} felt good~! I'm impressed this shower system manages to be so thorough~"

kam "It's been so long since I had a proper shower... My skin feels all tingly~"

#show kam confident

kam "You can feel for yourself, if you'd like~"

yum "No matter how much you scrub, you'll {i}never{/i} be clean."

#show kam worried

kam "Aww, Yumi, I'm crushed..."

"I feel nauseous all of a sudden. How come every time I talk to her it feels like going through the adult magazines on the news rack?"

#show kam annoyed

kam "So you got a good listen to my singing, did you? I hoped I could do it in peace without {i}you{/i} around."

kam "Lemme guess; you're gonna tell me to keep it down, aren't you?"

yum "What, your singing? I {i}did{/i} hear that, and..."

yum "...it's really good, actually."

#show kam surprised

kam "...Really?"

#show kam embarrassed, eyes closed

kam "I-I mean, of course {i}you{/i} would think it's good! You wouldn't know talent if it fell into your backyard!"

kam "I-it's nothing {i}that{/i} special, alright?! It's just something I happened to pick up, that's all!"

yum "No, I'm serious. That was like a professional singing just now. You've got a singing voice that most people would only dream of having."

yum "If you really worked on that, I'm sure you'd have an amazing career ahead of you."

kam "Mmn..."

"You'd think she'd be delighted to get a compliment, but now she just looks frustrated."
"What is it with demons having these overtly specific hang-ups? I don't think I'll ever get it..."

#show kam sad

kam "It's not like that'll matter."

kam "No matter how hard I try, I'll never be as good as you want me to be."

yum "Huh? Why not?"

kam "..."

#show kam annoyed, eyes closed

kam "{i}Geez{/i}, why are we even talking about this?! You need to butt out of my business!"

if minion:
    jump trueloyalty
else:
    jump begtokamika

label angrykamika:
#BRANCH: use if went to see Stacey
#MEMO: write this!


#show kam annoyed

label trueloyalty:
#BRANCH: dialogue path based on not seeing stacey AND agreeing to be minion

kam "{i}You're{/i} the minion, and {i}I'm{/i} the mistress! I should {i}never{/i} have to divulge any of {i}my{/i} personal business to the likes of {i}you!{/i} Got it?!"

yum "Alright, I get it! Sorry for giving you a {i}compliment{/i}, Jesus..."

#show kam annoyed, eyes closed

kam "Humph! You'd {i}better{/i} be sorry! We can't have conversations like this distracting us from our {i}real{/i} goal!"

#show kam confident

kam "And {i}speaking{/i} of that, I've just finished preparing an itinerary for the first phase of our plan!"

"Well {i}finally{/i}, it looks like I'm getting somewhere with her."

yum "Well? What's the plan, then?"

kam "Finally! You're starting to show some initiative! Someone looking to prove herself to me!"

yum "Ugh..."

kam "Alright, come hither. We have {i}so much{/i} to discuss!~"

jump kamikapowerpoint


label begtokamika:
#if kamika wants you to beg (because you either went to see stacey, or didn't agree to be a minion, but not both)
kam "What was that, my little minion? I don't think I heard enough begging~"

yum "...Are you serious?"

kam "Oh, you think I was going to forgive you {i}that{/i} easily? You disappoint me so much..."

yum "What? I'm allowed to see other people. This is college. You're supposed to mingle."

yum "You have a problem with that? ...What am I saying, {i}of course you do{/i}."

kam "A good minion has eyes only for their empress! No one else!"

kam "If you want to get back into my good graces, you'll have to get on your knees and {i}beg{/i} to see the fruits of my labor!~"

"God {i}dammit{/i}, this fucking demon has to make {i}EVERYTHING{/i} a pain in the ass..."

"If I want to know anything about Kamika's plan, I might have to prostrate myself in front of her. Is it worth it...?"

menu:
    "Beg for forgiveness.":
        $ kamika_points += 1
        jump prostateyourself
    "Tell her off.":
        jump screwyoukamika

label prostateyourself:

"I clasp my hands together and give her a pleading look once more."

yum "Oh, {i}please{/i} forgive my impudence, mistress! I just wanna know {i}SO BADLY{/i} about your delightfully devilish ideas!"

#show kam laughing

kam "{i}Nyahahaha~!{/i} Well, with begging like that, who am I to leave my {i}favorite{/i} minion in the dark~?"

"Any more of this shit and I'm gonna have an aneurysm."
jump kamikapowerpoint

label screwyoukamika:
"Yeaaaah. Enough was enough. I'm not sacrificing my dignity for this self-entitled bitch."

kam "...Eh? Why're you standing up?"

yum "Okay. I'm done humoring you."

kam "What? What are you saying...?"

kam "...I-I mean, kneel, damn you!"
#MEMO: let's see what slike comes up with


#CG: show CG of Kamika showing Phase 1 Powerpoint presentation intro on a laptop

label kamikapowerpoint:
#BRANCH: if you agreed to help Kamika by begging or by being a TRUE LOYALIST
"Before long, Kamika puts together another presentation - again, using {i}my{/i} laptop - and proceeds to divulge her plan to me."

kam "Phase 1 of 'Kamika's Ultimate Plan for Worldwide Enrapture' is a simple task, but nonetheless extremely important!"

yum "Do you just sit around making PowerPoints all day? Don't you have {i}anything{/i} better to do with your time?"

kam "Th-that's neither here nor there, minion!"

kam "The events contained within will be the deciding factor in how the rest of the operation proceeds, so listen up and listen well!"

#CG: show next slide in CG, mediocre acrylic paint drawing of Kamika watching a singer

yum "Still using my art supplies, ugh. I don't even care anymore..."

kam "What I've learned from watching your world is that {i}anyone{/i} can be captivated by a good singer!"

kam "Singing has the power to bring together people from all over the world, and a good singer can enthrall the hearts of many with hardly any effort at all!"

yum "...So your plan is to become a professional singer? Isn't that what I just-"

kam "Are you interrupting me with a pointless diatribe yet again?"

yum "No, I just... you know what, nevermind. Go on."

kam "So {i}anyways{/i}, we need to draw together a crowd through singing, and {i}who{/i} is able to do that?"

yum "A professional diva?"

#CG: show next slide in CG, mediocre acrylic paint drawing of Kamika singing to an adoring crowd

kam "{i}Me{/i}, obviously!"

yum "Oh. I guess compromises have to be made..."

kam "There's no way the humans of this world will be able to resist the charming voice of an all-powerful succubus such as myself!"

kam "Once they hear me sing, they'll start tripping over themselves just to lose themselves to the sound of my voice~"

kam "And by the time I'm finished, I'll have amassed a crowd of followers who will just be {i}begging{/i} me to leave them in permanent enrapture~!"

kam "It'll be the {i}perfect{/i} way to start building my beautiful utopia!"

yum "Okay... And what'll you do after that? Do you even have a way to sing to a whole crowd in the first place?"

kam "Don't worry about the little details; I've got it all under control!"

"It sounds like such a simple plan, and that's what scares me the most."
"If she's able to use her singing as a means to convert an entire audience of people... there's no telling {i}what{/i} she might do after that."
"I mean. If she's able to. That's a {i}biiiiiiiiiig{/i} if."

#fade CG
#scene dormroom

#show kam confident

kam "We'll initiate the plan tomorrow as soon as possible! Don't be late!"

yum "Uh, if you want me as soon as possible, then you might want to wait until later in the day. We still have classes in the morning."

#show kam annoyed

kam "What, are you really so concerned with {i}those{/i} obligations? We're making {i}history{/i} here, you know!"

yum "I paid good money to move here and take classes, and I don't have the time to skip out on them for any of this."

yum "If you want my help, you're going to have to work around my schedule. That's just the way it is."

kam "...Very well. But I still expect you in my presence as {i}soon{/i} as you have some free time, understood?!"

yum "I got it, I got it."

"She acts as though she's exempt from being a student, too. If anything, she'll probably get kicked out long before her plans even succeed."

yum "Are we done for the day? I still have things to do."

kam "Not so fast! I have one more thing to bring up."

#show kam annoyed, eyes closed

kam "While you were on your little walk earlier, you didn't happen to be {i}cheating{/i} on me, didn't you?"

yum "...What?"

#show kam annoyed

kam "You know what I mean! Are you hiding a boyfriend from me? What about a {i}girlfriend{/i}, huh?"

kam "Were you conspiring with someone in secret instead of coming back to me as you should have?"

yum "What are you talking about? I haven't been 'conspiring in secret' with anyone!"

#show kam annoyed, eyes closed

kam "I'm just making sure we completely understand one another here. If you're going to be my minion, you must make my master plan your top priority!"

kam "That means I expect your presence before me at {i}all times!{/i} You must devote your existence {i}only{/i} to me!"

#show kam annoyed

kam "No exceptions. You are mine, and mine alone."

kam "If I see you with anyone else... our arrangement is over. Am I clear?"

"This intensity in her voice... she wouldn't hesitate to disassociate herself from me if I step out of line even once!"
"If I do go against her, it'll be that much harder to know what she's planning. That is, assuming she even {i}has{/i} anything else planned other than this."
"But I can't betray her trust now, not when I've come this far... I nod my head."

yum "Clear as crystal."

#show kam smiling

kam "Very good. Maybe I was right to trust you after all."

kam "Who knows? If things go well, I might just give you a kiss~"

yum "I'd rather get a kiss from a hooker than from {i}you.{/i}"

#show kam confident

kam "Hah! Insult me all you like, but you won't be saying that for much longer once everything is set in motion."

kam "Speaking of which, {i}I{/i} have to go make my final preparations for tomorrow."

kam "See you then, my dear~"

#hide kam

"Kamika disappears into my bedroom, giggling madly to herself."
"Against all the odds, I've gained enough of her favor for her to spill out her plan to me... but I feel as though she's not letting me in on what else she has in store."
"And if tomorrow's plan manages to succeed, who knows what that could mean for the student body?"
"I have to find a way to sabotage it... I won't allow Kamika to have her way with me {i}or{/i} this school!"
"I'll just have to wait for my opportunity. For now, I'd better focus on the things that I can do right now."
$ helpkamika = True
jump s7iiimerge

label spurnedkamika:
#BRANCH: dialogue path based on not helping kamika (either by refusing to beg OR by both not agreeing to be a minion and going to see stacey)

kam "And don't think for a second that you're getting on my good side! I {i}know{/i} you're trying to win me over after you spurned me so badly!"

kam "Well it's {i}not{/i} going to work! I can't have anyone be half-hearted about serving me; either they give themselves to me willingly, or I {i}make{/i} 'em serve me!"

#show kam annoyed

kam "So if you think I'm gonna let you take advantage of me like this, then you'd better get your head out of your ass {i}right now!{/i} Do I make myself clear?!"

yum "Alright, alright! Sorry for giving you a {i}compliment{/i}, Jesus..."

#hide kam

"Kamika storms off into my bedroom, not even acknowledging my last sentence."
"Well, that was utterly pointless. I thought maybe we'd reach some common ground, but she's still acting like a complete bitch."
"I really hope I can find a way to resolve all this... I don't think I have much time left."
"I just hope whatever Kamika has planned, it doesn't happen soon."
jump s7iiimerge
#MERGE: dialogue paths converge here

label s7iiimerge:
"I spend the rest of the night catching up on my anatomy homework, and without much else provocation from Kamika, I eventually turn in for the night."


jump scene8
