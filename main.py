from wfc import Rule, Wave, State
import colorama


air = State(
    "air",
    Rule(
        lambda x, y : {
            (x, y+1): ["air"]
        }
    )
)

grass = State(
    "grass",
    Rule(
        lambda x, y : {
            (x, y-1): ["dirt"],
            (x, y+1): ["air"]
        }
    )
)

dirt = State(
    "dirt",
    Rule(
        lambda x, y: {
            (x, y+1): ["dirt", "grass"],
            (x, y-1): ["stone", "dirt"]
        }
    )
)

stone = State("stone",
    Rule(
        lambda x, y : {
            (x, y+1): ["stone", "dirt"]
        }
    )
)

landscape = Wave(
    (40, 10),
    [air, grass, dirt, stone]
)

landed = landscape.collapse()

cmap = {
    "air": colorama.Fore.WHITE,
    "grass": colorama.Fore.GREEN,
    "dirt": colorama.Fore.YELLOW,
    "stone": colorama.Fore.BLACK
}

for row in landed:
    for item in row:
        print(cmap[item.state.name] + "█" + colorama.Fore.RESET, end="")
    print()
