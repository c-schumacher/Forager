class MCEngine(object):   
    def simulate_once(self):
        raise NotImplementedError
        
    def simulate_many(self, ap = 0.05, rp = 0.05, ns = 10000):
        y, y2 = 0,0
        self.results = []
        for i in range(1, ns+1):
            res = self.simulate_once()
            self.results.append(res)
            count = res[0,1]
            y += count
            y2 += count**2
            mu = float(y)/i
            variance = float(y2)/i - mu**2
            dmu = variance/sqrt(i)
            if i > 15:
                if abs(dmu) < max(ap, abs(mu)*rp):
                    break
        return bootstrap(self.results)