import os
print(os.getcwd())
print('Hello')

def create_view(override_values={}):
    # [START bigquery_create_view]
    from google.cloud import bigquery

    client = bigquery.Client()

    view_id = "cpfit-innovation.Test_Azure.Yacht"
    # [END bigquery_create_view]
    # To facilitate testing, we replace values with alternatives
    # provided by the testing harness.
    view_id = override_values.get("view_id", view_id)
    # [START bigquery_create_view]
    view = bigquery.Table(view_id)

    # The source table in this example is created from a CSV file in Google
    # Cloud Storage located at
    # `gs://cloud-samples-data/bigquery/us-states/us-states.csv`. It contains
    # 50 US states, while the view returns only those states with names
    # starting with the letter 'W'.
    view.view_query = f"SELECT 555"

    # Make an API request to create the view.
    view = client.create_table(view)
    print(f"Created {view.table_type}: {str(view.reference)}")
    # [END bigquery_create_view]
    return view

create_view(override_values={})


