class Expo_Walker(Forager):
    def __init__(self, lambd, envRadius=75.0, resoRadius=5.0, resoCount=5):
        Forager.__init__(self, envRadius, resoRadius, resoCount)
        self.lambd = lambd
        
    def distRNG(self):
        return -log(random.random())/self.lambd
