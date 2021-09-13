#https://www.reddit.com/r/dailyprogrammer/comments/3xpgj8/20151221_challenge_246_easy_xmass_lights/

def max_leds(volt_led, cur_led, volt_bat, bat_capacity, hours):
    return int(bat_capacity / (hours * cur_led)) * int(volt_bat // volt_led)

def scheme (volt_led, cur_led, volt_bat, bat_capacity, hours):
    led = "-|>-"
    max_line = int(volt_bat // volt_led)
    num_in_parallel = int(max_leds(volt_led, cur_led, volt_bat, bat_capacity, hours) / max_line)
    scheme = "*"
    for i in range(max_line):
        scheme += "-" + led
    scheme += "-*"
    scheme = new_parallel(scheme)

    for i in range(num_in_parallel - 1):
        scheme += " " + ("-" + led) * max_line + '-'
        if (i + 1) < (num_in_parallel - 1):
            scheme = new_parallel(scheme)

    return scheme

def resistance(bat_capacity, hours):
    return round(0.5 / (bat_capacity / 100) / hours, 3)

def final(volt_led, cur_led, volt_bat, bat_capacity, hours):
    print("Resistor: " + str(resistance(bat_capacity, hours)), "Ohms")
    print("Scheme:\n" + str(scheme(volt_led, cur_led, volt_bat, bat_capacity, hours)))

def new_parallel(curr_scheme):
    return curr_scheme + "\n|" + ' ' * 26 + "|\n"

#Test case:
final(1.7, 20, 9, 1200, 20)