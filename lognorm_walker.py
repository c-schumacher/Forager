class Lognorm_Walker(Forager):
    def __init__(self, mu, sigma, agarRadius=75.0, foodRadius=5.0, resourceCount=5):
        Forager.__init__(self, agarRadius, foodRadius, resourceCount)
        self.mu = mu
        self.sigma = sigma
        
    def distRNG(self):
        return random.lognormvariate(self.mu, self.sigma)