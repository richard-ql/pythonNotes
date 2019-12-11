# 命令行模式
class Wizard:
    def __init__(self, src, root_dir):
        self.choices = []
        self.src = src
        self.root_dir =root_dir

    def preferences(self, command):
        self.choices.append(command)

    def excute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copy binaries --", self.src, " to ", self.root_dir)
            else:
                print("No operation")

if __name__=="__main__":
    wizard = Wizard("python3.5.gzip", "/usr/bin")
    wizard.preferences({"python": True})
    wizard.preferences({"java": False})
    wizard.excute()
