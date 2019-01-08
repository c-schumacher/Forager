class Pareto_Walker(Forager):
    def __init__(self, alpha, xmin=1.0, envRadius=75.0, resoRadius=5.0, resoCount=5):
        Forager.__init__(self, envRadius, resoRadius, resoCount)
        self.alpha = alpha
        self.xmin = xmin
        
    def distRNG(self):
        return self.xmin*(random.random())**(-1./self.alpha)
