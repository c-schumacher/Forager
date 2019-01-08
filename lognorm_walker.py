class Lognorm_Walker(Forager):
    def __init__(self, mu, sigma, envRadius=75.0, resoRadius=5.0, resoCount=5):
        Forager.__init__(self, envRadius, resoRadius, resoCount)
        self.mu = mu
        self.sigma = sigma
        
    def distRNG(self):
        return random.lognormvariate(self.mu, self.sigma)
