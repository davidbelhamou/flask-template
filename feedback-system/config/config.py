def get_config(env: str):
    conf = {
        "dev":{
            "mongo_uri": ["mongodb://user:pass@url1:port1, url2:port2, url3:port3"],
            "database": "db_name",
            "collection": "collection_name",
            "port": 11111,
            "algo_unique_field": {"algo1": ["id", "date"],
                                  "algo2": ["name", "score"]}
        },
        "prod": {

        }
    }