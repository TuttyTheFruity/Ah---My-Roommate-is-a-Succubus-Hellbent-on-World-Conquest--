label scene13:
scene classroom

#fade in from black, classroom
voice "c-13-1.mp3" #Mister Deeks (???)
dee "-And that is why the so called \"anime\" style is nothing more than an amalgamation of poor techniques that should not, under any circumstances, be the only thing you practice."

voice "c-13-2.mp3" #Mister Deeks (???)
dee "That's not to say it is a terrible medium on it's own, just that you should be improving far beyond what the style demands of you before you set such a limitation on yourself."

voice "c-13-3.mp3" #Mister Deeks (???)
dee "Class dismissed!"

#POINT CHECK: IF insufficient points for any route; BAD END
if stacey_points > 0:
    jump s13continue
elif lucca_points > 0:
    jump s13continue
elif kamika_points = 3:
    jump s13continue
else:
    jump hermitend

label hermitend:
"Another day, another dreadful class."
"I wish I could say that's the only unpleasant thing going on in my life."
"Too many people, too much drama, all of it absurd."
"Though, I suppose it's not so bad."
"...Whatever, I should just focus on preparing for the next class."
jump scene14iv


#IF sufficient points for any route; continue scene

label s13continue:
voice "c-13-4.mp3" #Yumi (Kathy Pfautsch)
yum "I can't believe he spent almost an entire hour talking about children's shows."

voice "c-13-5.mp3" #Stacey (Ashe Thurman)
sta "Maybe he just hasn't researched enough."

voice "c-13-6.mp3" #Yumi (Kathy Pfautsch)
yum "Does he look like the kind of guy who watches, let alone researches, anime?"

voice "c-13-7.mp3" #Stacey (Ashe Thurman)
sta "He seemed to like that Bobo's Strange Journey show a lot."

voice "c-13-8.mp3" #Yumi (Kathy Pfautsch)
yum "Good taste."

voice "c-13-9.mp3" #Stacey (Ashe Thurman)
sta "So, how are things on the roommate front? She suck your soul out yet?"

voice "c-13-10.mp3" #Yumi (Kathy Pfautsch)
yum "That girl couldn't drain a juice box, let alone a soul."

voice "c-13-11.mp3" #Stacey (Ashe Thurman)
sta "You think? I mean, her lungs should be strong enough."

voice "c-13-12.mp3" #Yumi (Kathy Pfautsch)
yum "That's not what I me- ya know what, you're right."

voice "c-13-13.mp3" #Yumi (Kathy Pfautsch)
yum "It's strange, for a demon she's rather... What's the word for it...?"

voice "c-13-14.mp3" #Stacey (Ashe Thurman)
sta "Sucky?"

voice "c-13-15.mp3" #Yumi (Kathy Pfautsch)
yum "Feels too literal. I wanna say \"naive\" but that seems contradictory somehow."

voice "c-13-16.mp3" #Stacey (Ashe Thurman)
sta "I'd say she's beyond classification then."

voice "c-13-17.mp3" #Yumi (Kathy Pfautsch)
yum "Really? Aren't you, like, the expert when it comes to demons?"

voice "c-13-18.mp3" #Stacey (Ashe Thurman)
sta "Don't know what to tell you, friend. Moe is a pretty standard dude."

voice "c-13-19.mp3" #Yumi (Kathy Pfautsch)
yum "Standard dude or standard demon?"

voice "c-13-20.mp3" #Stacey (Ashe Thurman)
sta "Same shit TBH, fam."

voice "c-13-21.mp3" #Stacey (Ashe Thurman)
sta "One time I went over to his room and there was this huge racket you could hear all the way from the hall."

voice "c-13-22.mp3" #Stacey (Ashe Thurman)
sta "When I knocked on his door, the sound suddenly stopped. When he finally answered, a minute and a half later, I asked him about it."

voice "c-13-23.mp3" #Stacey (Ashe Thurman)
sta "He started shaking and spouting off something about a bug infestation."

voice "c-13-24.mp3" #Stacey (Ashe Thurman)
sta "Very convenient he had a box of tissues by his computer, 'just in case'."

voice "c-13-25.mp3" #Yumi (Kathy Pfautsch)
yum "Damn, he really is normal."

voice "c-13-26.mp3" #Stacey (Ashe Thurman)
sta "Shocking, I know."

#variable lucca name = ???

voice "c-13-27.mp3" #Lucca (Victoria Wong)
luc "I h-hope I'm not interrupting anything..."

voice "c-13-28.mp3" #Yumi (Kathy Pfautsch)
yum "Oh, hey Lucca."

voice "c-13-29.mp3" #Stacey (Ashe Thurman)
sta "Yumi, you know the cowgirl?"

voice "c-13-30.mp3" #Yumi (Kathy Pfautsch)
yum "We go way back, she's another demon, sort of."

voice "c-13-31.mp3" #Lucca (Victoria Wong)
luc "I'm right here, you know!"

