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
    print("user said 'countdown'")
    return True
  if "there's a bee in the sea"  in user_message:
    return True
  if "to the right to the right to the right to the right"  in user_message:
    return True
  if "backward"  in user_message:
    return True
  if "joke"  in user_message:
    return True
  if "one two three, eyes on me"  in user_message:
    return True
  if "slim shady"  in user_message:
    return True
  if "z"  in user_message:
    return True
  if "ocean" in user_message or "sea" in user_message or "shark"  in user_message:
    return True
  if "duck"  in user_message:
    return True
  if "a" in user_message or "e" in user_message or "i" in user_message or "o" in user_message or "u" in user_message:
    return True
  if "die" in user_message or "dice" in user_message:
    return True
  if "capitalize" in user_message:
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
  if "joke"  in user_message:
    pass
  if "one two three, eyes on me"  in user_message:
    return "one, two, eyes on you!"
  if "slim shady"  in user_message:
    return "please stand up"
  if "z"  in user_message:
    pass
  if "ocean" in user_message or "sea"  in user_message or "shark"  in user_message:
    return "baby shark doodoodoodoodoodoo, baby shark doodoodoodoodoodoo, baby shark doodoodoodoodoodoo, baby shark!"
  if "duck"  in user_message:
    return "got any grapes?"
  if "a"  in user_message  or "e" in user_message or "i"  in user_message or "o"  in user_message or "u"  in user_message:
    pass
  if "capitalize" in user_message:
    state = "waiting_for_message_to_capitalize"
    return "What do you want me to capitalize?"
  if state == "waiting_for_message_to_capitalize":
    capital_message = user_message.upper()
    state = "start"
    return capital_message

  
  else:
    return False


# Proposal