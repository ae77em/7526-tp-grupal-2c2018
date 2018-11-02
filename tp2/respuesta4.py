"""
Customer example.

Covers:

- Waiting for other processes
- Resources: Resource

Scenario:
  A atm has a limited number of washing machines and defines
  a washing processes that takes some (random) time.

  Customer processes arrive at the atm at a random time. If one washing
  machine is available, they start the washing process and wait for it
  to finish. If not, they wait until they an use one.

"""
import random
import simpy
import numpy

RANDOM_SEED = 42
NUM_MACHINES = 1            # Number of machines in the atm
T_INTER_1ST = 4             # Arrive a client every ~4 minutes
T_INTER_2ND = 2             # Arrive a client every ~2 minutes
T_INTER_3RD = 6             # Arrive a client every ~6 minutes
SIM_TIME = 20               # Simulation time in minutes

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

def NoInSystem(R):                                                  
    """ Total number of customers in the resource R"""
    return (len(R.waitQ)+len(R.activeQ))    

def customer(env, name, atm):
    arrive = env.now
    print('%s arrives at the atm at %.2f.' % (name, arrive))

    with atm.machine.request() as request:
        yield request

        print('%s waited in the queue for %.2f minutes.' % (name, env.now-arrive))
        
        print('%s enters the atm at %.2f.' % (name, env.now))
        yield env.process(atm.get_money(name))

        print('%s leaves the atm at %.2f.' % (name, env.now))


def setup(env):
    # Create more customers while the simulation is running
    i = 0
    while True:
        if env.now < 240:
            t_inter = T_INTER_1ST
        elif env.now < 360:
            t_inter = T_INTER_2ND
        else:
            t_inter = T_INTER_3RD

        yield env.timeout(t_inter)
        i += 1

        # Create the atm
        atm = Customer(env)        
        env.process(customer(env, 'Customer %d' % i, atm))


# Setup and start the simulation
print('ATM')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env))
env.run(until=480)