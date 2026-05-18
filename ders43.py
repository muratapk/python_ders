class Banka:
    def __init__(self,bakiye):
        self.bakiye=bakiye

berfin=Banka(5000)
print(berfin.bakiye)
berfin.bakiye=1000
print(berfin.bakiye)