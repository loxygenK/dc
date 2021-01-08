from colored import fg, bg, attr

def question(message, override=False):
    terminate = "\n" if len(message) > 30 else ""
    mes = message.replace("\n", "\n    ")
    print_with_tag("?", message, "yellow_1", terminate)

    read = input()

    print(f"\033[1A\033[0G{fg('grey_46')}", end="")
    if override:
        print("\033[2KLoaded (Input has been hided)")
    else:
        print(f"{read} (Read)")
    print(attr('reset'), end="")

    return read


def success(message):
    print_with_tag("✓", message, "chartreuse_3a")


def print_with_tag(tag_char, message, color, end="\n"):
    print(
        f"{fg(color)}{attr('bold')}[{tag_char}]{attr('reset')}"
        f"{fg(color)} {message}{attr('reset')}", end=end
    )
