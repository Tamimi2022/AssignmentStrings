# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1 / 1
scored_0 = "Ruud Gullit"
scored_1 = "Marco van Basten"

# Part 1 / 2
goal_0 = 32
goal_1 = 54

# Part 1 / 3
scorers = scored_0 + " " + str(goal_0) + ", " + scored_1 + " " + str(goal_1)
print(scorers)

# Part 1 / 4
report = f"{scored_0} scored in the {goal_0}nd minute\n{scored_1} scored in the {goal_1}th minute"
print(report)

# Part 2 / 1
player = "Diego adona"
print(player)

# Part 2 / 2
first_name = player[:player.find(" ")]
print(first_name)

# Part 2 / 3
last_name_len = len(player[-player.find(" "):])
print(last_name_len)

# Part 2 / 4
name_short = player[:player.find(" ")].upper()[:1] + ". " + player[-player.find(" "):]
print(name_short)

# Part 2 / 5
chant = ((player[:player.find(" ")] + "! ") * len(player[:player.find(" ")])).strip()
print(chant)

# Part 2 / 6
good_chant = chant != 3
print(good_chant)