import phonenumbers, argparse  
from phonenumbers import carrier, geocoder, timezone

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

parse = argparse.ArgumentParser("Ingrese un numero de telefono con el codigo del pais. Ejemplo: -n +9997354128")
parse.add_argument('-n', '--number', help="Numero de telefono")
parse = parse.parse_args()

try:
    if parse.number:

        banner = """
    ‏  ⡔⠙⠢⡀   ⢀⠼⠅⠈⢂⠄     _______   __    __   ______   __    __  ________ 
    ‏  ⡌⠄⢰⠉⢙⢗⣲⡖⡋⢐⡺⡄⠈⢆   /       \ /  |  /  | /      \ /  \  /  |/        |
    ‏ ⡜⠄⢀⠆⢠⣿⣿⣿⣿⢡⢣⢿⡱⡀⠈⠆  $$$$$$$  |$$ |  $$ |/$$$$$$  |$$  \ $$ |$$$$$$$$/ 
    ‏ ⠧⠤⠂⠄⣼⢧⢻⣿⣿⣞⢸⣮⠳⣕⢤⡆  $$ |__$$ |$$ |__$$ |$$ |  $$ |$$$  \$$ |$$ |__    
    ‏⢺⣿⣿⣶⣦⡇⡌⣰⣍⠚⢿⠄⢩⣧⠉⢷⡇  $$    $$/ $$    $$ |$$ |  $$ |$$$$  $$ |$$    |   
    ‏⠘⣿⣿⣯⡙⣧⢎⢨⣶⣶⣶⣶⢸⣼⡻⡎⡇  $$$$$$$/  $$$$$$$$ |$$ |  $$ |$$ $$ $$ |$$$$$/    
    ‏ ⠘⣿⣿⣷⡀⠎⡮⡙⠶⠟⣫⣶⠛⠧⠁   $$ |      $$ |  $$ |$$ \__$$ |$$ |$$$$ |$$ |_____ 
    ‏   ⠈⢿⣿⣿⣿⣿⣷⣯⣿⣿⣷⣾⣿⣷⡄ $$/       $$/   $$/  $$$$$$/  $$/   $$/ $$$$$$$$/ 
    ‏      ⢻⠏⣼⣿⣿⣿⣿⡿⣿⣿⣏⢾⠇   _______    ______   __    __  __    __
    ‏      ⠈⡼⠿⠿⢿⣿⣦⡝⣿⣿⣿⠷⢀  /       \  /      \ /  |  /  |/  |  /  |          
    ‏       ⡇   ⠈⠻⠇⠿⠋  ⢘⡆ $$$$$$$  |/$$$$$$  |$$ |  $$ |$$ |  $$ |          
    ‏       ⠱⣀   ⣀⢼⡀ ⢀⣀⡜  $$ |  $$ |$$ |  $$ |$$  \/$$/ $$  \/$$/           
    ‏       ⢸        ⢏⠁   $$ |  $$ |$$ |  $$ | $$  $$<   $$  $$<            
    ‏      ⡰⠃     ⢸  ⢸⣧   $$ |  $$ |$$ |  $$ |  $$$$  \   $$$$  \           
    ‏     ⣼⣧      ⣼  ⡘⣿⡆  $$ |__$$ |$$ \__$$ | $$ /$$  | $$ /$$  |          
    ‏   ⢀⣼⣿⡙⣷⡄    ⠃ ⢠⣿⢸⣿⡀ $$    $$/ $$    $$/ $$ |  $$ |$$ |  $$ |          
    ‏  ⢀⣾⣿⣿⣷⣝⠿     ⢀⡞⢍⣼⣿⠇ $$$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/  
    ‏  ⣼⣿⣿⣿⣿⣿⣷⣄  ⠠⡊⠴⠋⠹⡜  
    ‏  ⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠀  BY: Alcatraz2033⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """
        print(GREEN + banner + RESET)

        parse.number = phonenumbers.parse(parse.number)
        hora = timezone.time_zones_for_number(parse.number)
        operadora = carrier.name_for_number(parse.number, "es")
        pais = geocoder.description_for_number(parse.number, "es")
        n_valido = phonenumbers.is_valid_number(parse.number)
        n_existe = phonenumbers.is_possible_number(parse.number)
        print(CYAN + "Zona horaria: " + RESET, hora[0])
        print(CYAN + "Operadora: " + RESET, operadora)
        print(CYAN + "Pais: " + RESET, pais)
        if n_valido:
            print(CYAN + "El numero es valido: " + RESET, "SI")
        else:
            print(CYAN + "El numero es valido: " + RESET, "NO")
        if n_existe:
            print(CYAN + "Posibilidad que el numero exista: " + RESET, "SI")
        else:
            print(CYAN + "Posibilidad que el numero exista: " + RESET, "NO")
    else:
        print(CYAN + "\nUsage: python3 phone.py -n <Numero de telefono mas codigo del país>\nEjemplo: python3 phone.py -n +9997354128")
        print(RED + "[!] No ha ingresado un numero de telefono")
except Exception as e:
    print(RED + "[!] La cadena proporcionada no parecía ser un número de teléfono.")
