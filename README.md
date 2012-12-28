Incubator
=========

This is a small example on how a genetic algorithm works.
It shows of the basic principles, but without a proper simulation.

Genes in a Chromosome are represented by a number from 0-9, and are
ordered in that Chromosome. I want to reach a Chromosome that consists
only out of 1's. Therefor the fitness function is very straightforward,
it counts the number of 1's.
( when printing out a Chromosome, these 1's are left blank, for better 
visibility )

You start out by creating an Incubator. This creates a random starting
population. Simply calling run on it will start the process of
generating new generations.
The steps of a Genetic Algorithm are:
* generate random population
* while fitness not good enough
  * selection
  * do a crossover (reproduce)
  * mutate
I left out the automatic while statement, you can manually run until you
are happy with the results.

The selection algorithm I use works with an Elitism of 50%, this is
normally too high to have good results. Eltism means you keep certain
top Chromosomes in your next generation, and only letting them mutate.
These 50% top Chromosomes than do a crossover, each 2 generate 2
offspring, by using a single crossover point.

The mutation is also very simple, it selets a random gene and gives it a
new random value from 0-9.

**WARNING**: Normally you would simulate the genes in a process, for example 
         a physics engine, and based on those results you would 
         calculate the fitness
         
**Check out run.py, and run it**
