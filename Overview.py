import streamlit as st
page_name = 'Overview'
import plotly.graph_objects as go
import pandas as pd

from src.utils import *


if __name__ == "__main__":

  # Create the average accuracy per run dataset.
  num_runs = 10
  df_accuracy = generate_dummy_data_for_average_accuracy_per_run(num_runs)

  # Create the latency per prediction dataset.
  num_predictions = 100
  df_latency = generate_dummy_data_for_latency_per_prediction(num_predictions)

  # Create the data drift across 5 different categories dataset.
  num_data_points = 100
  df_data_drift = generate_dummy_data_for_data_drift_across_5_different_categories(num_data_points)

  # Create the line graph of average accuracy per run.
  fig_accuracy = create_line_graph_of_average_accuracy_per_run(df_accuracy)

  # Create the scatter plot of latency per prediction.
  fig_latency = create_scatter_plot_of_latency_per_prediction(df_latency)

  # Create the bar chart of data drift across 5 different categories.
  fig_data_drift = create_bar_chart_of_data_drift_across_5_different_categories(df_data_drift)

  st.plotly_chart(fig_accuracy)
  st.plotly_chart(fig_latency)
  st.plotly_chart(fig_data_drift)
