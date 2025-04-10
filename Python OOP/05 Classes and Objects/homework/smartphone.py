class Smartphone:
    def __init__(self, memory:int):
        self.memory = memory    # phone memory
        self.apps = []
        self.is_on = False

    def power(self):
        """
        power off the phone if one is ON, otherwise power on if OFF
        :return:
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True
        """
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        # enough memory, but the phone is ON
        if self.memory >= app_memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        # enough memory, but the phone is OFF,
        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())