teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#seznam průměrných teplot za den
import statistics
avr_tepm = [round(statistics.mean(den), 2) for den in teploty]
print(avr_tepm)

#seznam ranních teplot
morning_temp = [teplota[0] for teplota in teploty]
print(morning_temp)

#seznam nočních teplot
evening_temp = [teplota[3] for teplota in teploty]
print(evening_temp)

#seznam poledních a nočních teplot
noon_evening_temp = [[teplota[1], teplota[3]] for teplota in teploty]
print(noon_evening_temp)