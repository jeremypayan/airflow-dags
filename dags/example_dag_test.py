import internal_unit_testing



def test_dag_import():
    from dags import example_dag, dag_slackbots_city_stats,dag_slackbots_stats_color,dag_slackbots_autonomy,dag_slackbots_prod_autonomy
    internal_unit_testing.assert_has_valid_dag(example_dag)
