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


RANDOM_SEED = 42
NUM_MACHINES = 1            # Number of machines in the atm
PROCESSTIME_TYPE1 = 4       # Minutes that takes a customer in the atm
PROCESSTIME_TYPE2 = 2       # Minutes that takes a customer in the atm
PROCESSTIME_TYPE3 = 3       # Minutes that takes a customer in the atm
PROCESSTIME_GAP1 = 3        # Minutes that takes a customer in the atm
PROCESSTIME_GAP2 = 1        # Minutes that takes a customer in the atm
PROCESSTIME_GAP3 = 2        # Minutes that takes a customer in the atm
PROCESSTIME_PERC1 = 0.1     # Minutes that takes a customer in the atm
PROCESSTIME_PERC2 = 0.7     # Minutes that takes a customer in the atm
PROCESSTIME_PERC3 = 0.2     # Minutes that takes a customer in the atm
T_INTER_1ST = 4             # Arrive a client every ~4 minutes
T_INTER_2ND = 2             # Arrive a client every ~2 minutes
T_INTER_3RD = 6             # Arrive a client every ~6 minutes
SIM_TIME = 20               # Simulation time in minutes


class Customer(object):
    """Customers have to request one of the machines. When they got one, they
    can start the washing processes and wait for it to finish (which
    takes ``washtime`` minutes)."""
    def __init__(self, env, washtime, processtime, gap):
        self.env = env
        self.machine = simpy.Resource(env)
        self.washtime = washtime
        self.processtime = processtime
        self.gap = gap

    def get_money(self, customer):
        """The washing processes. It takes a ``customer`` processes and tries
        to clean it."""
        time_in_atm = random.randint(self.processtime-self.gap, self.processtime+self.gap)
        yield self.env.timeout(time_in_atm)
        print("Customer %s took %d seconds." %(customer, time_in_atm))


def customer(env, name, cw):
    """The customer process (each customer has a ``name``) arrives at the atm
    (``cw``) and requests money.

    It then starts the washing process, waits for it to finish and
    leaves to never come back ..."""
    print('%s arrives at the atm at %.2f.' % (name, env.now))
    with cw.machine.request() as request:
        yield request

        print('%s enters the atm at %.2f.' % (name, env.now))
        yield env.process(cw.get_money(name))

        print('%s leaves the atm at %.2f.' % (name, env.now))


def setup(env, t_inter, processtime, gap):
    """Create a atm, a number of initial customers and keep creating customers
    approx. every ``t_inter`` minutes."""
    # Create the atm
    atm = Customer(env, processtime, processtime, gap)

    # Create 4 initial customers
    for i in range(4):
        env.process(customer(env, 'Customer %d' % i, atm))

    # Create more customers while the simulation is running
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        env.process(customer(env, 'Customer %d' % i, atm))


# Setup and start the simulation
print('ATM')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env, T_INTER_1ST, PROCESSTIME_TYPE1, PROCESSTIME_GAP1))
env.run(until=270) # 1er periodo -> 9-12

env = simpy.Environment()
env.process(setup(env, T_INTER_2ND, PROCESSTIME_TYPE1, PROCESSTIME_GAP1))
env.run(until=270) # 2do periodo -> 12-15

env = simpy.Environment()
env.process(setup(env, T_INTER_3RD, PROCESSTIME_TYPE1, PROCESSTIME_GAP1))
env.run(until=360) # 2do periodo -> 15-19
