#! /usr/bin/env python

from incubator import Incubator, Population, Chromosome

i = Incubator(16, 50)

# manual run

print "\n\n----- MANUAL RUN -----\n\n"

print "Initial Population\n"
print i.population

fitness = i.population.fitness()
print "\nCalculated Fitness and ordering\n"
for c,f in fitness:
	print str(c) + " score: " + str(f)

i.population.selection( fitness )
print "\nSelection\n"
print i.population

i.population.crossover()
print "\nCrossover\n"
print i.population

i.population.mutate()
print "\nMutation\n"
print i.population



# automatic run

print "\n\n----- AUTOMATIC RUN -----\n\n"

i.run(generations=3, verbose=True)
		
			
		









	
