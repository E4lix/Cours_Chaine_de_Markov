
import random
import statistics as stats
import ciw
import math


net_a = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=1.0/30.0)],
    service_distributions=[ciw.dists.Exponential(rate=1.0/25.0)],
    number_of_servers=[1])

sim = ciw.Simulation(net_a)
sim.simulate_until_max_time(20000 + 200000)
recs = sim.get_all_records()
waits = [r.waiting_time for r in recs if r.node==1]
print(sum(waits)/len(waits))


net_b = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=1.0/30.0)],
    service_distributions=[ciw.dists.Uniform(15, 35)],
    number_of_servers=[1])

sim = ciw.Simulation(net_b)
sim.simulate_until_max_time(20000 + 200000)
recs = sim.get_all_records()
waits = [r.waiting_time for r in recs if r.node==1]
print(sum(waits)/len(waits))




net_c = ciw.create_network(
    arrival_distributions=[ciw.dists.Gamma(shape=2.0, scale=15.0)],
    service_distributions=[ciw.dists.Uniform(15, 35)],
    number_of_servers=[1])

sim = ciw.Simulation(net_c)
sim.simulate_until_max_time(20000 + 200000)
recs = sim.get_all_records()
waits = [r.waiting_time for r in recs if r.node==1]
print(sum(waits)/len(waits))
