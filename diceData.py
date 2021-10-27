import random
import statistics 
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_results = []
for i in range (0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_results.append(dice1 + dice2)

mean = sum(dice_results)/len(dice_results)
median = statistics.median(dice_results)
mode = statistics.mode(dice_results)
std_deviation = statistics.stdev(dice_results)


first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)

fig = ff.create_distplot([dice_results], ["Results"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start], y =[0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y =[0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start], y =[0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y =[0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))

fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start], y =[0,0.17], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end], y =[0,0.17], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in dice_results if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_results if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_results if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}%  of data lies within first STANDARD DEVIATION".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_results)))
print("{}%  of data lies within second STANDARD DEVIATION".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_results)))
print("{}%  of data lies within third STANDARD DEVIATION".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_results)))
print("Mean of this Data is {}".format(mean))
print("Median of this Data {}".format(median))
print("Mode of this Data is {}".format(mode))
print("Stanndard deviation of this data is {}".format(std_deviation))