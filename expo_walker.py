class Expo_Walker(Forager):
    def __init__(self, lambd, agarRadius=75.0, foodRadius=5.0, resourceCount=5):
        Forager.__init__(self, agarRadius, foodRadius, resourceCount)
        self.lambd = lambd
        
    def distRNG(self):
        return -log(random.random())/self.lambd