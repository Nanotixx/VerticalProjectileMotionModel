# Vertical Projectile Motion Model : by Nanotixx

# Maximum height = v0t - 0.5 gt^2
# Maximum time = v0 / g

class jump:
    def __init__(self, velocity, time, gravity):
        self.velocity = velocity
        self.time = time
        self.gravity = gravity

    def simulate(self):
        heights = []

        while True:
            height = (float(self.velocity) * float(self.time)) - (0.5 * float(self.gravity) * (float(self.time) ** 2))
            self.time += .001 # Change the adding value to get smoother rising/falling motion! :D

            if height < 0:
                height = 0
                break
            else:
                heights.append(str(round(height, 3))) # round(value, n), n can be modified for more precision!
        
        return heights
    
    # Finds the peak of the height and time!
    def peak(self):
        peak_time = self.velocity / self.gravity
        peak_height = (float(self.velocity) * float(peak_time)) - (0.5 * float(self.gravity) * (float(peak_time) ** 2))
        return f"Peak height: {peak_height}\nPeak time: {peak_time}"



test = jump(30, 0, 9.8) # Parameters = (initial velocity, time, gravity)
result = test.simulate()

print("\n".join(result))