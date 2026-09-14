define p = Character("Pico", color="#c8ffc8")
define s = Character("Skullcat", color="#c8c8ff")

label start:

    jump chapter_4

    label chapter_1:
        window hide

        scene black with None

        pause 1.5

        scene bus stop evening with Dissolve(1.5)

        play music "audio/songs/town.mp3"

        show pico neutral right with dissolve

        window show

        p "Ugh, my face hurts."

        "The doors to the train close as I open the sliding door to the cabin."

        "Moving up the stairs, I walk all the way down the aisle to my usual seat"
        
        "I settle into the familiar leather seat and sigh with relief."

        p "Almost home, I'm starving."

        hide pico with fade

        "Leaning into my seat, I watch as the station starts to move, and the train begins to depart"

        "The rhythmic sound of the train on the tracks lulls me into a sense of calm."

        "The city buildings start to zoom by as the train picks up speed, the tracks screeching, and the train car clattering"

        "It's a Friday, and the train is packed with people heading home after a long week of work."

        "Teenagers are laughing and joking, while businesspeople are conversting, some enjoying a beverage in hand after a long week."
        
        p "Well..."
        
        p "It won't be too long before I get home"
    
    label chapter_2:
        scene park night:
            xsize config.screen_width
            ysize config.screen_height
        with dissolve

        play music "audio/songs/journey.mp3"
        
        "Hopping off the train, I make my way to my car"
        
        "*Beep* *Beep*"
        
        "*Car noise*"
        
        p "Well let's head home"
        
        "*Car zooms away*"
        
        p "Let's pick something up for Skullcat"
        
        "I drive to the the Bunkin Bonuts"
        
        p "Hi, can I get a Matcha Oreo Latte please?"
        
        "That'll be 14 Beeblebrox schmeckles please"
        
        p "Yep"
        
        "*Beep*"
        
        "I grab the drink. Skullcat always loves their funky drinks"
        
        "I speed away heading for home"

    label chapter_3:
        scene condo kitchen:
            xsize config.screen_width
            ysize config.screen_height
        with dissolve

        play music "audio/songs/start.mp3"
        
        p "Finally made it"
        
        "I hear clattering of dishes and pots in the kitchen."
        
        p "They must have not heard me walk in"
        
        "I slowly walk towards the kitchen, Skullcat's undead body occupying the space at the sink"

        show skullcat neutral with fade

        "Their tail, furry and ends with their tail bones sticking out, swishes back in forth as they're preoccupied"
        
        "They don't hear me as I get closer and closer"

        show skullcat at right
        
        show pico neutral right at left
        with fade

        "I get right behind them. They're concentrating on the dishes."
        
        "Their hands bubbly and they're humming a tune"
        
        "My hands hover around their waist, and I gently grab them"

        s "WAHHHHHH!"

        show skullcat neutral left at right

        "Their body jolts and their head shoots into the air with a rattling sound."

        "Their tail straightens, fur sticking out and sharp"

        "Water splashes from the dishes being dropped into the sink"

        "Skull cat's head falls into their hands and juggles it a little before settling it in the arms"

        "With a huff, they tilt their head towards me"

        s "YOU SCARED ME!"

        "I hold their arms to steady them as they settle down"

        p "Haha sorry about that, I couldn't resist"

        p "Are you okay?"

        s "Yeah, I'm fine. Just a little startled, that's all."

        p "Ohh, well, I wanted too surprise you with a drink I got for you"

        "I hold out the drink I got from the Bunkin Bonuts"

        s "Oh, thanks! You got my favorite!"

        p "No problem, I know how much you love your funky drinks"

        "They wipe their hands on the cloth and take the drink from me, taking a sip"

        s "Oh yeah, that hit the spot! Thanks again, Pico."

    label chapter_4:

        scene condo:
            xsize config.screen_width
            ysize config.screen_height
        with dissolve

        show skullcat neutral with dissolve
        
        play music "audio/songs/regrowth.mp3"

        call skullcat_interaction

        p "I have this thing I have to do, but I'll see you later."

        s "Okay, go do that thing then. I'll be here when you get back."

        return

label skullcat_interaction:
    call question_menu

label question_menu:
    menu:
        "How was your day?":
            jump how_was_your_day
        "What are you doing?":
            jump what_are_you_doing
        "Do you want to go out?":
            jump do_you_want_to_go_out
        "I have to go now.":
            return

label how_was_your_day:
    p "How was your day?"

    s "It was good, I had a lot of fun at work today."

    p "That's great to hear!"

    jump skullcat_interaction

label what_are_you_doing:
    p "What are you doing?"

    s "I'm just washing the dishes, it's a bit of a chore but it needs to be done."

    p "I understand, chores can be tedious."

    jump skullcat_interaction

label do_you_want_to_go_out:
    p "Do you want to go out?"

    s "Sure, that sounds like a great idea! Where do you want to go?"

    p "How about we go to the park and have a picnic?"

    s "That sounds perfect! Let's do it."

    jump skullcat_interaction