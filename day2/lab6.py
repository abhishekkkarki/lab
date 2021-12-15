#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
#run to university. You jog the first mile at 7mph; then run the next two at15mph; before
#jogging the last at 7mph again. Will this be quicker or slower than the bus?
stoppedtime= 2*10
distance= 4
speedMph= 25/60
drivingTime=distance/speedMph
totalTimeByBus= drivingTime+ stoppedtime
runningTime= ((1/7)+(2/15)+(1/7))*60
print(f"The total time taken by a bus is {totalTimeByBus}")
print(f"The total time while jogging is {runningTime}")
if totalTimeByBus>runningTime:
    print("Bus takes more time than the jog")
else:
    print("Bus takes less time than the jog")