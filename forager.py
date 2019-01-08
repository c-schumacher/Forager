class Forager(MCEngine):
    def __init__(self, envRadius, resoRadius, resoCount):
        MCEngine.__init__(self)
        self.envRadius = envRadius
        self.resoRadius = resoRadius
        self.resoCount = resoCount
        self.results = np.zeros([0,8])
    
    def simulate_once(self):
        ar = self.envRadius
        fr = self.resoRadius
        rc = self.resoCount if self.resoCount is not None else random.randrange(1,6)
        
        x0, y0 = 0.0, 0.0
        norm = lambda (x0,y0),(x1,y1) : sqrt((x1-x0)**2 + (y1-y0)**2)
        history = []
            
        resources = []
        while len(resources) < rc:
            while True:
                fx = random.uniform(-1.0, 1.0) * ar
                fy = random.uniform(-1.0, 1.0) * ar
                foodDist = sqrt(fx**2 + fy**2)
                if fr+15 < foodDist < ar - fr and all(norm(i,(fx,fy)) > 2*fr for i in resources): 
                    break    
            resources.append((fx,fy))

        found, steps, dist = 0, 0, 0
        start_time = time.time()
        while True:     
            theta = random.random()*2.*pi
            f = self.distRNG()
            x1 = x0 + f*cos(theta)
            y1 = y0 + f*sin(theta)
            history.append((x1,y1))

            dist += sqrt((y1-y0)**2 + (x1-x0)**2)

            if self.findResource(fr, [x0,y0,x1,y1,resources]) == True:
                found = 1
                break
                
            if self.inBounds(ar, [x1,y1]) == False:
                break

            x0, y0 = x1, y1
            steps +=1
        return np.array([resources, found, steps, dist, time.time()-start_time, history, ar, fr]).reshape([1,8]) 
        
    def simulate_many(self, ap = 0.025, rp = 0.025, ns = 10000):
        y, y2 = 0,0
        for i in range(1, ns+1):
            res = self.simulate_once()
            self.results = np.append(self.results, res, axis=0)
            count = res[0,1]
            y += count
            y2 += count**2
            mu = float(y)/i
            variance = float(y2)/i - mu**2
            dmu = variance/sqrt(i)
            if i > 10:
                if abs(dmu) < max(ap, abs(mu)*rp):
                    break
        return self.results

    
    def inBounds(self, outerRadius, positions):
        x1, y1 = positions 
        if x1**2 + y1**2 >= outerRadius**2:
            return False
        else:
            return True
        
    def findResource(self, resRadius, positions):
        Ax, Ay, Bx, By, resources = positions

        locations = len(resources)
        for i in range(locations):
            Cx, Cy = resources[i][0], resources[i][1]
            C = np.array([Cx,Cy])
            r = resRadius
            A = np.array([Ax,Ay])
            B = np.array([Bx,By]) 
            V = B-A  
            a = np.dot(V,V)
            b = 2 * np.dot(V,A-C)
            c = np.dot(A,A) + np.dot(C,C) - 2*np.dot(A,C) - r**2
            disc = b**2 - 4*a*c
            if disc < 0:
                continue
            sqrt_disc = sqrt(disc)
            t1 = (-b + sqrt_disc) / (2*a)
            t2 = (-b - sqrt_disc) / (2*a)
            if not (0 <= t1 <= 1 or 0 <= t2 <= 1):
                continue
            else:
                return True
        return False
    
    def foragerPlot(self):
        results = self.simulate_once()
        fcen = results[0,0]
        hist = results[0,5]
        ar = results [0,6]
        fr = results [0,7]

        plt.figure(figsize=(12,12))
        ax = plt.gca()
        ax.cla() 
        circle = plt.Circle((0, 0), ar, color='black', fill = False)

        ax.set_xlim((-ar-5, ar+5))
        ax.set_ylim((-ar-5, ar+5))
        x,y = zip(*hist)
        ax.plot(x,y, color='black')
        ax.add_artist(circle)
        for i in range(len(fcen)):
            circle2 = plt.Circle((fcen[i][0] , fcen[i][1]), fr, color='g', fill=True)
            ax.add_artist(circle2)
        plt.show()
