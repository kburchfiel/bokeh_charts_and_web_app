import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

df_flights = pd.read_csv(r'C:\Users\kburc\D1V1\Documents\!Dell64docs\Programming\py\kjb3_programs\route_maps_builder\df_flights_for_charting_2018.csv')
df_flights.drop('Unnamed: 0', axis = 1, inplace = True)
df_flights = df_flights.query("PASSENGERS > 0").copy() # Focusing only on passenger flights (i.e. not cargo flights) for these charts
df_flights


df_pax_pivot = df_flights.pivot_table(index = 'ORIGIN', values = ['PASSENGERS'], aggfunc = 'sum')
df_pax_pivot.reset_index(inplace=True)
df_pax_pivot.sort_values('PASSENGERS',ascending = False,inplace=True)
df_pax_pivot.reset_index(drop=True,inplace=True)
df_pax_pivot

df_top_10_airports = df_pax_pivot.head(10)

df_avg_dist_pivot = df_flights.query("ORIGIN_COUNTRY == 'US'").copy().pivot_table(index = 'ORIGIN', values = ['DISTANCE', 'PASSENGERS'], aggfunc = {'DISTANCE':'mean', 'PASSENGERS':'sum'})
df_avg_dist_pivot = df_avg_dist_pivot.query("PASSENGERS > 1000000").copy()
df_avg_dist_pivot.reset_index(inplace=True)
df_avg_dist_pivot.sort_values('DISTANCE',ascending = False,inplace=True)
df_avg_dist_pivot.reset_index(drop=True,inplace=True)

t20_airports_by_avg_dist = df_avg_dist_pivot.head(20)


output_file('t10_airports_by_pax.html')
cds_t10_pax_airports = ColumnDataSource(df_top_10_airports)

tooltips = [
("Airport", "@ORIGIN"),
("Passengers", "@PASSENGERS")
]
p = figure(x_range=df_top_10_airports['ORIGIN'], height = 350, toolbar_location = None, tooltips = tooltips)
p.vbar(x = 'ORIGIN', top = 'PASSENGERS', width = 0.9, source = cds_t10_pax_airports)
p.xaxis.major_label_orientation = 0.8
show(p) # Looks like this is the line that actually updates
# the path passed to output_file with the chart


output_file('t20_airports_by_avg_dist.html')
cds_t20_avg_dist = ColumnDataSource(t20_airports_by_avg_dist)

tooltips = [
("Airport", "@ORIGIN"),
("Average Distance", "@DISTANCE")
]
p_1 = figure(x_range=t20_airports_by_avg_dist['ORIGIN'], height = 350, toolbar_location = None, tooltips = tooltips)
p_1.vbar(x = 'ORIGIN', top = 'DISTANCE', width = 0.9, source = cds_t20_avg_dist)
#p.xaxis.major_label_orientation = 0.8
show(p_1)

print("Finished the script.")
