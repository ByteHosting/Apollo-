import os
import pythowo

def red(text):
    return f"\033[91m{text}\033[0m"


print(red("""
 .d8b.  d8888b.  .d88b.  db      db       .d88b.  
d8' `8b 88  `8D .8P  Y8. 88      88      .8P  Y8. 
88ooo88 88oodD' 88    88 88      88      88    88 
88~~~88 88~~~   88    88 88      88      88    88 
88   88 88      `8b  d8' 88booo. 88booo. `8b  d8' 
YP   YP 88       `Y88P'  Y88888P Y88888P  `Y88P'

"""))
def Apollo_Shell():
    while True:
        user_input = input("Apollo 1.12 > ")
        if user_input.lower() == "hello":
            print("Hello, world!")
        elif user_input.lower() == "exit":
            break
        elif user_input.lower() == "apollo -h":
            print("help is here")
        elif user_input.strip() == "cwear":
            os.system('clear' if os.name == 'posix' else 'cls')
        elif user_input.strip() == "":
            continue
        else:
            result, error = pythowo.run("<stdin>", user_input)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))
            else:
                print("Unknown command. Type 'exit' to quit.")

if __name__ == "__main__":
    Apollo_Shell()

