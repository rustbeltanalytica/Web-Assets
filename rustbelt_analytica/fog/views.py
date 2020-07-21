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

	world_50 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/part_1.csv')

	fig_1 = go.Figure(data=[go.Bar(x=world_50['Country Name'], y=world_50['2018'])])
	fig_1.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)
	fig_1.update_xaxes(title_text="", tickangle=45)

	fig_1.update_layout(
	    title="Figure 2: TOp 1% of Counties by Total Real GDP.  Source: BEA, 2018 (in 2012$)",
	    xaxis_title="",
	    yaxis_title="GDP",
	    font=dict(
	        family="Courier New, monospace",
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
	fig_2.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)
	fig_2.update_xaxes(title_text="", tickangle=45)

	fig_2.update_layout(
	    title="Figure 1: Largest State Economies by Total Real GDP. Source BEA, 2018 (in 2012$)",
	    xaxis_title="",
	    yaxis_title="GDP",
	    font=dict(
	        family="Helvetica, monospace",
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

	pop_by_gdp = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/pop_by_gdp.csv')
	fig8 = px.scatter(pop_by_gdp.reset_index(), x="CAGR_01-10_gdp", y="CAGR_01-10_y", color='GeoName', hover_data=['GeoName']) 

	fig8.update_layout(

	    xaxis_title="Annualized Growth Rate Total Population",
	    yaxis_title="Annualized Growth Rate Per Capita GDP",
	    font=dict(
	        family="Helvetica, monospace",
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
	plot_div8 = plot(fig8, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	quat_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_quat.csv')
	tertiary_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_tert.csv')
	secondary_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_sec.csv')
	primary_bar_10 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_10_primary_bar.csv')



	fig_10 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_10.add_trace(go.Bar(x=quat_bar_10['Year'], y=quat_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_10.add_trace(go.Bar(x=tertiary_bar_10['Year'], y=tertiary_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_10.add_trace(go.Bar(x=secondary_bar_10['Year'], y=secondary_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_10.add_trace(go.Bar(x=primary_bar_10['Year'], y=primary_bar_10['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)


	# Update yaxis properties
	fig_10.update_yaxes(range=[0, 70], row=1, col=1)
	fig_10.update_yaxes(range=[0, 70], row=1, col=2)
	fig_10.update_yaxes(range=[0, 70], row=2, col=1)
	fig_10.update_yaxes(range=[0, 70], row=2, col=2)

	# Update title and height
	fig_10.update_layout(title_text="figure 10: Share of Total Real GDP by Sector for United States, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_10.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_10.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)


	plot_div10 = plot(fig_10, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	quat_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_quat.csv')
	tertiary_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_tert.csv')
	secondary_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_sec.csv')
	primary_bar_11 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_11_primary_bar.csv')

	fig_11 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_11.add_trace(go.Bar(x=quat_bar_11['Year'], y=quat_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_11.add_trace(go.Bar(x=tertiary_bar_11['Year'], y=tertiary_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_11.add_trace(go.Bar(x=secondary_bar_11['Year'], y=secondary_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_11.add_trace(go.Bar(x=primary_bar_11['Year'], y=primary_bar_11['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_11.update_yaxes(range=[0, 50], row=1, col=1)
	fig_11.update_yaxes(range=[0, 50], row=1, col=2)
	fig_11.update_yaxes(range=[0, 50], row=2, col=1)
	fig_11.update_yaxes(range=[0, 50], row=2, col=2)

	# Update title and height
	fig_11.update_layout(title_text="figure 11: Share of Total Real GDP by Sector for Santa Clara County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_11.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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



	fig_11.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)


	plot_div11 = plot(fig_11, output_type='div', include_plotlyjs=False, show_link=False, link_text="")


	quat_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_quat.csv')
	tertiary_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_tert.csv')
	secondary_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_sec.csv')
	primary_bar_12 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_12_primary_bar.csv')

	fig_12 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_12.add_trace(go.Bar(x=quat_bar_12['Year'], y=quat_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_12.add_trace(go.Bar(x=tertiary_bar_12['Year'], y=tertiary_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_12.add_trace(go.Bar(x=secondary_bar_12['Year'], y=secondary_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_12.add_trace(go.Bar(x=primary_bar_12['Year'], y=primary_bar_12['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_12.update_yaxes(range=[0, 70], row=1, col=1)
	fig_12.update_yaxes(range=[0, 60], row=1, col=2)
	fig_12.update_yaxes(range=[0, 1], row=2, col=1)
	fig_12.update_yaxes(range=[0, 60], row=2, col=2)

	# Update title and height
	fig_12.update_layout(title_text="figure 12: Share of Total Real GDP by Sector for San Francisco County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_12.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_12.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)

	

	plot_div12 = plot(fig_12, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	quat_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_quat.csv')
	tertiary_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_tert.csv')
	secondary_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_sec.csv')
	primary_bar_13 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_13_primary_bar.csv')

	fig_13 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_13.add_trace(go.Bar(x=quat_bar_13['Year'], y=quat_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_13.add_trace(go.Bar(x=tertiary_bar_13['Year'], y=tertiary_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_13.add_trace(go.Bar(x=secondary_bar_13['Year'], y=secondary_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_13.add_trace(go.Bar(x=primary_bar_13['Year'], y=primary_bar_13['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_13.update_yaxes(range=[0, 70], row=1, col=1)
	fig_13.update_yaxes(range=[0, 60], row=1, col=2)
	fig_13.update_yaxes(range=[0, 60], row=2, col=1)
	fig_13.update_yaxes(range=[0, 60], row=2, col=2)

	# Update title and height
	fig_13.update_layout(title_text="figure 13: Share of Total Real GDP by Sector for Ohio, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_13.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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


	fig_13.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)


	plot_div13 = plot(fig_13, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	quat_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_quat.csv')
	tertiary_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_tert.csv')
	secondary_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_sec.csv')
	primary_bar_14 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_14_primary_bar.csv')

	fig_14 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_14.add_trace(go.Bar(x=quat_bar_14['Year'], y=quat_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_14.add_trace(go.Bar(x=tertiary_bar_14['Year'], y=tertiary_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_14.add_trace(go.Bar(x=secondary_bar_14['Year'], y=secondary_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_14.add_trace(go.Bar(x=primary_bar_14['Year'], y=primary_bar_14['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_14.update_yaxes(range=[0, 80], row=1, col=1)
	fig_14.update_yaxes(range=[0, 60], row=1, col=2)
	fig_14.update_yaxes(range=[0, 5], row=2, col=1)
	fig_14.update_yaxes(range=[0, 60], row=2, col=2)

	# Update title and height
	fig_14.update_layout(title_text="figure 14: Share of Total Real GDP by Sector for Cuyahoga County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_14.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_14.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)

	plot_div14 = plot(fig_14, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	blue_collar_bar_15 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_15_blue_collar_bar.csv')
	lower_skill_bar_15 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_15_lower_skill_bar.csv')
	knowledge_based_bar_15 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_15_knowledge_based_bar.csv')

	fig_15 = go.Figure(data=[
    go.Bar(x=blue_collar_bar_15['Year'], y=blue_collar_bar_15['% Share of GDP by Sector'], text=blue_collar_bar_15['% Share of GDP by Sector'], name="Blue-collar Services", marker=go.bar.Marker(color='#9b0000')),
    go.Bar(x=lower_skill_bar_15['Year'], y=lower_skill_bar_15['% Share of GDP by Sector'], text=lower_skill_bar_15['% Share of GDP by Sector'], name="Lower-skill Services", marker=go.bar.Marker(color='#d50000')),
    go.Bar(x=knowledge_based_bar_15['Year'], y=knowledge_based_bar_15['% Share of GDP by Sector'], text=knowledge_based_bar_15['% Share of GDP by Sector'], name='Knowledge-based Services', marker=go.bar.Marker(color='#ff5131'))


	])
	# Change the bar mode
	fig_15.update_layout(barmode='stack')

	fig_15.update_layout(title_text="figure 15: Breakdown of Cuyahoga County's Service Sector as Composition of GDP") 

	fig_15.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fire_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_fire.csv')
	health_care_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_health.csv')
	manage_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_manage.csv')
	education_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_ed.csv')
	arts_and_rec_bar_16 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_16_arts.csv')


	fig_16 = go.Figure(data=[
    go.Bar(x=fire_bar_16['Year'], y=fire_bar_16['% Share of GDP by Sector'], text=fire_bar_16['% Share of GDP by Sector'], name="F.I.R.E.", marker=go.bar.Marker(color='#9b0000')),
    go.Bar(x=health_care_bar_16['Year'], y=health_care_bar_16['% Share of GDP by Sector'], text=health_care_bar_16['% Share of GDP by Sector'], name="Health Care", marker=go.bar.Marker(color='#5e35b1')),
    go.Bar(x=manage_bar_16['Year'], y=manage_bar_16['% Share of GDP by Sector'], text=manage_bar_16['% Share of GDP by Sector'], name="Management of Companies", marker=go.bar.Marker(color='#009688')),
    go.Bar(x=education_bar_16['Year'], y=education_bar_16['% Share of GDP by Sector'], text=education_bar_16['% Share of GDP by Sector'], name="Education", marker=go.bar.Marker(color='#4caf50')),
    go.Bar(x=arts_and_rec_bar_16['Year'], y=arts_and_rec_bar_16['% Share of GDP by Sector'], text=arts_and_rec_bar_16['% Share of GDP by Sector'], name="Arts and Recreation", marker=go.bar.Marker(color='#ff5722'))



	])
	# Change the bar mode
	fig_16.update_layout(barmode='stack')
	fig_16.update_layout(title_text="figure 16: Breakdown of Cuyahoga County's Knowledge-Based Services as Composition of GDP")

	fig_16.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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


	quat_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_quat.csv')
	tertiary_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_tert.csv')
	secondary_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_sec.csv')
	primary_bar_17 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_17_primary.csv')

	fig_17 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_17.add_trace(go.Bar(x=quat_bar_17['Year'], y=quat_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_17.add_trace(go.Bar(x=tertiary_bar_17['Year'], y=tertiary_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_17.add_trace(go.Bar(x=secondary_bar_17['Year'], y=secondary_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_17.add_trace(go.Bar(x=primary_bar_17['Year'], y=primary_bar_17['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_17.update_yaxes(range=[0, 80], row=1, col=1)
	fig_17.update_yaxes(range=[0, 60], row=1, col=2)
	fig_17.update_yaxes(range=[0, 50], row=2, col=1)
	fig_17.update_yaxes(range=[0, 60], row=2, col=2)

	# Update title and height
	fig_17.update_layout(title_text="figure 17: Share of Total Real GDP by Sector for Clark County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_17.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_17.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)


	
	plot_div17 = plot(fig_17, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	blue_collar_bar_18 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_18_blue_collar_bar.csv')
	lower_skill_bar_18 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_18_lower_skill_bar.csv')
	knowledge_based_bar_18 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_18_knowledge_based_bar.csv')


	fig_18 = go.Figure(data=[
    go.Bar(x=blue_collar_bar_18['Year'], y=blue_collar_bar_18['% Share of GDP by Sector'], text=blue_collar_bar_18['% Share of GDP by Sector'], name="Blue-collar Services", marker=go.bar.Marker(color='#ff5131')),
    go.Bar(x=lower_skill_bar_18['Year'], y=lower_skill_bar_18['% Share of GDP by Sector'], text=lower_skill_bar_18['% Share of GDP by Sector'], name="Lower-skill Services", marker=go.bar.Marker(color='#d50000')),
    go.Bar(x=knowledge_based_bar_18['Year'], y=knowledge_based_bar_18['% Share of GDP by Sector'], text=knowledge_based_bar_18['% Share of GDP by Sector'], name='Knowledge-based Services', marker=go.bar.Marker(color='#9b0000'))


	])
	# Change the bar mode
	fig_18.update_layout(barmode='stack')
	fig_18.update_layout(title_text="figure 18: Breakdown of Clark County's Service Sector as Composition of GDP", )

	fig_18.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	quat_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_quat.csv')
	tertiary_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_tert.csv')
	secondary_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_sec.csv')
	primary_bar_19 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_19_primary.csv')


	fig_19 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_19.add_trace(go.Bar(x=quat_bar_19['Year'], y=quat_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_19.add_trace(go.Bar(x=tertiary_bar_19['Year'], y=tertiary_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_19.add_trace(go.Bar(x=secondary_bar_19['Year'], y=secondary_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_19.add_trace(go.Bar(x=primary_bar_19['Year'], y=primary_bar_19['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_19.update_yaxes(range=[0, 80], row=1, col=1)
	fig_19.update_yaxes(range=[0, 60], row=1, col=2)
	fig_19.update_yaxes(range=[0, 10], row=2, col=1)
	fig_19.update_yaxes(range=[0, 60], row=2, col=2)

	# Update title and height
	fig_19.update_layout(title_text="Figure 19: Share of Total Real GDP by Sector for Middlesex County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_19.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_19.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)
	
	plot_div19 = plot(fig_19, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	quat_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_quat.csv')
	tertiary_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_tert.csv')
	secondary_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_sec.csv')
	primary_bar_20 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_20_primary.csv')


	fig_20 = make_subplots(rows=2, cols=2, 
                    start_cell="bottom-left",
                    subplot_titles=("Tertiary", "Quaternary", "Primary", "Secondary"))

	fig_20.add_trace(go.Bar(x=quat_bar_20['Year'], y=quat_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=2)

	fig_20.add_trace(go.Bar(x=tertiary_bar_20['Year'], y=tertiary_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=1, col=1)

	fig_20.add_trace(go.Bar(x=secondary_bar_20['Year'], y=secondary_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=2)

	fig_20.add_trace(go.Bar(x=primary_bar_20['Year'], y=primary_bar_20['% Share of GDP by Sector'], text='% Share of GDP by Sector'),
	              row=2, col=1)

	# Update yaxis properties
	fig_20.update_yaxes(range=[0, 80], row=1, col=1)
	fig_20.update_yaxes(range=[0, 60], row=1, col=2)
	fig_20.update_yaxes(range=[0, 10], row=2, col=1)
	fig_20.update_yaxes(range=[0, 60], row=2, col=2)

	# Update title and height
	fig_20.update_layout(title_text="Figure 20: Share of Total Real GDP by Sector for Allegheny County, 2001 to 2018.  Source: BEA.", 
	                  height=700,
	                  showlegend=False)

	fig_20.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	fig_20.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)
	
	plot_div20 = plot(fig_20, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	santa_clara_emp_by_gdp_21 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_21.csv')

	fig_21 = go.Figure()
	fig_21.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_21['Year'], y=santa_clara_emp_by_gdp_21['Total Employment'] *500, name='Total Employment')) # fill down to xaxis
	fig_21.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_21['Year'], y=santa_clara_emp_by_gdp_21['% Share of GDP by Sector'], fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_21.update_yaxes(range=[50000000, 300000000])
	fig_21.update_layout(title_text="Figure 21: Santa Clara County’s Information Technology(or Quaternary) Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018")

	fig_21.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	santa_clara_emp_by_gdp_22 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_22.csv')


	fig_22 = go.Figure()
	fig_22.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_22['Year'], y=santa_clara_emp_by_gdp_22['Total Employment'] *350, name='Total Employment')) # fill down to xaxis
	fig_22.add_trace(go.Scatter(x=santa_clara_emp_by_gdp_22['Year'], y=santa_clara_emp_by_gdp_22['% Share of GDP by Sector'], fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_22.update_layout(title_text="Figure 22: Santa Clara County’s Manufacturing(or Secondary) Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018")

	fig_22.update_yaxes(range=[50000000, 300000000])

	fig_22.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	cuya_emp_by_gdp_23 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_23.csv')


	fig_23 = go.Figure()
	fig_23.add_trace(go.Scatter(x=cuya_emp_by_gdp_23['Year'], y=cuya_emp_by_gdp_23['Total Employment'] *1100, name='Total Employment')) # fill down to xaxis
	fig_23.add_trace(go.Scatter(x=cuya_emp_by_gdp_23['Year'], y=cuya_emp_by_gdp_23['% Share of GDP by Sector'] *1.8, fill='tonexty', name='Total GDP')) # fill to trace0 y

	fig_23.update_layout(title_text='Figure 23: Cuyahoga County’s Information Technology Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018')

	fig_23.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	cuya_emp_by_gdp_24 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_24.csv')


	fig_24 = go.Figure()
	fig_24.add_trace(go.Scatter(x=cuya_emp_by_gdp_24['Year'], y=cuya_emp_by_gdp_24['Total Employment']*385, name='Total Employment')) # fill down to xaxis
	fig_24.add_trace(go.Scatter(x=cuya_emp_by_gdp_24['Year'], y=cuya_emp_by_gdp_24['% Share of GDP by Sector'], fill='tonexty', name='Total Employment')) # fill to trace0 y

	fig_24.update_layout(title_text='Figure 24: Cuyahoga County’s Manufacturing Sector, Employment v. Total GDP (2001 = 100, in 2012$). Source: BEA, 2001 to 2018')

	fig_24.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
                         line=dict(color='#9b0000', width=4, dash='dot')))
	fig_26.add_trace(go.Scatter(x=oh_secondary_26['Year'], y=oh_secondary_26['% of total'], name = 'Ohio',
                         line=dict(color='#d50000', width=4, dash='dash')))
	fig_26.add_trace(go.Scatter(x=usa_secondary_26['Year'], y=usa_secondary_26['% of total'], name='United States',
                         line=dict(color='#ff5131', width=4)))

	fig_26.update_layout(title_text='Figure 26: Percent of All Private Sector Employment that is in the Manufacturing, or Secondary, Sector. Source: BEA, 1969-2018')

	fig_26.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	usa_secondary_28 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_28_secondary.csv')
	usa_tert_28 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_28_tert.csv')

	fig_28 = go.Figure()

	fig_28.add_trace(go.Scatter(x=usa_secondary_28['Year'], y=usa_secondary_28['Secondary Employment Total'], name='Secondary Employment',
                         line=dict(color='firebrick', width=4, dash='dot')))
	fig_28.add_trace(go.Scatter(x=usa_tert_28['Year'], y=usa_tert_28['Tertiary Employment Total'], name = 'Tertiary Employment',
                         line=dict(color='royalblue', width=4, dash='dash')))

	fig_28.update_layout(title_text='Figure 28: Total Private Sector Employment in U.S. in the Manufacturing and Tertiary Sector. Source: BEA, 1969-2018')


	fig_28.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
                         line=dict(color='firebrick', width=4, dash='dot')))
	fig_29.add_trace(go.Scatter(x=ohio_tert_29['Year'], y=ohio_tert_29['Tertiary Employment Total'], name = 'Tertiary Employment',
                         line=dict(color='royalblue', width=4, dash='dash')))

	fig_29.update_layout(title_text='Figure 29: Total Private Sector Employment in Ohio in the Manufacturing and Tertiary Sector. Source: BEA, 1969-2018')


	fig_29.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
                         line=dict(color='firebrick', width=4, dash='dot')))
	fig_30.add_trace(go.Scatter(x=cuya_tert_30['Year'], y=cuya_tert_30['Tertiary Employment Total'], name = 'Tertiary Employment',
                         line=dict(color='royalblue', width=4, dash='dash')))

	fig_30.update_layout(title_text='Figure 30: Total Private Sector Employment in Cuyahoga County in the Manufacturing and Tertiary Sector. Source: BEA, 1969-2018')


	fig_30.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_31.add_trace(go.Scatter(x=cuya_knowledge_based_31['Year'], y=cuya_knowledge_based_31['Knowledge Based Employment Total'], fill='tozeroy', name='Knowledge Based')) 
	fig_31.add_trace(go.Scatter(x=cuya_lower_skill_31['Year'], y=cuya_lower_skill_31['Lower Skill Employment Total'], fill='tonexty', name='Lower Skill')) 
	fig_31.add_trace(go.Scatter(x=cuya_secondary_31['Year'], y=cuya_secondary_31['Secondary Employment Total'], fill='tozeroy',name='Secondary'))
	fig_31.add_trace(go.Scatter(x=cuya_quat_31['Year'], y=cuya_quat_31['Quaternary Employment Total'], fill='tozeroy',name='Quaternary'))# fill down to xaxis
	fig_31.add_trace(go.Scatter(x=cuya_blue_collar_31['Year'], y=cuya_blue_collar_31['Blue Collar Employment Total'], fill='tozeroy', name='Blue Collar')) 

	fig_31.update_layout(title_text='Figure 31: Cuyahoga County Private Sector Employment by Sector. Source BEA, 2001 to 2018.')


	fig_31.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	cuya_2001_lower_skill_32 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_32_lower.csv')
	cuya_2001_knowledge_based_32 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_32_knowledge.csv')


	fig_32 = go.Figure()
	fig_32.add_trace(go.Scatter(x=cuya_2001_lower_skill_32['Year'], y=cuya_2001_lower_skill_32['% of total'], name='Lower Skill')) 
	fig_32.add_trace(go.Scatter(x=cuya_2001_knowledge_based_32['Year'], y=cuya_2001_knowledge_based_32['% of total'], fill='tonexty',name='Knowledge Based'))

	fig_32.update_layout(title_text='Figure 32: Cuyahoga County Private Sector Employment by Sector. Source BEA, 2001 to 2018.')


	fig_32.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div32 = plot(fig_32, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	usa_2001_lower_skill_33 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_33_lower.csv')
	usa_2001_knowledge_based_33 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_33_knowledge.csv')


	fig_33 = go.Figure()
	fig_33.add_trace(go.Scatter(x=usa_2001_lower_skill_33['Year'], y=usa_2001_lower_skill_33['% of total'], name='Lower Skill')) 
	fig_33.add_trace(go.Scatter(x=usa_2001_knowledge_based_33['Year'], y=usa_2001_knowledge_based_33['% of total'], fill='tonexty',name='Knowledge Based'))

	fig_33.update_layout(title_text='Figure 33: Proportion of Private Sector Jobs that are in Knowledge-based versus Lower-wage Services in the U.S. Source: BEA, 2001 to 2018')


	fig_33.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	fig_34.add_trace(go.Scatter(x=ohio_2001_lower_skill_34['Year'], y=ohio_2001_lower_skill_34['% of total'], name='Lower Skill')) 
	fig_34.add_trace(go.Scatter(x=ohio_2001_knowledge_based_34['Year'], y=ohio_2001_knowledge_based_34['% of total'], fill='tonexty',name='Knowledge Based'))


	fig_34.update_layout(title_text='Figure 34: Proportion of Private Sector Jobs that are in Knowledge-based versus Lower-wage Services in Ohio Source: BEA, 2001 to 2018')


	fig_34.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_35.update_layout(title_text='Figure 35: Real Per Capita Income v. % of Knowledge-based Service Jobs by State.  Source: BEA, 2018.')


	fig_35.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div35 = plot(fig_35, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	state_emp_percent_36 = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_36.csv')

	fig_36 = px.bar(state_emp_percent_36, x='GeoName', y='% Jobs in Knowledge-based Services',
             hover_data=["GeoName", "% Jobs in Knowledge-based Services"],
             height=700,
             color='% Jobs in Knowledge-based Services',
             # color_discrete_sequence=px.colors.qualitative.Antique,
             title='Figure 36: Proportion of Private Sector Jobs that are in Knowledge-based Services in Big-City Counties. Source: BEA, 2018')

	fig_36.update_yaxes(title_text="")
	fig_36.update_xaxes(title_text="", tickangle=45)
	fig_36.update_layout(showlegend=False)

	fig_36.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)

	fig_36.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
             title='Figure 37: Proportion of Private Sector Jobs that are in Information Technology in Big-City Counties. Source: BEA, 2018')

	fig_37.update_yaxes(title_text="")
	fig_37.update_xaxes(title_text="", tickangle=45)
	fig_37.update_layout(showlegend=False)

	fig_37.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)

	fig_37.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	fig_39.update_traces(marker_color='#ff5131')

	fig_39.update_layout(title_text='Figure 39: Unemployment Rate for Leisure and Hospitality Workers, 2001 to April 2020. Source: BLS.')

	fig_39.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_42_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_42.csv')


	fig_42 = go.Figure(data=go.Scatter(x=fig_42_df['observation_date'], y=fig_42_df['ICSA']))
	fig_42.update_traces(marker_color='#ff5131')
	fig_42.update_yaxes(range=[0, 3000000])
	fig_42.update_layout(title_text='Figure 42: Initial Unemployment Claims (Monthly) Jan 1967 to April 2020. Source U.S. Employment and Training Organization')

	fig_42.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_43.update_layout(title_text='Figure 43: Initial Unemployment Claims (Monthly) Jan 1967 to April 2020. Source U.S. Employment and Training Organization')

	fig_43.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	fig_44.update_traces(marker_color='#ff5131')
	fig_44.update_xaxes(title='Male')
	fig_44.update_layout(title_text='Figure 44: Male Labor Force Participation Rate Jan. 1948 to May 2020. Source: Bureau of Labor Statistics')

	fig_44.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_50.update_layout(title_text='Figure 50: Life expectancy versus health spending per capita. Source: OECD, 2017')

	fig_50.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
	        size=12,
	        color="#212121"
	    ),
	    autosize=True,
	    
	    uniformtext_minsize=8,
	    uniformtext_mode='hide',
	    paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		)

	plot_div50 = plot(fig_50, output_type='div', include_plotlyjs=False, show_link=False, link_text="")

	fig_51_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_51.csv')


	# Create figure with secondary y-axis
	fig_51 = make_subplots(specs=[[{"secondary_y": True}]])

	# Add traces
	fig_51.add_trace(
	    go.Scatter(x=fig_51_df['Current $millions'], y=fig_51_df['Federal'], name="% Federal"),
	    secondary_y=True,
	    
	)

	fig_51.add_trace(
	    go.Scatter(x=fig_51_df['Current $millions'], y=fig_51_df['Private'], name="% Private"),
	    secondary_y=True,
	    
	)

	fig_51.add_trace(
	    go.Scatter(x=fig_51_df['Current $millions'], y=fig_51_df['Total Funding'], name="Total Funding", fill='tonexty'),
	    secondary_y=False,
	)
	# Add figure title
	fig_51.update_layout(
	    title_text="Figure 51: R&D Funding Source, 1953-2016. Source: NSF"
	)

	# Set y-axes titles
	fig_51.update_yaxes(title_text="R&D Funding (billions in 2009$)", secondary_y=False)

	fig_51.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	fig_52.update_traces(marker_color='#ff5131')

	fig_52.update_layout(
	    title_text="Figure 52: Top 1% National Income Share, USA, 1914-2018. Source: World Inequality Database."
	)

	fig_52.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	fig_53.update_traces(marker_color='#ff5131')

	fig_53.update_layout(
	    title_text="Figure 53: Wages and Salary Income as Precent of Gross Domestic Product, 1947-2019. Source: Federal Reserve Bank of St. Louis."
	)

	fig_53.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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

	fig_57_df = pd.read_csv('/home/rocinante/Desktop/rustbelt_analytica_webapp/rustbelt_analytica/fog/data/fig_57.csv')

	fig_57 = go.Figure(data=go.Scatter(x=fig_57_df['observation_date'], y=fig_57_df['IPG3254S'], fill='tonexty'))
	fig_57.update_traces(marker_color='#ff5131')

	fig_57.update_yaxes(range=[85, 125])

	fig_57.update_layout(
	    title_text="Figure 57: Industrial Production: Pharmaceutical and medicine, 2000 to 2019 (Index 2000 = 100). SOurce: BOard of Governors of the Federal Reserve System (US)"
	)

	fig_57.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	    title_text="Figure 58: Top Firms by R&D Expenditures (in millions).  Source: European Commission, EU R&D Scoreboard, 2019."
	)

	fig_58.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)

	fig_58.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
                         line=dict(color='firebrick', width=4, dash='dot')))
	fig_59.add_trace(go.Scatter(x=fig_59_health['Year'], y=fig_59_health['Annual'], name = 'Healthcare and Social Assistance',
                         line=dict(color='royalblue', width=4, dash='dash')))
	fig_59.add_trace(go.Scatter(x=fig_59_total['Year'], y=fig_59_total['Annual'], name='Total',
                         line=dict(color='#81C784', width=4))) # dash options include 'dash', 'dot', and 'dashdot'
	fig_59.update_layout(
    	title_text="Figure 59: Employment Growth in the Cleveland MSA, 1990 to 2019 (Index 1990 = 100). Source: Bureau of Labor Statistics."
	)


	fig_59.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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
	fig_60.update_traces(marker_color='#ff5131', marker_line_color='#9b0000',
                  marker_line_width=1.5, opacity=0.6)
	fig_60.update_layout(title_text='Figure 60: Location Quotient of Healthcare Practioners and Technical Operations for Largest 40 Metros. Source:  Occupational Employment and Statistics, May 2019.')
	fig_60.update_xaxes(title_text="", tickangle=45)

	fig_60.update_layout(

	    font=dict(
	        family="Helvetica, monospace",
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


	context={'plot_div': plot_div,
			 'plot_div2': plot_div2,
			 'plot_div8': plot_div8,
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
			 'plot_div42': plot_div42,
			 'plot_div43': plot_div43,
			 'plot_div44': plot_div44,
			 'plot_div50': plot_div50,
			 'plot_div51': plot_div51,
			 'plot_div52': plot_div52,
			 'plot_div53': plot_div53,
			 'plot_div53': plot_div53,
			 'plot_div57': plot_div57,
			 'plot_div58': plot_div58,
			 'plot_div59': plot_div59,
			 'plot_div60': plot_div60,


			}


	return HttpResponse(template.render(context, request))

