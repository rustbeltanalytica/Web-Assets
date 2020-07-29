from django.shortcuts import render
from django.http import HttpResponse
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.subplots import make_subplots


from django.template import loader

import pandas as pd
# import modin.pandas as pd
import numpy as np
import scipy.stats as stats

import plotly.graph_objects as go
import plotly.express as px
from urllib.request import urlopen
import json

def index(request):

	# return HttpResponse("Start of Web Doc")

	# x_data = [0,1,2,3]
	# y_data = [x**2 for x in x_data]
	# plot_div = plot([Scatter(x=x_data, y=y_data,
	# 				mode='lines', name='test',
	# 				opacity=0.8, marker_color='green')],
	# 				output_type='div')
	template = loader.get_template('fog/index.html')
	# context={'plot_div': plot_div}

	# FIGURE 2 Plotly

	world_50 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_2.csv')

	fig_1 = go.Figure(data=[go.Bar(x=world_50['GeoName'], y=world_50['2018'])])
	fig_1.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)
	fig_1.update_xaxes(title_text="", tickangle=45)

	fig_1.update_layout(
	    title="Figure 2: Top 1% of Countries by Total Real GDP.  Source: BEA, 2018 (in 2012$)",
	    xaxis_title="",
	    yaxis_title="GDP",
	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    showlegend=False,
	    # width=1500,
	    # height=700,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
	)

	plot_div = plot(fig_1, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
	
	'''
		Figure #: 1
		Section #: 1
		Data: BEA 
	'''

	gdp_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/pt1_fig2.csv')

	fig_2 = go.Figure(data=[go.Bar(x=gdp_10['State'], y=gdp_10['GDP'])])
	fig_2.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)
	fig_2.update_xaxes(title_text="", tickangle=45)

	fig_2.update_layout(
	    title="Figure 1: Largest State Economies by Total Real GDP. Source BEA, 2018 (in 2012$)",
	    xaxis_title="",
	    yaxis_title="GDP",
	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    showlegend=False,
	    # width=1500,
	    # height=700,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
	)
	# fig2.update_layout(showlegend=False)

	plot_div2 = plot(fig_2, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_4_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_4.csv')
	fig_4 = px.scatter(fig_4_df, x='Annualized Growth Rate TP', y='Annualized GDP', color="MSA",
                 hover_data=['MSA'])


	fig_4.update_layout(showlegend=False)

	fig_4.update_layout(

	    xaxis_title="Annualized Growth Rate Total Population",
	    yaxis_title="Annualized Growth Rate Per Capita GDP",
	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    showlegend=False,
	    # width=1500,
	    # height=700,
	    
	    uniformtext_minsize=8,
		xaxis =  {                                     
                  'showgrid': False
                                         },
        yaxis = {                              
                  'showgrid': False
                },

	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_4.update_traces(mode='markers', marker_line_width=2, marker_size=8)

	plot_div4 = plot(fig_4, output_type='div', include_plotlyjs=False, show_link=False, link_text="")



	rusty = [50970, 51483, 52393, 53298, 54384, 54463, 54762, 53673, 51196, 52469, 53366, 54343, 54716, 55519, 56589, 57018, 57775, 59073]
	sunny  =[50759, 50359, 50881, 53018, 54392, 55560, 56188, 54458, 50845, 51036, 51709, 52279, 52580, 52566, 53968, 53232, 53518, 54604]
	years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]


	fig_6 = go.Figure(data=[
	    go.Bar(name='Rust Belt', x=years, y=rusty, marker=go.bar.Marker(color='rgb(165,15,21)')),
	    go.Bar(name='Sun Belt', x=years, y=sunny, marker=go.bar.Marker(color='rgb(102,101,101)'))
	])

	fig_6.update_yaxes(range=[46000, 60000])
	fig_6.update_layout(title_text='Figure 6: Real GDP Per Capita in the Rust Belt vs the Sun Belt. Source: BEA, 2001-2018')
	fig_6.update_layout(barmode='group')
	fig_6.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)
	
	plot_div6 = plot(fig_6, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	years_7 = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

	cle_7 = [49280, 50487, 51781, 53162, 54677, 54050, 54303, 54652, 50980, 51635, 52899, 53260, 53351, 55194, 56084, 56195, 56902, 58010]
	cuy_7 = [57518, 59037, 60880, 62399, 64555, 63733, 64356, 65304, 61033, 61271, 62653, 63743, 64308, 66639, 68125, 68458, 69681, 71325]
	us_7 = [46539, 46912, 47841, 49201, 50463, 51405, 51874, 51315, 49577, 50428, 50840, 51603, 52191, 53118, 54261, 54752, 55692, 56968]

	fig_7 = go.Figure()
	fig_7.add_trace(go.Scatter(x=years_7, y=cle_7, name='Cleveland',
	                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_7.add_trace(go.Scatter(x=years_7, y=us_7, name = 'U.S.',
	                         line=dict(color='rgb(81,80,80)', width=4, dash='dash')))
	fig_7.add_trace(go.Scatter(x=years_7, y=cuy_7, name='Cuyahoga',
	                         line=dict(color='rgb(102,101,101)', width=4)))

	fig_7.update_layout(title_text='Figure 7: GDP Per Capita for Cleveland MSA, Cuyahoga County, and the U.S. Source BEA (in 2012$)')
	fig_7.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)
	
	plot_div7 = plot(fig_7, output_type='div', include_plotlyjs=False, show_link=False, link_text="")



	# pop_by_gdp = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/pop_by_gdp.csv')
	# fig8 = px.scatter(pop_by_gdp.reset_index(), x="CAGR_01-10_y", y="CAGR_01-10_gdp", color='GeoName', hover_data=['GeoName']) 
	fig_8_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_8.csv')
	fig_8 = px.scatter(fig_8_df, x='Annualized Rate Pop.1', y='Annualized Rate GDP Per Capita.1', color="MSA",
                 hover_data=['MSA'])


	fig_8.update_layout(showlegend=False)

	fig_8.update_layout(

	    xaxis_title="Annualized Growth Rate Total Population",
	    yaxis_title="Annualized Growth Rate Per Capita GDP",
	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    showlegend=False,
	    # width=1500,
	    # height=700,
	    
	    uniformtext_minsize=8,
		xaxis =  {                                     
                  'showgrid': False
                                         },
        yaxis = {                              
                  'showgrid': False
                },

	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_8.update_traces(mode='markers', marker_line_width=2, marker_size=8)
	plot_div8 = plot(fig_8, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_9_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_9.csv')

	fig_9 = px.scatter(fig_9_df, x='AGR 10 to 18 Pop', y='AGR 10 to 18 GDP', color="County",
                 hover_data=['County'])


	fig_9.update_layout(showlegend=False)

	fig_9.update_layout(

	    xaxis_title="Annualized Growth Rate Total Population",
	    yaxis_title="Annualized Growth Rate Per Capita GDP",
	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    showlegend=False,
	    # width=1500,
	    # height=700,
	    
	    uniformtext_minsize=8,
		xaxis =  {                                     
                  'showgrid': False
                                         },
        yaxis = {                              
                  'showgrid': False
                },

	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_9.update_traces(mode='markers', marker_line_width=2, marker_size=8)
	plot_div9 = plot(fig_9, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# quat_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_quat.csv')
	# tertiary_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_tert.csv')
	# secondary_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_sec.csv')
	# primary_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_primary_bar.csv')



	# fig_10 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_10.add_trace(go.Bar(x=quat_bar_10['Year'], y=quat_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_10.add_trace(go.Bar(x=tertiary_bar_10['Year'], y=tertiary_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_10.add_trace(go.Bar(x=secondary_bar_10['Year'], y=secondary_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_10.add_trace(go.Bar(x=primary_bar_10['Year'], y=primary_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)


	# # Update yaxis properties
	# fig_10.update_yaxes(range=[0, 70], row=1, col=1)
	# fig_10.update_yaxes(range=[0, 70], row=1, col=2)
	# fig_10.update_yaxes(range=[0, 70], row=2, col=1)
	# fig_10.update_yaxes(range=[0, 70], row=2, col=2)

	# # Update title and height
	# fig_10.update_layout(title_text="figure 10: Share of Total Real GDP by Sector for United States, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	df_10_p = [3.6, 3.6, 3.4, 3.4, 3.4, 3.6, 3.6, 3.6, 4.2, 3.7, 3.7, 3.8, 4.1, 4.3, 4.5, 4.3, 4.4, 4.3]
	df_10_s = [20.7, 20.3, 20.5, 20.9, 20.6, 20.6, 20.6, 19.9, 18.4, 18.4, 18.1, 17.7, 17.9, 17.7, 17.4, 17.2, 17.2, 17.2]
	df_10_t = [65.0, 64.9, 64.8, 64.1, 64.2, 63.8, 63.3, 63.0, 64.0, 64.2, 64.3, 64.6, 64.0, 63.9, 63.6, 63.4, 63.2, 62.8]
	df_10_q = [11.5, 11.9, 11.7, 12.0, 12.1, 12.2, 12.7, 13.7, 13.5, 13.7, 13.9, 13.9, 14.1, 14.2, 14.6, 15.1, 15.4, 15.9]

	years_10 = list(range(2001,2019))

	fig_10 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_10.add_trace(go.Bar(x=years_10, y=df_10_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_10.add_trace(go.Bar(x=years_10, y=df_10_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_10.add_trace(go.Bar(x=years_10, y=df_10_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_10.add_trace(go.Bar(x=years_10, y=df_10_p, text='% Share of GDP by Sector'),
	              row=2, col=1)


	# Update yaxis properties
	fig_10.update_yaxes(range=[0, 70], row=1, col=1)
	fig_10.update_yaxes(range=[0, 70], row=1, col=2)
	fig_10.update_yaxes(range=[0, 70], row=2, col=1)
	fig_10.update_yaxes(range=[0, 70], row=2, col=2)

	# Update title and height
	fig_10.update_layout(title_text="Figure 10: Share of Total Real GDP by Sector for United States, 2001 to 2018. Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_10.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    # showlegend=False,
	    # width=1500,
	    # height=700,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_10.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)


	plot_div10 = plot(fig_10, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# quat_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_quat.csv')
	# tertiary_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_tert.csv')
	# secondary_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_sec.csv')
	# primary_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_primary_bar.csv')

	# fig_11 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_11.add_trace(go.Bar(x=quat_bar_11['Year'], y=quat_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_11.add_trace(go.Bar(x=tertiary_bar_11['Year'], y=tertiary_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_11.add_trace(go.Bar(x=secondary_bar_11['Year'], y=secondary_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_11.add_trace(go.Bar(x=primary_bar_11['Year'], y=primary_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_11.update_yaxes(range=[0, 50], row=1, col=1)
	# fig_11.update_yaxes(range=[0, 50], row=1, col=2)
	# fig_11.update_yaxes(range=[0, 50], row=2, col=1)
	# fig_11.update_yaxes(range=[0, 50], row=2, col=2)

	# # Update title and height
	# fig_11.update_layout(title_text="figure 11: Share of Total Real GDP by Sector for Santa Clara County, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	# fig_11.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	#     # width=1500,
	#     # height=700,
	#     # showlegend=False,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)



	# fig_11.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)

	df_11_p = [.8, .5, .4, .3, .2, .3, .2, .2, .4, .3, .2, .2, .2, .2, .2, .3, .3, .2]
	df_11_s = [23.0, 22.1, 22.8, 22.6, 24.6, 25.4, 27.1, 27.6, 28.6, 28.8, 28.8, 29.9, 28.9, 28.7, 28.8, 29.0, 28.7, 28.2]
	df_11_t = [59.3, 60.7, 56.7, 54.9, 51.3, 49.1, 46.8, 44.8, 43.9, 41.6, 40.2, 39.5, 37.6, 36.5, 35.1, 33.7, 32.6, 31.0]
	df_11_q = [24.3, 24.0, 25.0, 26.6, 26.2, 26.9, 26.8, 27.9, 27.4, 29.3, 30.9, 29.3, 33.3, 34.7, 36.0, 37.3, 38.9, 41.4]


	years_11 = list(range(2001,2019))

	fig_11 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_11.add_trace(go.Bar(x=years_11, y=df_11_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_11.add_trace(go.Bar(x=years_11, y=df_11_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_11.add_trace(go.Bar(x=years_11, y=df_11_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_11.add_trace(go.Bar(x=years_11, y=df_11_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_11.update_yaxes(range=[0, 75], row=1, col=1)
	fig_11.update_yaxes(range=[0, 50], row=1, col=2)
	fig_11.update_yaxes(range=[0, 50], row=2, col=1)
	fig_11.update_yaxes(range=[0, 50], row=2, col=2)

	# Update title and height
	fig_11.update_layout(title_text="Figure 11: Share of Total Real GDP by Sector for Santa Clara County, 2001 to 2018. Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_11.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    # width=1500,
	    # height=700,
	    # showlegend=False,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)



	fig_11.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
	                  marker_line_width=1.5, opacity=0.6)


	plot_div11 = plot(fig_11, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	# quat_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_quat.csv')
	# tertiary_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_tert.csv')
	# secondary_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_sec.csv')
	# primary_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_primary_bar.csv')

	# fig_12 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_12.add_trace(go.Bar(x=quat_bar_12['Year'], y=quat_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_12.add_trace(go.Bar(x=tertiary_bar_12['Year'], y=tertiary_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_12.add_trace(go.Bar(x=secondary_bar_12['Year'], y=secondary_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_12.add_trace(go.Bar(x=primary_bar_12['Year'], y=primary_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_12.update_yaxes(range=[0, 70], row=1, col=1)
	# fig_12.update_yaxes(range=[0, 60], row=1, col=2)
	# fig_12.update_yaxes(range=[0, 1], row=2, col=1)
	# fig_12.update_yaxes(range=[0, 60], row=2, col=2)

	# # Update title and height
	# fig_12.update_layout(title_text="figure 12: Share of Total Real GDP by Sector for San Francisco County, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	# fig_12.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	#     # width=1500,
	#     # height=700,
	#     # showlegend=False,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	# fig_12.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)
	df_12_p = [.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	df_12_s = [6.3,5.9,6.0,5.6,5.5,5.0,5.1,5.1,4.8,4.3,4.5,4.7,5.0,5.2,5.3,5.8,5.5,5.4]
	df_12_t = [68.6,68.9,69.4,68.7,68.3,67.8,66.6,64.1,66.4,66.0,63.7,63.3,62.3,59.8,57.4,54.8,53.1,50.7]
	df_12_q = [24.2,24.2,23.6,24.5,24.9,26.2,27.2,29.9,28.1,28.9,30.8,30.7,31.6,33.7,36.4,38.2,40.4,42.6] 


	years_12 = list(range(2001,2019))

	fig_12 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_12.add_trace(go.Bar(x=years_12, y=df_12_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_12.add_trace(go.Bar(x=years_12, y=df_12_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_12.add_trace(go.Bar(x=years_12, y=df_12_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_12.add_trace(go.Bar(x=years_12, y=df_12_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_12.update_yaxes(range=[0, 80], row=1, col=1)
	fig_12.update_yaxes(range=[0, 50], row=1, col=2)
	fig_12.update_yaxes(range=[0, 50], row=2, col=1)
	fig_12.update_yaxes(range=[0, 50], row=2, col=2)

	# Update title and height
	fig_12.update_layout(title_text="Figure 12: Share of Total Real GDP by Sector for San Francisco County, 2001 to 2018. Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_12.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    # width=1500,
	    # height=700,
	    # showlegend=False,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)



	fig_12.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
	                  marker_line_width=1.5, opacity=0.6)


	

	plot_div12 = plot(fig_12, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# quat_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_quat.csv')
	# tertiary_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_tert.csv')
	# secondary_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_sec.csv')
	# primary_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_primary_bar.csv')

	# fig_13 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_13.add_trace(go.Bar(x=quat_bar_13['Year'], y=quat_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_13.add_trace(go.Bar(x=tertiary_bar_13['Year'], y=tertiary_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_13.add_trace(go.Bar(x=secondary_bar_13['Year'], y=secondary_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_13.add_trace(go.Bar(x=primary_bar_13['Year'], y=primary_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_13.update_yaxes(range=[0, 70], row=1, col=1)
	# fig_13.update_yaxes(range=[0, 60], row=1, col=2)
	# fig_13.update_yaxes(range=[0, 60], row=2, col=1)
	# fig_13.update_yaxes(range=[0, 60], row=2, col=2)

	# # Update title and height
	# fig_13.update_layout(title_text="figure 13: Share of Total Real GDP by Sector for Ohio, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	# fig_13.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	#     # width=1500,
	#     # height=700,
	#     # showlegend=False,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)


	# fig_13.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)

	df_13_p = [1.5,1.6,1.4,1.5,1.4,1.5,1.4,1.4,2.0,1.6,1.6,1.4,1.9,2.5,3.4,3.9,4.2,4.4]
	df_13_s = [27.8,27.3,27.2,28.0,27.3,27.2,26.7,25.0,22.2,22.8,23.4,22.8,22.9,23.8,22.6,22.5,22.4,22.6]
	df_13_t = [63.7,63.8,64.1,63.2,63.8,63.7,63.8,64.6,66.0,65.3,64.4,65.5,65.1,64.4,64.8,64.6,64.4,64.1]
	df_13_q = [7.8,8.0,7.9,7.9,7.9,8.1,8.5,9.2,9.9,10.3,10.6,10.3,10.2,9.3,9.3,9.4,9.5,9.6] 


	years_13 = list(range(2001,2019))

	fig_13 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_13.add_trace(go.Bar(x=years_13, y=df_13_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_13.add_trace(go.Bar(x=years_13, y=df_13_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_13.add_trace(go.Bar(x=years_13, y=df_13_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_13.add_trace(go.Bar(x=years_13, y=df_13_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_13.update_yaxes(range=[0, 80], row=1, col=1)
	fig_13.update_yaxes(range=[0, 50], row=1, col=2)
	fig_13.update_yaxes(range=[0, 50], row=2, col=1)
	fig_13.update_yaxes(range=[0, 50], row=2, col=2)

	# Update title and height
	fig_13.update_layout(title_text="Figure 13: Share of Total Real GDP by Sector for San Francisco County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_13.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#213131"
	    ),
	    autosize=True,
	    # width=1500,
	    # height=700,
	    # showlegend=False,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)



	fig_13.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
	                  marker_line_width=1.5, opacity=0.6)


	plot_div13 = plot(fig_13, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# quat_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_quat.csv')
	# tertiary_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_tert.csv')
	# secondary_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_sec.csv')
	# primary_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_primary_bar.csv')

	# fig_14 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_14.add_trace(go.Bar(x=quat_bar_14['Year'], y=quat_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_14.add_trace(go.Bar(x=tertiary_bar_14['Year'], y=tertiary_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_14.add_trace(go.Bar(x=secondary_bar_14['Year'], y=secondary_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_14.add_trace(go.Bar(x=primary_bar_14['Year'], y=primary_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_14.update_yaxes(range=[0, 80], row=1, col=1)
	# fig_14.update_yaxes(range=[0, 60], row=1, col=2)
	# fig_14.update_yaxes(range=[0, 5], row=2, col=1)
	# fig_14.update_yaxes(range=[0, 60], row=2, col=2)

	# # Update title and height
	# fig_14.update_layout(title_text="figure 14: Share of Total Real GDP by Sector for Cuyahoga County, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	# fig_14.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	#     # width=1500,
	#     # height=700,
	#     # showlegend=False,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	# fig_14.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)

	df_14_p = [.2,.2,.1,.2,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.2,.2,.2,.2]
	df_14_s = [19.7,19.2,19.1,19.0,18.0,18.3,18.5,17.5,14.7,15.5,15.8,15.1,15.2,15.0,14.5,14.3,14.2,14.4]
	df_14_t = [69.2,69.3,69.7,70.1,71.0,70.9,70.1,70.0,71.9,70.9,70.4,71.4,71.3,72.1,72.3,72.1,72.3,72.1]
	df_14_q = [11.5,11.6,11.3,11.0,10.9,11.0,11.6,12.5,13.3,13.6,13.8,13.4,13.4,12.7,12.9,13.3,13.5,13.4] 


	years_14 = list(range(2001,2019))

	fig_14 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_14.add_trace(go.Bar(x=years_14, y=df_14_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_14.add_trace(go.Bar(x=years_14, y=df_14_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_14.add_trace(go.Bar(x=years_14, y=df_14_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_14.add_trace(go.Bar(x=years_14, y=df_14_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_14.update_yaxes(range=[0, 80], row=1, col=1)
	fig_14.update_yaxes(range=[0, 50], row=1, col=2)
	fig_14.update_yaxes(range=[0, 50], row=2, col=1)
	fig_14.update_yaxes(range=[0, 50], row=2, col=2)

	# Update title and height
	fig_14.update_layout(title_text="Figure 14: Share of Total Real GDP by Sector for San Francisco County, 2001 to 2018. Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_14.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#214141"
	    ),
	    autosize=True,
	    # width=1500,
	    # height=700,
	    # showlegend=False,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)



	fig_14.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
	                  marker_line_width=1.5, opacity=0.6)

	plot_div14 = plot(fig_14, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# blue_collar_bar_15 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_15_blue_collar_bar.csv')
	# lower_skill_bar_15 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_15_lower_skill_bar.csv')
	# knowledge_based_bar_15 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_15_knowledge_based_bar.csv')

	# fig_15 = go.Figure(data=[
 #    go.Bar(x=blue_collar_bar_15['Year'], y=blue_collar_bar_15['% Share of GDP by Sector'], text=blue_collar_bar_15['% Share of GDP by Sector'], name="Blue-collar Services", marker=go.bar.Marker(color='rgb(165,15,21)')),
 #    go.Bar(x=lower_skill_bar_15['Year'], y=lower_skill_bar_15['% Share of GDP by Sector'], text=lower_skill_bar_15['% Share of GDP by Sector'], name="Lower-wage Services", marker=go.bar.Marker(color='rgb(81,80,80)')),
 #    go.Bar(x=knowledge_based_bar_15['Year'], y=knowledge_based_bar_15['% Share of GDP by Sector'], text=knowledge_based_bar_15['% Share of GDP by Sector'], name='Knowledge-based Services', marker=go.bar.Marker(color='rgb(203,24,29)'))


	# ])
	# # Change the bar mode
	# fig_15.update_layout(barmode='stack')

	# fig_15.update_layout(title_text="Figure 15: Breakdown of Cuyahoga County's Service Sector as Composition of GDP") 

	# fig_15.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	years_15 = list(range(2001,2019))
	kb_lables = ["42%","43%","43%","43%","45%","44%","43%","44%","47%","45%","45%","47%","46%","47%","48%","48%","47%","47%"]
	lw_labels = ["16%","15%","15%","15%","14%","14%","14%","13%","13%","13%","13%","13%","13%","13%","13%","13%","13%","13%"]
	bc_labels = ["12%","11%","12%","12%","12%","13%","13%","13%","12%","13%","12%","12%","12%","11%","11%","11%","12%","12%"]
	kb_15 = [42,43,43,43,45,44,43,44,47,45,45,47,46,47,48,48,47,47]
	lw_15 = [16,15,15,15,14,14,14,13,13,13,13,13,13,13,13,13,13,13]
	bc_15 = [12,11,12,12,12,13,13,13,12,13,12,12,12,11,11,11,12,12]

	fig_15 = go.Figure(data=[
	    go.Bar(x=years_15, y=bc_15, text=bc_labels, name="Blue-collar Services", marker=go.bar.Marker(color='rgb(165,15,21)')),
	    go.Bar(x=years_15, y=lw_15, text=lw_labels, name="Lower-wage Services", marker=go.bar.Marker(color='rgb(81,80,80)')),
	    go.Bar(x=years_15, y=kb_15, text=kb_lables, name='Knowledge-based Services', marker=go.bar.Marker(color='rgb(203,24,29)'))


	])
	# Change the bar mode
	fig_15.update_layout(barmode='stack')

	fig_15.update_layout(title_text="Figure 15: Breakdown of Cuyahoga County's Service Sector as Composition of GDP") 

	fig_15.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)
	
	plot_div15 = plot(fig_15, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# fire_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_fire.csv')
	# health_care_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_health.csv')
	# manage_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_manage.csv')
	# education_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_ed.csv')
	# arts_and_rec_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_arts.csv')


	# fig_16 = go.Figure(data=[
 #    go.Bar(x=fire_bar_16['Year'], y=fire_bar_16['% Share of GDP by Sector'], text=fire_bar_16['% Share of GDP by Sector'], name="F.I.R.E.", marker=go.bar.Marker(color='rgb(0,0,0)')),
 #    go.Bar(x=health_care_bar_16['Year'], y=health_care_bar_16['% Share of GDP by Sector'], text=health_care_bar_16['% Share of GDP by Sector'], name="Health Care", marker=go.bar.Marker(color='rgb(165,15,21)')),
 #    go.Bar(x=manage_bar_16['Year'], y=manage_bar_16['% Share of GDP by Sector'], text=manage_bar_16['% Share of GDP by Sector'], name="Management of Companies", marker=go.bar.Marker(color='rgb(203,24,29)')),
 #    go.Bar(x=education_bar_16['Year'], y=education_bar_16['% Share of GDP by Sector'], text=education_bar_16['% Share of GDP by Sector'], name="Education", marker=go.bar.Marker(color='rgb(124,123,122)')),
 #    go.Bar(x=arts_and_rec_bar_16['Year'], y=arts_and_rec_bar_16['% Share of GDP by Sector'], text=arts_and_rec_bar_16['% Share of GDP by Sector'], name="Arts and Recreation", marker=go.bar.Marker(color='rgb(171,171,170)'))



	# ])
	# # Change the bar mode
	# fig_16.update_layout(barmode='stack')
	# fig_16.update_layout(title_text="figure 16: Breakdown of Cuyahoga County's Knowledge-Based Services as Composition of GDP")

	# fig_16.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	years_16 = list(range(2001,2019))

	fire_bar_16_labels = ["62.3%","63.7%","63.5%","63.7%","65.7%","62.0%","63.0%","62.8%","61.9%","59.1%","59.1%","57.4%","56.4%","58.7%","59.8%","59.2%","58.6%","58.5%"]
	health_care_bar_16_labels = ["23.0%","22.4%","22.2%","22.4%","21.2%","23.7%","23.4%","23.9%","24.9%","26.4%","26.2%","26.2%","27.0%","25.3%","25.1%","25.7%","24.8%","24.8%"]
	manage_bar_16_labels = ["6.7%","6.3%","6.7%","6.5%","6.4%","7.3%","6.6%","6.3%","5.7%","6.5%","7.2%","9.0%","8.9%","8.6%","8.1%","7.8%","9.5%","9.4%"]
	education_bar_16_labels = ["4.4%","4.2%","4.3%","4.4%","4.0%","4.2%","4.2%","4.2%","4.6%","4.7%","4.5%","4.1%","4.0%","3.7%","3.5%","3.6%","3.3%","3.3%"]
	arts_and_rec_bar_16_labels = ["3.6%","3.5%","3.3%","3.0%","2.6%","2.7%","2.9%","2.8%","3.0%","3.4%","3.0%","3.3%","3.6%","3.8%","3.6%","3.7%","3.8%","3.9%"]

	fire_bar_16 = [62.3,63.7,63.5,63.7,65.7,62.0,63.0,62.8,61.9,59.1,59.1,57.4,56.4,58.7,59.8,59.2,58.6,58.5]
	health_care_bar_16 = [23.0,22.4,22.2,22.4,21.2,23.7,23.4,23.9,24.9,26.4,26.2,26.2,27.0,25.3,25.1,25.7,24.8,24.8]
	manage_bar_16 = [6.7,6.3,6.7,6.5,6.4,7.3,6.6,6.3,5.7,6.5,7.2,9.0,8.9,8.6,8.1,7.8,9.5,9.4]
	education_bar_16 = [4.4,4.2,4.3,4.4,4.0,4.2,4.2,4.2,4.6,4.7,4.5,4.1,4.0,3.7,3.5,3.6,3.3,3.3]
	arts_and_rec_bar_16 = [3.6,3.5,3.3,3.0,2.6,2.7,2.9,2.8,3.0,3.4,3.0,3.3,3.6,3.8,3.6,3.7,3.8,3.9]



	fig_16 = go.Figure(data=[
	    go.Bar(x=years_16, y=fire_bar_16, name="F.I.R.E.", text=fire_bar_16_labels, marker=go.bar.Marker(color='rgb(0,0,0)')),
	    go.Bar(x=years_16, y=health_care_bar_16, text=health_care_bar_16_labels, name="Health Care", marker=go.bar.Marker(color='rgb(165,15,21)')),
	    go.Bar(x=years_16, y=manage_bar_16, text=manage_bar_16_labels, name="Management of Companies", marker=go.bar.Marker(color='rgb(203,24,29)')),
	    go.Bar(x=years_16, y=education_bar_16, text=education_bar_16_labels,name="Education", marker=go.bar.Marker(color='rgb(124,123,122)')),
	    go.Bar(x=years_16, y=arts_and_rec_bar_16, text=arts_and_rec_bar_16_labels,name="Arts and Recreation", marker=go.bar.Marker(color='rgb(171,171,170)'))



	])
	# Change the bar mode
	fig_16.update_layout(barmode='stack')
	fig_16.update_layout(title_text="Figure 16: Breakdown of Cuyahoga County's Knowledge-Based Services as Composition of GDP")

	fig_16.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)

	
	plot_div16 = plot(fig_16, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	# quat_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_quat.csv')
	# tertiary_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_tert.csv')
	# secondary_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_sec.csv')
	# primary_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_primary.csv')

	# fig_17 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_17.add_trace(go.Bar(x=quat_bar_17['Year'], y=quat_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_17.add_trace(go.Bar(x=tertiary_bar_17['Year'], y=tertiary_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_17.add_trace(go.Bar(x=secondary_bar_17['Year'], y=secondary_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_17.add_trace(go.Bar(x=primary_bar_17['Year'], y=primary_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_17.update_yaxes(range=[0, 80], row=1, col=1)
	# fig_17.update_yaxes(range=[0, 60], row=1, col=2)
	# fig_17.update_yaxes(range=[0, 50], row=2, col=1)
	# fig_17.update_yaxes(range=[0, 60], row=2, col=2)

	# # Update title and height
	# fig_17.update_layout(title_text="figure 17: Share of Total Real GDP by Sector for Clark County, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	# fig_17.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	# fig_17.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)

	df_17_p = [.2,.2,.2,.2,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]
	df_17_s = [14.1,13.5,14.1,15.3,16.1,15.5,15.5,14.4,13.5,11.5,10.1,9.1,8.4,7.9,7.5,7.7,7.9,8.2]
	df_17_t = [78.1,78.2,77.8,76.9,76.2,76.8,76.7,77.2,77.6,79.7,81.2,82.0,82.9,83.1,83.5,82.8,82.3,81.9]
	df_17_q = [7.5,7.9,7.9,7.7,7.5,7.4,7.5,8.2,8.7,8.7,8.7,8.9,8.6,8.9,9.0,9.7,9.9,10.1] 


	years_17 = list(range(2001,2019))

	fig_17 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_17.add_trace(go.Bar(x=years_17, y=df_17_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_17.add_trace(go.Bar(x=years_17, y=df_17_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_17.add_trace(go.Bar(x=years_17, y=df_17_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_17.add_trace(go.Bar(x=years_17, y=df_17_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_17.update_yaxes(range=[0, 90], row=1, col=1)
	fig_17.update_yaxes(range=[0, 50], row=1, col=2)
	fig_17.update_yaxes(range=[0, 50], row=2, col=1)
	fig_17.update_yaxes(range=[0, 50], row=2, col=2)

	# Update title and height
	fig_17.update_layout(title_text="Figure 17: Share of Total Real GDP by Sector for Clark County, 2001 to 2018. Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_17.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)




	fig_17.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)


	
	plot_div17 = plot(fig_17, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# blue_collar_bar_18 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_18_blue_collar_bar.csv')
	# lower_skill_bar_18 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_18_lower_skill_bar.csv')
	# knowledge_based_bar_18 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_18_knowledge_based_bar.csv')


	# fig_18 = go.Figure(data=[
 #    go.Bar(x=blue_collar_bar_18['Year'], y=blue_collar_bar_18['% Share of GDP by Sector'], text=blue_collar_bar_18['% Share of GDP by Sector'], name="Blue-collar Services", marker=go.bar.Marker(color='rgb(165,15,21)')),
 #    go.Bar(x=lower_skill_bar_18['Year'], y=lower_skill_bar_18['% Share of GDP by Sector'], text=lower_skill_bar_18['% Share of GDP by Sector'], name="Lower-wage Services", marker=go.bar.Marker(color='rgb(203,24,29)')),
 #    go.Bar(x=knowledge_based_bar_18['Year'], y=knowledge_based_bar_18['% Share of GDP by Sector'], text=knowledge_based_bar_18['% Share of GDP by Sector'], name='Knowledge-based Services', marker=go.bar.Marker(color='rgb(124,123,122)'))


	# ])
	# # Change the bar mode
	# fig_18.update_layout(barmode='stack')
	# fig_18.update_layout(title_text="Figure 18: Breakdown of Clark County's Service Sector as Composition of GDP", )

	blue_collar_bar_18 = [10.0,10.1,9.7,10.4,10.1,10.1,10.2,10.8,11.1,11.9,11.3,11.9,11.6,11.7,11.6,11.6,11.9,11.5]
	lower_skill_bar_18 = [36.7,36.3,35.2,34.4,33.9,33.1,31.9,31.6,31.2,32.9,33.8,34.0,34.5,34.9,34.5,33.4,32.9,31.6]
	knowledge_based_bar_18 = [31.5,31.8,32.8,32.1,32.2,33.7,34.6,34.8,35.3,34.9,36.1,36.1,36.8,36.4,37.4,37.9,37.6,38.8] 

	blue_collar_bar_18_labels = ["10.0%","10.1%","9.7%","10.4%","10.1%","10.1%","10.2%","10.8%","11.1%","11.9%","11.3%","11.9%","11.6%","11.7%","11.6%","11.6%","11.9%","11.5%"]
	lower_skill_bar_18_labels = ["36.7%","36.3%","35.2%","34.4%","33.9%","33.1%","31.9%","31.6%","31.2%","32.9%","33.8%","34.0%","34.5%","34.9%","34.5%","33.4%","32.9%","31.6%"]
	knowledge_based_bar_18_labels = ["31.5%","31.8%","32.8%","32.1%","32.2%","33.7%","34.6%","34.8%","35.3%","34.9%","36.1%","36.1%","36.8%","36.4%","37.4%","37.9%","37.6%","38.8%"] 

	years_18 = list(range(2001,2019))

	fig_18 = go.Figure(data=[
	    go.Bar(x=years_18, y=blue_collar_bar_18, text=blue_collar_bar_18_labels, name="Blue-collar Services", marker=go.bar.Marker(color='rgb(165,15,21)')),
	    go.Bar(x=years_18, y=lower_skill_bar_18, text=lower_skill_bar_18_labels, name="Lower-wage Services", marker=go.bar.Marker(color='rgb(203,24,29)')),
	    go.Bar(x=years_18, y=knowledge_based_bar_18, text=knowledge_based_bar_18_labels, name='Knowledge-based Services', marker=go.bar.Marker(color='rgb(124,123,122)'))


	])
	# Change the bar mode
	fig_18.update_layout(barmode='stack')
	fig_18.update_layout(title_text="Figure 18: Breakdown of Clark County's Service Sector as Composition of GDP", )

	fig_18.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)
	
	plot_div18 = plot(fig_18, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# quat_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_quat.csv')
	# tertiary_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_tert.csv')
	# secondary_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_sec.csv')
	# primary_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_primary.csv')


	# fig_19 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_19.add_trace(go.Bar(x=quat_bar_19['Year'], y=quat_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_19.add_trace(go.Bar(x=tertiary_bar_19['Year'], y=tertiary_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_19.add_trace(go.Bar(x=secondary_bar_19['Year'], y=secondary_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_19.add_trace(go.Bar(x=primary_bar_19['Year'], y=primary_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_19.update_yaxes(range=[0, 80], row=1, col=1)
	# fig_19.update_yaxes(range=[0, 60], row=1, col=2)
	# fig_19.update_yaxes(range=[0, 10], row=2, col=1)
	# fig_19.update_yaxes(range=[0, 60], row=2, col=2)

	# # Update title and height
	# fig_19.update_layout(title_text="Figure 19: Share of Total Real GDP by Sector for Middlesex County, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)

	df_19_p = [.2,.2,.2,.3,.2,.3,.3,.3,.4,.2,.1,.1,.1,.1,.1,.1,.1,.1]
	df_19_s = [16.2,16.6,17.8,17.1,16.9,17.1,18.8,17.6,17.2,17.9,17.8,17.8,17.4,17.8,18.1,17.6,17.5,17.0]
	df_19_t = [62.5,60.9,60.1,59.3,57.7,57.6,55.1,54.1,54.5,52.8,53.0,52.6,52.8,52.3,51.4,50.8,49.9,49.2]
	df_19_q = [25.2,25.2,23.5,25.0,26.3,25.9,26.0,28.1,28.1,29.1,29.1,29.5,29.7,30.0,30.6,31.6,32.6,33.9] 


	years_19 = list(range(2001,2019))

	fig_19 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_19.add_trace(go.Bar(x=years_19, y=df_19_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_19.add_trace(go.Bar(x=years_19, y=df_19_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_19.add_trace(go.Bar(x=years_19, y=df_19_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_19.add_trace(go.Bar(x=years_19, y=df_19_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_19.update_yaxes(range=[0, 70], row=1, col=1)
	fig_19.update_yaxes(range=[0, 50], row=1, col=2)
	fig_19.update_yaxes(range=[0, 50], row=2, col=1)
	fig_19.update_yaxes(range=[0, 50], row=2, col=2)

	fig_19.update_layout(title_text="Figure 19: Share of Total Real GDP by Sector for Middlesex County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)


	fig_19.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
	                  marker_line_width=1.5, opacity=0.6)

	fig_19.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)
	
	plot_div19 = plot(fig_19, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# quat_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_quat.csv')
	# tertiary_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_tert.csv')
	# secondary_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_sec.csv')
	# primary_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_primary.csv')


	# fig_20 = make_subplots(rows=2, cols=2, 
 #                    start_cell="bottom-left",
 #                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	# fig_20.add_trace(go.Bar(x=quat_bar_20['Year'], y=quat_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=2)

	# fig_20.add_trace(go.Bar(x=tertiary_bar_20['Year'], y=tertiary_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=1, col=1)

	# fig_20.add_trace(go.Bar(x=secondary_bar_20['Year'], y=secondary_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=2)

	# fig_20.add_trace(go.Bar(x=primary_bar_20['Year'], y=primary_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	#               row=2, col=1)

	# # Update yaxis properties
	# fig_20.update_yaxes(range=[0, 80], row=1, col=1)
	# fig_20.update_yaxes(range=[0, 60], row=1, col=2)
	# fig_20.update_yaxes(range=[0, 10], row=2, col=1)
	# fig_20.update_yaxes(range=[0, 60], row=2, col=2)

	# # Update title and height
	# fig_20.update_layout(title_text="Figure 20: Share of Total Real GDP by Sector for Allegheny County, 2001 to 2018.  Source: BEA.", 
	#                   height=700,
	#                   showlegend=False)



	# fig_20.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	# fig_20.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)

	df_20_p = [.5,.4,.3,.3,.3,.4,.4,.3,.5,.5,.6,.7,.7,.7,1.1,1.1,1.0,1.0]
	df_20_s = [15.2,15.4,15.9,15.3,13.4,13.1,13.1,13.0,11.8,11.5,11.5,11.3,11.5,11.9,11.1,11.1,11.1,11.1]
	df_20_t = [71.5,70.9,70.4,69.9,71.0,71.7,71.0,69.3,70.1,69.9,69.8,69.7,69.7,69.6,70.2,69.3,69.5,69.1]
	df_20_q = [13.8,14.2,14.1,14.9,15.4,15.3,15.9,17.5,17.7,18.2,18.1,18.3,18.1,17.8,17.7,18.5,18.4,19.2] 


	years_20 = list(range(2001,2019))

	fig_20 = make_subplots(rows=2, cols=2, 
	                    start_cell="bottom-left",
	                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_20.add_trace(go.Bar(x=years_20, y=df_20_q, text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_20.add_trace(go.Bar(x=years_20, y=df_20_t, text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_20.add_trace(go.Bar(x=years_20, y=df_20_s, text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_20.add_trace(go.Bar(x=years_20, y=df_20_p, text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_20.update_yaxes(range=[0, 90], row=1, col=1)
	fig_20.update_yaxes(range=[0, 50], row=1, col=2)
	fig_20.update_yaxes(range=[0, 50], row=2, col=1)
	fig_20.update_yaxes(range=[0, 50], row=2, col=2)

	fig_20.update_layout(title_text="Figure 20: Share of Total Real GDP by Sector for Allegheny County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)


	fig_20.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
	                  marker_line_width=1.5, opacity=0.6)

	fig_20.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	# fig_20.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
 #                  marker_line_width=1.5, opacity=0.6)
	
	plot_div20 = plot(fig_20, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# santa_clara_emp_by_gdp_21 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_21.csv')

	# fig_21 = go.Figure()
	# fig_21.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_21['Year'], y=santa_clara_emp_by_gdp_21['Total Employment'] *500, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	# fig_21.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_21['Year'], y=santa_clara_emp_by_gdp_21['% Share of GDP by Sector'], line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	# fig_21.update_yaxes(range=[50000000, 300000000])
	# fig_21.update_layout(title_text="Figure 21: Santa Clara County’s Information Technology(or Quaternary) Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018")

	# fig_21.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)
	gdp_total_21 = [100,94,104,116,123,136,148,163,157,185,210,208,261,295,337,372,416,490]
	total_emp_21 = [100,86,83,84,84,88,95,97,93,94,99,100,110,117,126,129,135,142]

	years_21 = list(range(2001,2019))

	fig_21 = go.Figure()
	fig_21.add_trace(go.Scatter(x=years_21, y=total_emp_21, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	fig_21.add_trace(go.Scatter(x=years_21, y=gdp_total_21, line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_21.update_layout(title_text="Figure 21: Santa Clara County’s Information Technology (or Quaternary) Sector, Employment v. Total GDP (2001 = 100, in 2012$).<br> Source: BEA, 2001 to 2018")

	fig_21.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)


	plot_div21 = plot(fig_21, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# santa_clara_emp_by_gdp_22 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_22.csv')


	# fig_22 = go.Figure()
	# fig_22.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_22['Year'], y=santa_clara_emp_by_gdp_22['Total Employment'] *350, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	# fig_22.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_22['Year'], y=santa_clara_emp_by_gdp_22['% Share of GDP by Sector'], line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	# fig_22.update_layout(title_text="Figure 22: Santa Clara County’s Manufacturing(or Secondary) Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018")

	# fig_22.update_yaxes(range=[50000000, 300000000])

	gdp_total_22 = [100,91,101,105,122,136,159,171,173,191,207,223,239,258,285,306,325,353]
	total_emp_22 = [100,86,75,73,75,75,75,74,67,65,67,68,68,70,72,74,75,77]

	fig_22 = go.Figure()
	fig_22.add_trace(go.Scatter(x=years_21, y=total_emp_22, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	fig_22.add_trace(go.Scatter(x=years_21, y=gdp_total_22, line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_22.update_layout(title_text="Figure 22: Santa Clara County’s Manufacturing (or Secondary) Sector, Employment v. Total GDP (2001 = 100, in 2012$). <br>Source: BEA, 2001 to 2018")

	fig_22.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div22 = plot(fig_22, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# cuya_emp_by_gdp_23 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_23.csv')


	# fig_23 = go.Figure()
	# fig_23.add_trace(go.Scatter(x=cuya_emp_by_gdp_23['Year'], y=cuya_emp_by_gdp_23['Total Employment'] *1100, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	# fig_23.add_trace(go.Scatter(x=cuya_emp_by_gdp_23['Year'], y=cuya_emp_by_gdp_23['% Share of GDP by Sector'] *1.8, line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	# fig_23.update_layout(title_text='Figure 23: Cuyahoga County’s Information Technology Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018')

	# fig_23.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	gdp_total_23 = [100,103,102,102,103,102,107,117,115,116,121,119,121,119,123,127,131,133]
	total_emp_23 = [100,94,91,90,91,92,94,95,88,86,87,88,91,91,92,92,93,93]

	fig_23 = go.Figure()
	fig_23.add_trace(go.Scatter(x=years_21, y=total_emp_23, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	fig_23.add_trace(go.Scatter(x=years_21, y=gdp_total_23, line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_23.update_layout(title_text="Figure 23: Cuyahoga County’s Information Technology (or Quaternary) Sector, Employment v. Total GDP (2001 = 100, in 2012$).<br>Source: BEA, 2001 to 2018")

	fig_23.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)


	plot_div23 = plot(fig_23, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# cuya_emp_by_gdp_24 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_24.csv')


	# fig_24 = go.Figure()
	# fig_24.add_trace(go.Scatter(x=cuya_emp_by_gdp_24['Year'], y=cuya_emp_by_gdp_24['Total Employment']*385, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	# fig_24.add_trace(go.Scatter(x=cuya_emp_by_gdp_24['Year'], y=cuya_emp_by_gdp_24['% Share of GDP by Sector'], line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total Employment')) # fill to trace0 y

	# fig_24.update_layout(title_text='Figure 24: Cuyahoga County’s Manufacturing Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018')

	# fig_24.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	gdp_total_24 = [100,99,101,102,100,99,100,95,74,78,81,79,80,82,81,80,80,83]
	total_emp_24 = [100,92,88,87,85,84,82,79,69,67,69,70,71,71,71,70,69,72]

	fig_24 = go.Figure()
	fig_24.add_trace(go.Scatter(x=years_21, y=total_emp_24, line=dict(color='rgb(81,80,80)'), name='Total Employment')) # fill down to xaxis
	fig_24.add_trace(go.Scatter(x=years_21, y=gdp_total_24, line=dict(color='rgb(203,24,29)'), fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_24.update_layout(title_text="Figure 24: Cuyahoga County’s Manufacturing (or Secondary) Sector, Employment v. Total GDP (2001 = 100, in 2012$).<br>Source: BEA, 2001 to 2018")

	fig_24.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)

	plot_div24 = plot(fig_24, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	cuya_secondary_26 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_26_cuya.csv')
	oh_secondary_26 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_26_oh.csv')
	usa_secondary_26 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_26_us.csv')


	fig_26 = go.Figure()
	# Create and style traces
	fig_26.add_trace(go.Scatter(x=cuya_secondary_26['Year'], y=cuya_secondary_26['% of total'], name='Cuyahoga County',
                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_26.add_trace(go.Scatter(x=oh_secondary_26['Year'], y=oh_secondary_26['% of total'], name = 'Ohio',
                         line=dict(color='rgb(81,80,80)', width=4, dash='dash')))
	fig_26.add_trace(go.Scatter(x=usa_secondary_26['Year'], y=usa_secondary_26['% of total'], name='United States',
                         line=dict(color='rgb(102,101,101)', width=4)))

	fig_26.update_layout(title_text='Figure 25: Percent of All Private Sector Employment that is in the Manufacturing (or Secondary), Sector.<br>Source: BEA, 1969-2018')

	fig_26.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div26 = plot(fig_26, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	years_27 = list(range(1969, 2019))

	cle_27 = [.51, .48, .46, .46, .46, .46, .44, .45, .45, .46, .45, .43, .43, .41, .39, .39, .39, .38, .37, .36, .36, .34, .33, .32, .32, .31, .30, .29, .29, .28, .28, .27, .22, .21, .20, .20, .20, .19, .19, .18, .16, .16, .17, .16, .17, .16, .16, .16, .15, .16]
	oh_27 = [.55, .53, .51, .51, .52, .51, .49, .49, .50, .50, .49, .48, .48, .46, .45, .46, .45, .45, .43, .43, .42, .41, .40, .40, .39, .39, .38, .37, .37, .36, .35, .35, .30, .29, .29, .29, .29, .28, .27, .26, .23, .23, .23, .23, .23, .24, .24, .24, .24, .24]
	us_27 = [.43, .42, .40, .40, .41, .40, .39, .39, .39, .39, .39, .38, .37, .36, .35, .35, .35, .34, .33, .33, .32, .31, .30, .30, .29, .29, .28, .28, .27, .27, .26, .26, .24, .23, .23, .23, .22, .22, .22, .21, .19, .19, .19, .18, .18, .18, .19, .18, .18, .18]

	fig_27 = go.Figure()
	fig_27.add_trace(go.Scatter(x=years_27, y=cle_27, name='Cuyahoga County',
	                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_27.add_trace(go.Scatter(x=years_27, y=oh_27, name = 'Ohio',
	                         line=dict(color='rgb(81,80,80)', width=4, dash='dash')))
	fig_27.add_trace(go.Scatter(x=years_27, y=us_27, name='U.S.',
	                         line=dict(color='rgb(102,101,101)', width=4)))

	fig_27.update_layout(title_text='Figure 26: Percent of All Private Earnings from the Manufacturing (or Secondary), Sector.Source: BEA, 1969-2018')

	fig_27.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div27 = plot(fig_27, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	usa_secondary_28 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_28_secondary.csv')
	usa_tert_28 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_28_tert.csv')

	fig_28 = go.Figure()

	fig_28.add_trace(go.Scatter(x=usa_secondary_28['Year'], y=usa_secondary_28['Secondary Employment Total'], name='Secondary Employment',
                         line=dict(color='rgb(59,59,59)', width=4, dash='dot')))
	fig_28.add_trace(go.Scatter(x=usa_tert_28['Year'], y=usa_tert_28['Tertiary Employment Total'], name = 'Tertiary Employment',
                         line=dict(color='rgb(38,38,38)', width=4, dash='dash')))

	fig_28.update_layout(title_text='Figure 27: Total Private Sector Employment in U.S. in the Manufacturing (or Secondary) and Service (or Tertiary) Sector. Source: BEA, 1969-2018')


	fig_28.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div28 = plot(fig_28, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	ohio_secondary_29 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_29_secondary.csv')
	ohio_tert_29 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_29_tert.csv')


	fig_29 = go.Figure()
	# Create and style traces
	fig_29.add_trace(go.Scatter(x=ohio_secondary_29['Year'], y=ohio_secondary_29['Secondary Employment Total'], name='Secondary Employment',
                         line=dict(color='rgb(59,59,59)', width=4, dash='dot')))
	fig_29.add_trace(go.Scatter(x=ohio_tert_29['Year'], y=ohio_tert_29['Tertiary Employment Total'], name = 'Tertiary Employment',
                         line=dict(color='rgb(38,38,38)', width=4, dash='dash')))

	fig_29.update_layout(title_text='Figure 28: Total Private Sector Employment in Ohio in the Manufacturing (or Secondary) and Service (or Tertiary) Sector. Source: BEA, 1969-2018')


	fig_29.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div29 = plot(fig_29, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	cuya_secondary_30 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_30_secondary.csv')
	cuya_tert_30 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_30_tert.csv')
	
	fig_30 = go.Figure()
	fig_30.add_trace(go.Scatter(x=cuya_secondary_30['Year'], y=cuya_secondary_30['Secondary Employment Total'], name='Secondary Employment',
                         line=dict(color='rgb(59,59,59)', width=4, dash='dot')))
	fig_30.add_trace(go.Scatter(x=cuya_tert_30['Year'], y=cuya_tert_30['Tertiary Employment Total'], name = 'Tertiary Employment',
                         line=dict(color='rgb(38,38,38)', width=4, dash='dash')))

	fig_30.update_layout(title_text='Figure 29: Total Private Sector Employment in Cuyahoga County in the Manufacturing (or Secondary) and Service (or Tertiary) Sector.<br> Source: BEA, 1969-2018')


	fig_30.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div30 = plot(fig_30, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	cuya_knowledge_based_31 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_31_knowledge.csv')
	cuya_lower_skill_31 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_31_low.csv')
	cuya_blue_collar_31 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_31_blue.csv')
	cuya_secondary_31 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_31_secondary.csv')
	cuya_quat_31 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_31_quat.csv')


	fig_31 = go.Figure()

	fig_31.add_trace(go.Scatter(x=cuya_knowledge_based_31['Year'], y=cuya_knowledge_based_31['Knowledge Based Employment Total'], line=dict(color='rgb(255,255,255)'), fill='tozeroy', name='Knowledge Based')) 
	fig_31.add_trace(go.Scatter(x=cuya_lower_skill_31['Year'], y=cuya_lower_skill_31['Lower Skill Employment Total'], line=dict(color='rgb(230,0,0)'), fill='tonexty', name='Lower Wage')) 
	fig_31.add_trace(go.Scatter(x=cuya_secondary_31['Year'], y=cuya_secondary_31['Secondary Employment Total'], line=dict(color='rgb(230,210,0)'), fill='tozeroy',name='Secondary'))
	fig_31.add_trace(go.Scatter(x=cuya_quat_31['Year'], y=cuya_quat_31['Quaternary Employment Total'], line=dict(color='rgb(0,0,0)'), fill='tozeroy',name='Quaternary'))# fill down to xaxis
	fig_31.add_trace(go.Scatter(x=cuya_blue_collar_31['Year'], y=cuya_blue_collar_31['Blue Collar Employment Total'], line=dict(color='rgb(160,200,255)'), fill='tozeroy', name='Blue Collar')) 

	fig_31.update_layout(title_text='Figure 30: Cuyahoga County Private Sector Employment by Sector. Source BEA, 2001 to 2018.')


	fig_31.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div31 = plot(fig_31, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	# cuya_2001_lower_skill_32 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_32_lower.csv')
	# cuya_2001_knowledge_based_32 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_32_knowledge.csv')


	# fig_32 = go.Figure()
	# fig_32.add_trace(go.Scatter(x=cuya_2001_lower_skill_32['Year'], y=cuya_2001_lower_skill_32['% of total'], line=dict(color='rgb(203,24,29)'), name='Lower Skill')) 
	# fig_32.add_trace(go.Scatter(x=cuya_2001_knowledge_based_32['Year'], y=cuya_2001_knowledge_based_32['% of total'], line=dict(color='rgb(38,38,38)'), fill='tonexty',name='Knowledge Based'))

	# fig_32.update_layout(title_text='Figure 31: Cuyahoga County Private Sector Employment by Sector. Source BEA, 2001 to 2018.')


	# fig_32.update_layout(

	#     font=dict(
	#         family="EB Garamond, serif",
	#         size=12,
	#         color="#212121"
	#     ),
	#     autosize=True,
	    
	#     uniformtext_minsize=8,
	#     uniformtext_mode='hide',
	#     paper_bgcolor='rgba(0,0,0,0)',
 #        plot_bgcolor='rgba(0,0,0,0)',
	# 	)

	cuya_2001_lower_skill_32 = [30,30,30,30,30,30,30,29,29,29,29,29,29,30,29,29,29,29]
	cuya_2001_knowledge_based_32 = [32,34,34,35,35,36,36,37,39,39,39,39,39,39,39,39,39,39]

	cuya_2001_lower_skill_32_labels = ["30%","30%","30%","30%","30%","30%","30%","29%","29%","29%","29%","29%","29%","30%","29%","29%","29%","29%"]
	cuya_2001_knowledge_based_32_labels = ["32%","34%","34%","35%","35%","36%","36%","37%","39%","39%","39%","39%","39%","39%","39%","39%","39%","39%"]

	fig_32 = go.Figure()
	fig_32.add_trace(go.Scatter(x=years_21, y=cuya_2001_lower_skill_32, text=cuya_2001_lower_skill_32_labels, line=dict(color='rgb(203,24,29)'), name='Lower Skill')) 
	fig_32.add_trace(go.Scatter(x=years_21, y=cuya_2001_knowledge_based_32, text=cuya_2001_knowledge_based_32_labels, line=dict(color='rgb(38,38,38)'), fill='tonexty',name='Knowledge Based'))

	fig_32.update_layout(title_text='Figure 31: Proportion of Private Sector Jobs that are in Knowledge-based versus Lower-wage Services in Cuyahoga County.<br>Source: BEA, 2001 to 2018.')


	fig_32.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
	        plot_bgcolor='rgba(0,0,0,0)',
	)

	fig_32.update_yaxes(range=[25, 50])



	plot_div32 = plot(fig_32, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	usa_2001_lower_skill_33 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_33_lower.csv')
	usa_2001_knowledge_based_33 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_33_knowledge.csv')


	fig_33 = go.Figure()
	fig_33.add_trace(go.Scatter(x=usa_2001_lower_skill_33['Year'], y=usa_2001_lower_skill_33['% of total'], line=dict(color='rgb(203,24,29)'), name='Lower Wage')) 
	fig_33.add_trace(go.Scatter(x=usa_2001_knowledge_based_33['Year'], y=usa_2001_knowledge_based_33['% of total'], line=dict(color='rgb(38,38,38)'), fill='tonexty',name='Knowledge Based'))

	fig_33.update_layout(title_text='Figure 32: Proportion of Private Sector Jobs that are in Knowledge-based versus Lower-wage Services in the U.S. Source: BEA, 2001 to 2018')


	fig_33.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div33 = plot(fig_33, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	ohio_2001_lower_skill_34 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_34_lower.csv')
	ohio_2001_knowledge_based_34 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_34_knowledge.csv')



	fig_34 = go.Figure()
	fig_34.add_trace(go.Scatter(x=ohio_2001_lower_skill_34['Year'], y=ohio_2001_lower_skill_34['% of total'], line=dict(color='rgb(203,24,29)'), name='Lower Wage')) 
	fig_34.add_trace(go.Scatter(x=ohio_2001_knowledge_based_34['Year'], y=ohio_2001_knowledge_based_34['% of total'], line=dict(color='rgb(38,38,38)'), fill='tonexty',name='Knowledge Based'))


	fig_34.update_layout(title_text='Figure 33: Proportion of Private Sector Jobs that are in Knowledge-based versus Lower-wage Services in Ohio Source: BEA, 2001 to 2018')


	fig_34.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div34 = plot(fig_34, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	income_by_jobs_35 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_35.csv')

	fig_35 = px.scatter(income_by_jobs_35, x="% Jobs in Knowledge-based Services", y="Real Per Capita Income", color="GeoName",
                 hover_data=['GeoName'])

	fig_35.update_xaxes(range=[20, 45])
	fig_35.update_layout(showlegend=False)

	fig_35.update_layout(title_text='Figure 34: Real Per Capita Income v. % of Knowledge-based Service Jobs by State.  Source: BEA, 2018.')


	fig_35.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    xaxis =  {                                     
                  'showgrid': False
                                         },
        yaxis = {                              
                  'showgrid': False
                },
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_35.update_traces(mode='markers', marker_line_width=2, marker_size=8)


	plot_div35 = plot(fig_35, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	state_emp_percent_36 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_36.csv')

	fig_36 = px.bar(state_emp_percent_36, x='GeoName', y='% Jobs in Knowledge-based Services',
             hover_data=["GeoName", "% Jobs in Knowledge-based Services"],
             height=700,
             color='% Jobs in Knowledge-based Services',
             # color_discrete_sequence=px.colors.qualitative.Antique,
             title='Figure 35: Proportion of Private Sector Jobs that are in Knowledge-based Services in Big-City Counties. Source: BEA, 2018')

	fig_36.update_yaxes(title_text="")
	fig_36.update_xaxes(title_text="", tickangle=45)
	fig_36.update_layout(showlegend=False)

	fig_36.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)

	fig_36.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div36 = plot(fig_36, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	
	state_emp_percent_37 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_37.csv')

	fig_37 = px.bar(state_emp_percent_37, x='GeoName', y='% Jobs in Knowledge-based Services',
             hover_data=["GeoName", "% Jobs in Knowledge-based Services"],
             height=700,
             color='% Jobs in Knowledge-based Services',
             color_discrete_sequence=px.colors.qualitative.Antique,
             title='Figure 36: Proportion of Private Sector Jobs that are in Information Technology in Big-City Counties. Source: BEA, 2018')

	fig_37.update_yaxes(title_text="")
	fig_37.update_xaxes(title_text="", tickangle=45)
	fig_37.update_layout(showlegend=False)

	fig_37.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)

	fig_37.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div37 = plot(fig_37, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	fig_39_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_39.csv')

	fig_39 = go.Figure(data=go.Scatter(x=fig_39_df['observation_date'], y=fig_39_df['LNU04032241']))
	fig_39.update_traces(marker_color='rgb(81,80,80)')

	fig_39.update_layout(title_text='Figure 38: Unemployment Rate for Leisure and Hospitality Workers, January 2001 to May 2020. Source: BLS.')

	fig_39.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div39 = plot(fig_39, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_41_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_41.csv')


	fig_41 = px.bar(fig_41_df, x='GeoName', y='% Jobs in Lower-wage Services',
             hover_data=["GeoName", "% Jobs in Lower-wage Services"],
             height=600,
             color='% Jobs in Lower-wage Services',
             color_discrete_sequence=px.colors.qualitative.Antique,
             title='Figure 40: Proportion of Private Sector Jobs that are in Lower-wage Services in Big-City Counties. Source: BEA, 2018')

	fig_41.update_yaxes(title_text="")
	fig_41.update_xaxes(title_text="")
	fig_41.update_layout(showlegend=False)

	fig_41.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)

	fig_41.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    # uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div41 = plot(fig_41, output_type='div', include_plotlyjs=False, show_link=False, link_text="")




	fig_42_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_42.csv')


	fig_42 = go.Figure(data=go.Scatter(x=fig_42_df['observation_date'], y=fig_42_df['ICSA']))
	fig_42.update_traces(marker_color='rgb(81,80,80)')
	fig_42.update_yaxes(range=[0, 3000000])
	fig_42.update_layout(title_text='Figure 41: Initial Unemployment Claims (Monthly) Jan 1967 to April 2020. Source U.S. Employment and Training Organization')

	fig_42.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div42 = plot(fig_42, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	df_no_US = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_43.csv')
	df_life_exp_US = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_43_us.csv')


	fig_43 = go.Figure()
	fig_43.add_trace(go.Scatter(x=df_no_US['TIME'], y=df_no_US['Value'],
                    mode='lines',
                    name='Other Nations', line=dict(color='#9e9e9e', width=1)))
	fig_43.add_trace(go.Scatter(x=df_life_exp_US['TIME'], y=df_life_exp_US['Value'],
                    mode='lines',
                    name='USA',line=dict(color='#d32f2f', width=3)))

	fig_43.update_layout(hovermode="x unified", showlegend=False)

	fig_43.update_layout(title_text='Figure 42: Initial Unemployment Claims (Monthly) Jan 1967 to April 2020. Source U.S. Employment and Training Organization')

	fig_43.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div43 = plot(fig_43, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_44_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_44.csv')

	fig_44 = go.Figure(data=go.Scatter(x=fig_44_df['observation_date'], y=fig_44_df['LNS11300001']))
	fig_44.update_traces(marker_color='rgb(81,80,80)')
	fig_44.update_xaxes(title='Male')
	fig_44.update_layout(title_text='Figure 43: Male Labor Force Participation Rate Jan. 1948 to May 2020. Source: Bureau of Labor Statistics')

	fig_44.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div44 = plot(fig_44, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	composite_50 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_50.csv')


	fig_50 = px.scatter(composite_50, x="Life expectancy at birth", y="Health spending per capita", color="Country",
                 hover_data=['Country'], trendline="lowess")

	fig_50.update_layout(showlegend=False)

	fig_50.update_layout(title_text='Figure 49: Life expectancy versus health spending per capita. Source: OECD, 2018')

	fig_50.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    xaxis =  {                                     
                  'showgrid': False
                                         },
        yaxis = {                              
                  'showgrid': False
                },
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)
	fig_50.update_traces(mode='markers', marker_line_width=2, marker_size=8)

	plot_div50 = plot(fig_50, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	fig_51_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_51.csv')


	# Create figure with secondary y-axis
	fig_51 = make_subplots(specs=[[{"secondary_y": True}]])

	# Add traces
	fig_51.add_trace(
	    go.Scatter(x=fig_51_df['Current $millions'], y=fig_51_df['Federal'], line=dict(color='rgb(102,101,101)'), name="% Federal"),
	    secondary_y=True,
	    
	)

	fig_51.add_trace(
	    go.Scatter(x=fig_51_df['Current $millions'], y=fig_51_df['Private'], line=dict(color='rgb(81,80,80)'), name="% Private"),
	    secondary_y=True,
	    
	)

	fig_51.add_trace(
	    go.Scatter(x=fig_51_df['Current $millions'], y=fig_51_df['Total Funding'], line=dict(color='rgb(203,24,29)', width=1), name="Total Funding", fill='tonexty'),
	    secondary_y=False,
	)
	# Add figure title
	fig_51.update_layout(
	    title_text="Figure 50: R&D Funding Source, 1953-2016. Source: NSF"
	)

	# Set y-axes titles
	fig_51.update_yaxes(title_text="R&D Funding (billions in 2009$)", secondary_y=False)

	fig_51.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div51 = plot(fig_51, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_52_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_52.csv')

	fig_52 = go.Figure(data=go.Scatter(x=fig_52_df['Year'], y=fig_52_df['sptinc_z_US\nPre-tax national income \nTop 1% | share\nUSA']))
	fig_52.update_traces(marker_color='rgb(81,80,80)')

	fig_52.update_layout(
	    title_text="Figure 51: Top 1% National Income Share, USA, 1914-2018. Source: World Inequality Database."
	)

	fig_52.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div52 = plot(fig_52, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_53_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_53.csv')

	fig_53 = go.Figure(data=go.Scatter(x=fig_53_df['observation_date'], y=fig_53_df['WASCUR_GDP']))
	fig_53.update_traces(marker_color='rgb(81,80,80)')

	fig_53.update_layout(
	    title_text="Figure 52: Wages and Salary Income as Precent of Gross Domestic Product, 1947-2019. Source: Federal Reserve Bank of St. Louis."
	)

	fig_53.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div53 = plot(fig_53, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	cle_54 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_54_cle.csv')
	oh_54 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_54_oh.csv')
	usa_54 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_54_us.csv')


	fig_54 = go.Figure()
	# Create and style traces
	fig_54.add_trace(go.Scatter(x=cle_54['Year'], y=cle_54['% of total'], name='Cleveland Salary and Wages',
	                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_54.add_trace(go.Scatter(x=oh_54['Year'], y=oh_54['% of total'], name = 'Ohio Salary and Wages',
	                         line=dict(color='rgb(59,59,59)', width=4, dash='dash')))
	fig_54.add_trace(go.Scatter(x=usa_54['Year'], y=usa_54['% of total'], name='US Salary and Wages',
	                         line=dict(color='rgb(38,38,38)', width=4))) # dash options include 'dash', 'dot', and 'dashdot'
	fig_54.update_layout(
	    title_text="Figure 53:  Percent of Total Income from Salaries and Wages, 1969-2018. Source: BEA"
	)


	fig_54.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div54 = plot(fig_54, output_type='div', include_plotlyjs=False, show_link=False, link_text="")



	cle_55 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_55_cle.csv')
	oh_55 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_55_oh.csv')
	usa_55 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_55_us.csv')


	fig_55 = go.Figure()
	# Create and style traces
	fig_55.add_trace(go.Scatter(x=cle_55['Year'], y=cle_55['% of total'], name='Cleveland Salary and Wages',
	                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_55.add_trace(go.Scatter(x=oh_55['Year'], y=oh_55['% of total'], name = 'Ohio Salary and Wages',
	                         line=dict(color='rgb(59,59,59)', width=4, dash='dash')))
	fig_55.add_trace(go.Scatter(x=usa_55['Year'], y=usa_55['% of total'], name='US Salary and Wages',
	                         line=dict(color='rgb(38,38,38)', width=4))) # dash options include 'dash', 'dot', and 'dashdot'
	fig_55.update_layout(
	    title_text="Figure 54:  Percent of Total Income from Personal Transfer Receipts, 1969-2018. Source: BEA"
	)


	fig_55.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div55 = plot(fig_55, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	cle_56 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_56_cle.csv')
	oh_56 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_56_oh.csv')
	usa_56 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_56_us.csv')


	fig_56 = go.Figure()
	# Create and style traces
	fig_56.add_trace(go.Scatter(x=cle_56['Year'], y=cle_56['% of total'], name='Cleveland Salary and Wages',
	                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_56.add_trace(go.Scatter(x=oh_56['Year'], y=oh_56['% of total'], name = 'Ohio Salary and Wages',
	                         line=dict(color='rgb(59,59,59)', width=4, dash='dash')))
	fig_56.add_trace(go.Scatter(x=usa_56['Year'], y=usa_56['% of total'], name='US Salary and Wages',
	                         line=dict(color='rgb(38,38,38)', width=4))) # dash options include 'dash', 'dot', and 'dashdot'
	fig_56.update_layout(
    title_text="Figure 55:  Percent of Total Income from Dividends, Interest and Rent, 1969-2018. Source: BEA"
	)


	fig_56.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div56 = plot(fig_56, output_type='div', include_plotlyjs=False, show_link=False, link_text="")




	fig_57_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_57.csv')

	fig_57 = go.Figure(data=go.Scatter(x=fig_57_df['observation_date'], y=fig_57_df['IPG3254S'], fill='tonexty'))
	fig_57.update_traces(marker_color='rgb(81,80,80)')

	fig_57.update_yaxes(range=[85, 125])

	fig_57.update_layout(
	    title_text="Figure 56: Industrial Production: Pharmaceutical and medicine, 2000 to 2019 (Index 2000 = 100). SOurce: BOard of Governors of the Federal Reserve System (US)"
	)

	fig_57.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div57 = plot(fig_57, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	fig_58_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_58.csv')


	fig_58 = go.Figure(go.Bar(
            x=fig_58_df['R&D 2018/19 (€million)'],
            y=fig_58_df['Company'],
            orientation='h'))

	fig_58.update_layout(
	    title_text="Figure 57: Top Firms by R&D Expenditures (in millions).  Source: European Commission, EU R&D Scoreboard, 2019."
	)

	fig_58.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)

	fig_58.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div58 = plot(fig_58, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	fig_59_hospital = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_59_hospital.csv')
	fig_59_health = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_59_health.csv')
	fig_59_total = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_59_total.csv')


	fig_59 = go.Figure()
	# Create and style traces
	fig_59.add_trace(go.Scatter(x=fig_59_hospital['Year'], y=fig_59_hospital['Annual'], name='Hospitals',
                         line=dict(color='rgb(203,24,29)', width=4, dash='dot')))
	fig_59.add_trace(go.Scatter(x=fig_59_health['Year'], y=fig_59_health['Annual'], name = 'Healthcare and Social Assistance',
                         line=dict(color='rgb(81,80,80)', width=4, dash='dash')))
	fig_59.add_trace(go.Scatter(x=fig_59_total['Year'], y=fig_59_total['Annual'], name='Total',
                         line=dict(color='rgb(102,101,101)', width=4))) # dash options include 'dash', 'dot', and 'dashdot'
	fig_59.update_layout(
    	title_text="Figure 58: Employment Growth in the Cleveland MSA, 1990 to 2019 (Index 1990 = 100). Source: Bureau of Labor Statistics."
	)


	fig_59.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div59 = plot(fig_59, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	fig_60_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_60.csv')


	fig_60 = go.Figure(data=[go.Bar(x=fig_60_df['Area Name New'], y=fig_60_df['Location Quotient'])])
	fig_60.update_traces(marker_color='rgb(16,16,16)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=1.5, opacity=0.6)
	fig_60.update_layout(title_text='Figure 59: Location Quotient of Healthcare Practioners and Technical Operations for Largest 40 Metros. Source:  Occupational Employment and Statistics, May 2019.')
	fig_60.update_xaxes(title_text="", tickangle=45)

	fig_60.update_layout(

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    # width=1500,
	    height=700,
   
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div60 = plot(fig_60, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	life_by_income_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_63.csv')

	
	fig_63 = px.scatter(life_by_income_df, y='Per Capita Income (In 2015 Inflation Adjusted Dollars)', x="Life Expectancy", color="Census Tract", hover_data=['Census Tract'], color_continuous_scale='Rainbow')
	# fig_63.update_layout(title_text='Figure 63: Figure 63: Life Expectancy v. Per Capita Income for Census Tracts in Cuyahoga County.<br>Source: U.S. Small-area Life Expectancy Estimates Project – USALEEP, 2010-2015<br> and ACS 5-Year, 2011-2015.<br>')
	fig_63.update_traces()

	fig_63.update_layout(

		yaxis_title='Per Capita Income',

	    font=dict(
	        family="EB Garamond, serif",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    xaxis =  {                                     
                  'showgrid': False
                                         },
        yaxis = {                              
                  'showgrid': False
                },
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        coloraxis_showscale=False,
		)

	fig_63.update_traces(mode='markers', marker_line_width=2, marker_size=8)

	# fig_63.update_traces(mode='markers', marker_line_width=2, marker_size=8)
	plot_div63 = plot(fig_63, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	context={'plot_div': plot_div,
			 'plot_div2': plot_div2,
			 'plot_div4': plot_div4,
			 'plot_div6': plot_div6,
			 'plot_div7': plot_div7,
			 'plot_div8': plot_div8,
			 'plot_div9': plot_div9,
			 'plot_div10': plot_div10,
			 'plot_div11': plot_div11,
			 'plot_div12': plot_div12,
			 'plot_div13': plot_div13,
			 'plot_div14': plot_div14,
			 'plot_div15': plot_div15,
			 'plot_div16': plot_div16,
			 'plot_div17': plot_div17,
			 'plot_div18': plot_div18,
			 'plot_div19': plot_div19,
			 'plot_div20': plot_div20,
			 'plot_div21': plot_div21,
			 'plot_div22': plot_div22,
			 'plot_div23': plot_div23,
			 'plot_div24': plot_div24,
			 'plot_div26': plot_div26,
			 'plot_div27': plot_div27,
			 'plot_div28': plot_div28,
			 'plot_div29': plot_div29,
			 'plot_div30': plot_div30,
			 'plot_div31': plot_div31,
			 'plot_div32': plot_div32,
			 'plot_div33': plot_div33,
			 'plot_div34': plot_div34,
			 'plot_div35': plot_div35,
			 'plot_div36': plot_div36,
			 'plot_div37': plot_div37,
			 'plot_div39': plot_div39,
			 'plot_div41': plot_div41,
			 'plot_div42': plot_div42,
			 'plot_div43': plot_div43,
			 'plot_div44': plot_div44,
			 'plot_div50': plot_div50,
			 'plot_div51': plot_div51,
			 'plot_div52': plot_div52,
			 'plot_div53': plot_div53,
			 'plot_div54': plot_div54,
			 'plot_div55': plot_div55,
			 'plot_div56': plot_div56,
			 'plot_div57': plot_div57,
			 'plot_div58': plot_div58,
			 'plot_div59': plot_div59,
			 'plot_div60': plot_div60,
			 'plot_div63': plot_div63,


			}


	return HttpResponse(template.render(context, request))

