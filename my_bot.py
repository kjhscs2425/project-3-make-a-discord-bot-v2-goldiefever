import random
state = "start"
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "" in user_message:
    return True
  if "countdown"  in user_message:
    return True
  if "there's a bee in the sea"  in user_message:
    return True
  if "to the right to the right to the right to the right"  in user_message:
    return True
  if "backward"  in user_message:
    return True
  if "one two three, eyes on me"  in user_message:
    return True
  if "slim shady"  in user_message:
    return True
  if "ocean" in user_message or "sea" in user_message or "shark"  in user_message:
    return True
  if "duck"  in user_message:
    return True
  if "die" in user_message or "dice" in user_message:
    return True
  if "capitalize" in user_message:
    return True
  if "pick a card" in user_message:
    return True
  if "sarcastic" in user_message:
    return True
  if "a" in user_message or "e" in user_message or "i" in user_message or "o" in user_message or "u" in user_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global state
  # if "" in user_message:
    
  if "countdown"  in user_message:
    state = "waiting_for_countdown_number"
    return "What do you want me to countdown from?"
  if state == "waiting_for_countdown_number":
    countdown_number = int(user_message)
    output_message = ""
    for i in range (countdown_number):
      output_message += f"{countdown_number-i}"
    output_message += " blastoff!"
    state = "start"
    return output_message
  if "there's a bee in the sea"  in user_message:
    return "adee adee, holy macaroni"
  if "to the right to the right to the right to the right"  in user_message:
    return "to the left to the left to the left to the left, now kick now kick now kick now kick, now walk it by yourself now walk it by yourself"
  if "backward"  in user_message:
    state = "waiting_for_backwards_message"
    return "What do you want me to say backwards?"
  if state == "waiting_for_backwards_message":
    backwards_message = user_message
    output_message = ""
    for i in range (len(backwards_message)):
      output_message += backwards_message[-1-i]
    state = "start"
    return output_message
  if "one two three, eyes on me"  in user_message:
    return "one, two, eyes on you!"
  if "slim shady"  in user_message:
    return "please stand up"
  if "ocean" in user_message or "sea"  in user_message or "shark"  in user_message:
    return "baby shark doodoodoodoodoodoo, baby shark doodoodoodoodoodoo, baby shark doodoodoodoodoodoo, baby shark!"
  if "duck"  in user_message:
    return "got any grapes?"
  if "die" in user_message or "dice" in user_message:
    state = "waiting_for_side_number"
    return "How many sides you want on the die roll?"
  if state == "waiting_for_side_number":
    side_number = int(user_message)
    output_message = random.randint(1,side_number)
    state = "start"
    return output_message
  if "capitalize" in user_message:
    state = "waiting_for_message_to_capitalize"
    return "What do you want me to capitalize?"
  if state == "waiting_for_message_to_capitalize":
    capital_message = user_message.upper()
    state = "start"
    return capital_message
  if "pick a card" in user_message:
    suit = ["clubs", "diamonds", "hearts", "spades"]
    number = ["ace",2,3,4,5,6,7,8,9,10,"jack","queen","king"]
    return f"{random.choice(number)} of {random.choice(suit)}"
  if "sarcastic" in user_message:
    state = "waiting_for_sarcastic_message"
    return "What do you want me to say sarcastically?"
  if state == "waiting_for_sarcastic_message":
    text = user_message
    text = text.replace("a", "A")
    text = text.replace("e", "E")
    text = text.replace("i", "I")
    text = text.replace("o", "O")
    text = text.replace("u", "U")
    state = "start"
    return text

  if "a"  in user_message  or "e" in user_message or "i"  in user_message or "o"  in user_message or "u"  in user_message:
    counter_a = 0
    counter_e = 0
    counter_i = 0
    counter_o = 0
    counter_u = 0
    for letter in user_message:
      if letter == "a":
        counter_a += 1
      if letter == "e":
        counter_e += 1
      if letter == "i":
        counter_i += 1
      if letter == "o":
        counter_o += 1
      if letter == "u":
        counter_u += 1
    vowels = [counter_a, counter_e, counter_i, counter_o, counter_u]
    max_value = max(vowels)
    if counter_a == max_value:
      return "A lake tay ayt ayt ayt ayples aynd baynaynays"
    if counter_e == max_value:
      return "EE leeke tee eet eet eet eeples eend beeneenees"
    if counter_i == max_value:
      return "I like tie iet iet iet ieples iend bienienies"
    if counter_o == max_value:
      return "O loke toe oet oet oet oeples oend boenoenoes"
    if counter_u == max_value:
      return "OO looke too oot oot oot ooples oond boonoonoos"
    return
  else:
    return False