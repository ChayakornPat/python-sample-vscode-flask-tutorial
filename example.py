def update_view(override_values={}):
    # [START bigquery_update_view_query]
    from google.cloud import bigquery

    credentials = service_account.Credentials.from_service_account_file('cpfit-innovation.json')
    project_id = 'cpfit-innovation'
    client = bigquery.Client(credentials=credentials,project=project_id)

    view_id = "cpfit-innovation.TEST_Onedrive.Yacht"
    # [END bigquery_update_view_query]
    # To facilitate testing, we replace values with alternatives
    # provided by the testing harness.
    view_id = override_values.get("view_id", view_id)
    # [START bigquery_update_view_query]
    view = bigquery.Table(view_id)

    # The source table in this example is created from a CSV file in Google
    # Cloud Storage located at
    # `gs://cloud-samples-data/bigquery/us-states/us-states.csv`. It contains
    # 50 US states, while the view returns only those states with names
    # starting with the letter 'M'.
    view.view_query = f"SELECT "Data Platform" "

    # Make an API request to update the query property of the view.
    view = client.update_table(view, ["view_query"])
    print(f"Updated {view.table_type}: {str(view.reference)}")
    # [END bigquery_update_view_query]
    return view
update_view(override_values={})
