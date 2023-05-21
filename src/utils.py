# Generating Dummy Data

import random
import pandas as pd

def generate_dummy_data_for_average_accuracy_per_run(num_runs):
  """Generates dummy data for average accuracy per run.

  Args:
    num_runs: The number of runs to generate data for.

  Returns:
    A Pandas DataFrame, where each row contains the accuracy for a single run, and a date column.
  """
  data = []
  for i in range(num_runs):
    accuracy = random.randint(0, 100)
    date = pd.to_datetime("2023-05-20", format="%Y-%m-%d") + pd.Timedelta(days=i)
    data.append([accuracy, date])

  return pd.DataFrame(data, columns=["accuracy", "date"])


def generate_dummy_data_for_latency_per_prediction(num_predictions):
  """Generates dummy data for latency per prediction.

  Args:
    num_predictions: The number of predictions to generate data for.

  Returns:
    A Pandas DataFrame, where each row contains the latency for a single prediction, and an id column.
  """
  data = []
  for i in range(num_predictions):
    latency = random.randint(1, 1000)
    id = i
    data.append([latency, id])

  return pd.DataFrame(data, columns=["latency", "id"])


def generate_dummy_data_for_data_drift_across_5_different_categories(num_data_points):
  """Generates dummy data for data drift across 5 different categories.

  Args:
    num_data_points: The number of data points to generate data for.

  Returns:
    A Pandas DataFrame, where each row contains the category and value for a single data point, and an id column.
  """
  data = []
  for i in range(num_data_points):
    category = random.randint(0, 4)
    value = random.randint(1, 100)
    id = i
    data.append([category, value, id])

  return pd.DataFrame(data, columns=["category", "value", "id"])

# ========================================================================== #

# Generating Graphs

import random
import pandas as pd
import plotly.graph_objects as go

def create_line_graph_of_average_accuracy_per_run(df):
  """Creates a line graph of average accuracy per run.

  Args:
    df: A Pandas DataFrame, where each row contains the accuracy for a single run, and a date column.

  Returns:
    A Plotly graph.
  """
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=df["date"], y=df["accuracy"], mode="lines"))
  fig.update_layout(title="Average Accuracy Per Run")

  return fig


def create_scatter_plot_of_latency_per_prediction(df):
  """Creates a scatter plot of latency per prediction.

  Args:
    df: A Pandas DataFrame, where each row contains the latency for a single prediction, and an id column.

  Returns:
    A Plotly graph.
  """
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=df["id"], y=df["latency"], mode="markers"))
  fig.update_layout(title="Latency Per Prediction")

  return fig


def create_bar_chart_of_data_drift_across_5_different_categories(df):
  """Creates a bar chart of data drift across 5 different categories.

  Args:
    df: A Pandas DataFrame, where each row contains the category and value for a single data point, and an id column.

  Returns:
    A Plotly graph.
  """
  fig = go.Figure()
  fig.add_trace(go.Bar(x=df["category"], y=df["value"], orientation="v"))
  fig.update_layout(title="Data Drift Across 5 Different Categories")

  return fig

