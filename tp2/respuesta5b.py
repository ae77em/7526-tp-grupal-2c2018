"""

Punto 5 b

"""
import random
import simpy
import numpy

RANDOM_SEED = 99999
queues = [[],[],[],[],[],[]]

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


class Request(object):
    # Mean of msec that takes a request in the server for each type
    PROCESSTIME = {
        'A': 120,
        'B': 240,
        'C': 500
    }

    # Gap of msec that takes a request in the server for each type
    GAP = {
        'A': 60,
        'B': 120,
        'C': 300
    }

    def __init__(self, env, dto, n):
        self.env = env
        self.type =  numpy.random.choice(['A', 'B', 'C'], p=[0.7, 0.2, 0.1])
        self.machine = simpy.Resource(env)
        self.processtime = self.PROCESSTIME[self.type]
        self.gap = self.GAP[self.type]
        self.queue_data = dto
        self.number_of_server = n

    def __str__(self):
        return str(self.number_of_server) + " -> " + str(self.queue_data.current_people)

    def do_process(self, request):
        time_in_server = random.randint(self.processtime-self.gap, self.processtime+self.gap)
        yield self.env.timeout(time_in_server)
        print("%s of type %s took %d msec." %(request, self.type, time_in_server))

def request(env, name, server):
    arrive = env.now
    print('%s arrives at the server %d at %.2f.' % (name, server.number_of_server, arrive))

    server.queue_data.add_people_to_queue()
    
    with server.machine.request() as request:
        yield request

        waited = env.now - arrive
        print('%s waited in the queue of server %d for %.2f msec.' % (name, server.number_of_server, waited))
        server.queue_data.update_max_waiting_time(waited)
        
        print('%s enters the server %d at %.2f.' % (name, server.number_of_server, env.now))
        yield env.process(server.do_process(name))

        server.queue_data.quit_people_from_queue()

        print('%s leaves the server %d at %.2f.' % (name, server.number_of_server, env.now))
    
def setup(env, dtos):
    # Create the server
    servers = [Request(env, dtos[0], 1), Request(env, dtos[1], 2), Request(env, dtos[2], 3), Request(env, dtos[3], 4), Request(env, dtos[4], 5)]
            
    # Create more customers while the simulation is running
    i = 0
    j = 0
    while True:
        t_inter = random.expovariate(1.0/45.0) # msec

        yield env.timeout(t_inter)
        i += 1
                
        server = servers[j]
        env.process(request(env, 'Request %d' % i, server))
        j += 1
        
        if ( j > 4): 
            j = 0

# Setup and start the simulation
print('SERVER')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
dtos = [Dto(), Dto(), Dto(), Dto(), Dto()]
env = simpy.Environment()
env.process(setup(env, dtos))
env.run(until=1000000)

print("Round Robin")
for dto in dtos:
    print("Max time waited: %.2f msec." % dto.max_time_waited)
    print("Max queue length: %d people." % dto.max_people)

"""
FIN Punto 5 b

"""

