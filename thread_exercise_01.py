import threading
import queue
import time

#form queue
jono = queue.Queue()
#numbers we are working with
numerot = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Put numbers to queue
for n in numerot:
	jono.put(n)

#the print function
def rinttaa_kaikki(lanka, jono):	#arguments are thread number and queue
	while True:
		#gets the task from the queue
		jobi = jono.get()
		#Waits for a seccond for better view
		time.sleep(1)
		#Main loop for printing numbers
		for i in range(10):
			print(f'{jobi}', end=' ')
			jobi += 1
		#At the end of the line print which thread was working
		print(f'Performed by thread # {lanka}')
		#Let the system know the job at hand is done. To free the thread.
		jono.task_done()

#Make four threads and start them
for i in range(1,5):
	jobbari = threading.Thread(target=rinttaa_kaikki, args=(i, jono), daemon=True)
	jobbari.start()

#exits the program when the queue is empty
jono.join()



