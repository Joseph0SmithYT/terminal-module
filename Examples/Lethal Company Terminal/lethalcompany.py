import terminal as terminalpkg
terminal = terminalpkg.CustomTerminal()

from moon import Moon

@terminal.register_command('moons', 'Displays all moons.', required=False)
def moons(moon_name):
    experimentation = Moon("Experimentation", "B", 
             "Arid. Low habitability, worsened by industrial artifacts."\
             , "Unknown.")
    assurance = Moon("Assurance", "D",
                     "Similar to its twin moon, 41-Experimentation, featuring far more jagged and weathered terrain.",)
    vow = Moon("Vow", "C", 
               "Humid.", "Diverse, teeming with plant-life.")
    offense = Moon("Offense", "B",
                   "Believed to have splintered off from its cousin Assurance, Offense features similar\
                      jagged and dry conditions but differs in its ecosystem.",
                      "A competitive and toughened ecosystem supports aggressive lifeforms. Travellers \
                        to 21-Offense should know it's not for the faint of heart.")
    march = Moon("March", "B",
                 "March undergoes constant drizzling weather. Its terrain is more expansive.")
    rend = Moon("Rend", "A", 
                "Its planet orbits white dwarf star, making for inhospitable, cold conditions. Constant blizzards decrease visibility.",
                "It's highly unlikely for complex life to exist here.", 550)
    dine = Moon("Dine", "S", 
                "Its planet orbits white dwarf star, making for inhospitable, cold conditions. Constant blizzards decrease visibility.",
                "It's highly unlikely for complex life to exist here.", 600)
    titan = Moon("Titan", "S+",
                "A flat, frozen landscape.", 
                "Dangerous entities have been rumored to take residence in the vast network of tunnels.", 700)
    moons = {"experimentation": experimentation,
             "assurance": assurance,
             "vow": vow,
             "offense": offense,
             "march": march,
             "rend": rend,
             "dine": dine,
             "titan": titan
             }
    if moon_name == None:
        for moon in moons:
            print(f"{moons[moon].name}")
    elif not moon_name == None:
        if not moon_name in moons:
            for moon in moons:
                print(f"{moons[moon].name}")
        else:
            print(f"{moons[moon_name].name}\n{moons[moon_name].description}\n")

terminal.start()