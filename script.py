import click
import random

from time import time


def simulation(doors, switch):
	closed_doors = []

	for i in range(doors):
		closed_doors.append(i)

	choice = random.choice(closed_doors) # randomly chooses a door for player
	prize = random.choice(closed_doors) # randomly chooses door for prize to be behind

	while len(closed_doors) > 2:
		open_door = random.choice(closed_doors) # chooses door to be opened

		if open_door == prize or open_door == choice:
			continue # prize and choice are not opened

		closed_doors.remove(open_door) # opens door

	if switch == True:
		closed_doors.remove(choice) 
		choice = random.choice(closed_doors) # chooses other door given the conditional

	win = (choice == prize) 

	if choice == prize:
		win = True 

	return win

@click.command()
@click.option('-d', '--doors', default=3, help='Number of doors in simulation')
@click.option('-i', '--iterations', default=100, help="Number of iterations of simulation")
def main(doors, iterations):
	start = time()
	switch_win = 0
	not_switch_win = 0

	for i in range(iterations):
		won = simulation(doors, True)

		if won == True:
			switch_win += 1

	for i in range(iterations):
		won = simulation(doors, False)

		if won == True:
			not_switch_win += 1

	click.echo("Switch wins: %.2f" % ((switch_win/iterations)*100) + "%")
	click.echo("Non-switch wins: %.2f" % ((not_switch_win/iterations)*100) + "%")
	click.echo("Executed %d times in %.2f" % (iterations, (time() - start)) + " seconds")


if __name__ == '__main__':
	main()