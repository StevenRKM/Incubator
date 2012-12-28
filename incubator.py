from random import randint

"""

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
         
"""

class Chromosome:
	genes = None
	
	def __init__(self, length = 10, genes = None):
		"""
		length: number of genes in a chromosome
		"""
		if genes == None:
			self.generate( length )
		else:
			self.genes = genes			
		
	def mutate(self):
		old_genes = list(self.genes)
		while old_genes == self.genes:
			self.genes[ randint(0, len(self.genes)-1) ] = randint(0, 9)
	
	def generate( self, length ):
		self.genes = [ randint(0, 9) for i in range(length) ]
		
	def todict( x ):
		return [ int(i) for i in list( x ) ]
		
	def fitness(self):
		return self.genes.count(1)

	def __str__( self ):
		return str("").join( [ i==1 and ' ' or str(i) for i in self.genes ] )
		
	def __repr__( self ):
		return str(self)
		

class Population:
	chromosomes = None
	
	def __init__(self, count = 8, length=10):
		"""
		count: number of chromosomes
		length: number of genes in a chromosome
		"""
		self.chromosomes = [ Chromosome(length) for x in range(count) ]
		
	def fitness(self):
		fitness = [ (c, c.fitness()) for c in self.chromosomes ]
		fitness = sorted( fitness, key=lambda c: c[1], reverse=True )
		return fitness
		
	def selection(self, fitness=None):
		if fitness == None:
			fitness = self.fitness()		
		selection = fitness[ :len(self.chromosomes)/2 ]
		self.chromosomes = [ s[0] for s in selection ]	
		
	def crossover(self):
		for r in range(0, len(self.chromosomes)-1, 2):
			c1 = self.chromosomes[r]
			c2 = self.chromosomes[r+1]
			# select crossover point, make sure it always cuts between two genes
			x = randint( 1, len( c1.genes)-2 )
			new_c1 = c1.genes[:x] + c2.genes[x:]
			new_c2 = c2.genes[:x] + c1.genes[x:]
			self.chromosomes += [Chromosome( genes = new_c1 )]
			self.chromosomes += [Chromosome( genes = new_c2 )]		
		
	def mutate(self):
		for c in self.chromosomes:
			c.mutate()
		
	def __str__( self ):
		return str("\n").join( [ str(i) for i in self.chromosomes ] )
		
	def __repr__( self ):
		return str(self)
	
	
class Incubator:
	
	def __init__(self, count=8, length=10):
		"""
		count: number of chromosomes in a population
		length: number of genes in a chromosome
		"""
		self.generation = 0
		self.best_fitness_history = []
		self.count = count
		self.length = length
		self.population = Population( count=count, length=length )		
		
	def run(self, generations = 10, verbose=False):
		start_generation = self.generation
		
		while self.generation < start_generation + generations:
			if verbose:
				print "\nGeneration %2d\n" % self.generation
				print self.population
			elif start_generation == self.generation:
				print "\nGeneration %2d\n" % self.generation
				print self.population
			
			fitness = self.population.fitness()
			self.population.selection( fitness )
			self.population.crossover()
			self.population.mutate()
			self.best_fitness_history.append( fitness[0][1] )
			
			if verbose:
				print "\nBest fitness %2d" % self.generation, "+"*fitness[0][1] + "."*(self.length -fitness[0][1]), "%2d" % fitness[0][1]
				print "by",fitness[0][0]
			else:
				if start_generation == self.generation + generations -1:
					print "\nGeneration %2d\n" % self.generation
					print self.population
				
			self.generation += 1
			
		print ""
		self.print_best_fitness(generations)
		
	def print_best_fitness(self, last=None):
		if last:
			history = self.best_fitness_history[-last:]
			x = max( len(self.best_fitness_history) - last, 0)
		else:
			history = self.best_fitness_history
			x = 0
		
		for fitness in history:
			print "Generation %2d" % x, "+"*fitness + "."*(self.length -fitness), "%2d" % fitness
			x += 1