voice "c-13-32.mp3" #Yumi (Kathy Pfautsch)
yum "Don't mind her, she's friendly."

voice "c-13-33.mp3" #Stacey (Ashe Thurman)
sta "Are you sure? I hear you're not supposed to trust demons in funny hats."

voice "c-13-34.mp3" #Yumi (Kathy Pfautsch)
yum "I was talking about you and your funny hat, actually."

voice "c-13-35.mp3" #Lucca (Victoria Wong)
luc "I-I'll have you know this hat is fashionable and f-functional..."

voice "c-13-36.mp3" #Stacey (Ashe Thurman)
sta "I bet there's a big ol' horn under there. Like a unicorn. Majestic and aerodynamic."

voice "c-13-37.mp3" #Lucca (Victoria Wong)
luc "W-what!? N-No!"

"Stacey takes a good, hard look at Lucca's hat, carefully weighing the possibilities."

voice "c-13-38.mp3" #Stacey (Ashe Thurman)
sta "..."

voice "c-13-39.mp3" #Lucca (Victoria Wong)
luc "I-It's rude to stare..."

voice "c-13-40.mp3" #Stacey (Ashe Thurman)
sta "Okay, I believe you."

voice "c-13-41.mp3" #Yumi (Kathy Pfautsch)
yum "What."

voice "c-13-42.mp3" #Stacey (Ashe Thurman)
sta "If she says there isn't a horn, there isn't one."

voice "c-13-43.mp3" #Yumi (Kathy Pfautsch)
yum "Anyway..."

voice "c-13-44.mp3" #Lucca (Victoria Wong)
luc "Yumi, I have to talk to you. I-In private. Are you free?"

if kamika_points = 3:
    jump kamikaroute
elif stacey_points > lucca_points:
    jump staceyroute
elif lucca_points > stacey_points:
    jump luccaroute
else:
    jump tiebreaker

#IF equal LUCCA and STACEY points

label tiebreaker:
"Oh, shit. I promised both of them I'd help out today. Quick, make something up!"

menu:
    "Go with Stacey":
        voice "c-13-45.mp3" #Yumi (Kathy Pfautsch)
        yum "Sorry Lucca, I already made plans. Can it wait?"

        voice "c-13-46.mp3" #Lucca (Victoria Wong)
        luc "...I-I guess..."
        jump staceyroute
    "Go with Lucca":
        voice "c-13-47.mp3" #Yumi (Kathy Pfautsch)
        yum "Oh crap. Stacey, I'm gonna hafta cancel."

        voice "c-13-48.mp3" #Stacey (Ashe Thurman)
        sta "Eh? But, you promised..."

        voice "c-13-49.mp3" #Yumi (Kathy Pfautsch)
        yum "I know, but this concerns a certain demon with an ego. I'm sorry!"

        voice "c-13-50.mp3" #Stacey (Ashe Thurman)
        sta "It's cool, I guess... Writing is a lonely task anyway."

        voice "c-13-51.mp3" #Stacey (Ashe Thurman)
        sta "Go, lay the demon!"

        voice "c-13-52.mp3" #Lucca (Victoria Wong)
        luc "Do you mean \"Slay\"?"

        voice "c-13-53.mp3" #Stacey (Ashe Thurman)
        sta "Close enough."
        jump luccaroute


label staceyroute:

$ route = "stacey"
voice "c-13-54.mp3" #Yumi (Kathy Pfautsch)
yum "I would, but I promised Stacey."

voice "c-13-55.mp3" #Lucca (Victoria Wong)
luc "Not the issue here, but okay."

voice "c-13-56.mp3" #Stacey (Ashe Thurman)
sta "C'mon, let's go somewhere else for this."

jump scene14i


label luccaroute:

$ route = "lucca"
voice "c-13-57.mp3" #Yumi (Kathy Pfautsch)
yum "I'll talk to you later, Stacey."

voice "c-13-58.mp3" #Stacey (Ashe Thurman)
sta "Take it easy, Yumi."

voice "c-13-59.mp3" #Lucca (Victoria Wong)
luc "A-Alright, let's go!"

jump scene14ii


label kamikaroute:

$ route = "kamika"
voice "c-13-60.mp3" #Yumi (Kathy Pfautsch)
yum "...Sorry, guys. I just can't sit still knowing Kamika might be up to {i}something{/i}."

voice "c-13-61.mp3" #Yumi (Kathy Pfautsch)
yum "I'm gonna have to go and check up on her. I'll call you guys if anything major's happening."

voice "c-13-62.mp3" #Stacey (Ashe Thurman)
sta "You're the boss, boss. Do whatcha gotta do."

voice "c-13-63.mp3" #Lucca (Victoria Wong)
luc "B-be careful, Yumi..."

voice "c-13-64.mp3" #Yumi (Kathy Pfautsch)
yum "I'll be back soon. Hopefully."

"With trepidation in my heart, I make my way back to the dorms."

jump scene14iii
