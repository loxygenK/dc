from colored import fg, bg, attr

def question(message, override=False):
    terminate = "\n" if len(message) > 30 else ""
    mes = message.replace("\n", "\n    ")
    print_with_tag("?", mes, "yellow_1", terminate)

    read = input()

    print(f"\033[1A\033[0G{fg('grey_46')}", end="")
    if override:
        print("\033[2KLoaded (Input has been hided)")
    else:
        print(f"{read} (Read)")
    print(attr('reset'), end="")

    return read


def log(message):
    print_with_tag(" ", message, "light_steel_blue")


def fatal(message):
    print_with_tag("!", message, "orange_red_1")


def success(message):
    print_with_tag("✓", message, "chartreuse_3a")


def print_with_tag(tag_char, message, color, end="\n"):
    print(
        f"{fg(color)}{attr('bold')}[{tag_char}]{attr('reset')}"
        f"{fg(color)} {message}{attr('reset')}", end=end
    )
