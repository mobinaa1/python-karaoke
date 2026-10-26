import os
import time
print ("music is playing...")
os.startfile("music.mp3")
lyrics = [
    (" ","💑🎧",16),
    ("we can remember....swimming in december","🏊‍♀️❄💙",9),
    ("Heading for the city lights...in 1975","🎞🍿",7),
    ("we share in each other","👂🥰",4),
    ("nearer than Farther","😉",4),
    ("the scent of a lemon... drips from your EeEeEeeyes","🍋👀",8),
    ("we are the people that rule the world","👶🏻👧🏾🧑🏻🧓🏻👴🏽🌎",4),
    ("a force running in every boy and girl","🔁👱🏼‍️👩🏻",4),
    ("all rejoicing in the world take me now","💃🏻🕺🏻🎆",6),
    ("we can try","😉",2),
    ("we lived an adventure","🎒🌄",4),
    ("LOVE in the SUMMER","💑🔥",4),
    ("following the sun till night","🌙🚶🏽☀️🚶",3),
    ("reminiscing other times of life","⏰",5),
    ("for each every other","😶",4),
    ("the feeling was stronger","❤💪🏼",4),
    ("the shock hit eleven","😮",3),
    ("Got lost in your EeEeeys.... i can`t do well when i think you`re gonna leave me but i kow i try","🥺💔🙃🙂",10),
    ("are you gonna leave me now","😔",4),
    ("can`t you be believing now","😞",5),
    ("i can`t do well when i think you`re gonna leave me but i kow i try","🥺💔🙃🙂",7),
    ("are you gonna leave me now","😔",4),
    ("can`t you be believing now","😞",6),
    ("can you remember and humanize","🤝🏼🤔",4),
    ("it was still where we`d energized","⚡🔋",4),
    ("lie in the sand and visualize","⛱👙",3),
    ("like it`s 75 again","⌛❣",5)]
for line, emoji,delay in lyrics:
    print(f"{line} {emoji}")
    time.sleep(delay)
print("lyrics finished!Enjoy the rest of the song✨😊✨")


