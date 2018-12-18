class Pareto_Walker(Forager):
    def __init__(self, alpha, xmin=1.0, agarRadius=75.0, foodRadius=5.0, resourceCount=5):
        Forager.__init__(self, agarRadius, foodRadius, resourceCount)
        self.alpha = alpha
        self.xmin = xmin
        
    def distRNG(self):
        return self.xmin*(random.random())**(-1./self.alpha)