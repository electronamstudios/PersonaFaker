import os
from thispersondoesnotexist import get_online_person
from thispersondoesnotexist import save_picture

final = "0"
number = "0"

class OperatingSystem:
    def linux():
        os.mkdir("/tmp/PersonaFaker/Pictures")
        def num_math():
            global final 
            global number

            final = int(number) + 1
            number = final

            final = str(final)
            number = str(number)

        num_math()

        picture = get_online_person()
        path = "/tmp/PersonaFaker/Pictures" + final + ".jpeg"

        save_picture(picture, path)
        print("\n     Saved File To", path,"\n")
    def windows():
        os.mkdir("C:/tmp/PersonaFaker/Pictures")