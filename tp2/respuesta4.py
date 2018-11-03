"""

Punto 4

"""
import random
import simpy
import numpy

RANDOM_SEED = 42

class Dto:
    def __init__(self):
        self.current_people = 0
        self.max_people = 0
        self.max_time_waited = 0.0

    def add_people_to_queue(self):
        self.current_people += 1

        if (self.current_people > self.max_people):
            self.max_people = self.current_people

    def quit_people_from_queue(self):
        self.current_people -= 1

    def update_max_waiting_time(self, t):
        if (t>self.max_time_waited):
            self.max_time_waited = t


class Customer(object):
    # Mean of minutes that takes a customer in the atm for each type of client
    PROCESSTIME = {
        '1': 4,
        '2': 2,
        '3': 3
    }

    # Gap of minutes that takes a customer in the atm for each type of client
    GAP = {
        '1': 3,
        '2': 1,
        '3': 2
    }

    def __init__(self, env):
        self.env = env
        self.type =  numpy.random.choice(['1', '2', '3'], p=[0.1, 0.7, 0.2])
        self.machine = simpy.Resource(env)
        self.processtime = self.PROCESSTIME[self.type]
        self.gap = self.GAP[self.type]

    def get_money(self, customer):
        time_in_atm = random.randint(self.processtime-self.gap, self.processtime+self.gap)
        yield self.env.timeout(time_in_atm)
        print("Customer %s took %d minutes." %(customer, time_in_atm))

def customer(env, name, atm, dto):
    arrive = env.now
    print('%s arrives at the atm at %.2f.' % (name, arrive))

    dto.add_people_to_queue()
    
    with atm.machine.request() as request:
        yield request

        waited = env.now - arrive
        print('%s waited in the queue for %.2f minutes.' % (name, waited))
        dto.update_max_waiting_time(waited)
        
        print('%s enters the atm at %.2f.' % (name, env.now))
        yield env.process(atm.get_money(name))

        dto.quit_people_from_queue()

        print('%s leaves the atm at %.2f.' % (name, env.now))
    
def setup(env, dto):
    # Create the atm
    atm = Customer(env)
            
    # Create more customers while the simulation is running
    i = 0
    while True:
        if env.now < 240:
            t_inter = random.expovariate(0.25) # minutes
        elif env.now < 360:
            t_inter = random.expovariate(0.5) # minutes
        else:
            t_inter = random.expovariate(1.0/6.0) # minutes

        yield env.timeout(t_inter)
        i += 1

        env.process(customer(env, 'Customer %d' % i, atm, dto))

# Setup and start the simulation
print('ATM')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
dto = Dto()
env = simpy.Environment()
env.process(setup(env, dto))
env.run(until=480)

print("Max time waited: %.2f minutes." % dto.max_time_waited)
print("Max queue length: %d people." % dto.max_people)

"""
FIN punto 4

"""

