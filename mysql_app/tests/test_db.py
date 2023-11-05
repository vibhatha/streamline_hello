import os

import pytest

from gymcana.data import DataEngine


@pytest.fixture(scope="session")
def engine(request):
    print("\nInitializing resources")
    username = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    host = "localhost"
    engine_ = DataEngine(username=username, password=password, host=host)

    def db_connector_teardown():
        print("\nFinalizing resources")
        engine_.close()

    request.addfinalizer(db_connector_teardown)
    print("Returning resource")
    return engine_


def test_connection(engine):
    assert engine.connection.is_connected()


def test_create_sample_db(engine):
    db_name = "SAMPLE_DB"
    create_query = f"""
    CREATE DATABASE IF NOT EXISTS {db_name};
"""
    delete_query = f"""
    DROP DATABASE IF EXISTS {db_name};
"""
    engine.cursor.execute(create_query)
    engine.cursor.execute(delete_query)


def test_table_lifecyle(engine):
    db_name = "SAMPLE_DB"
    create_db_query = f"""
    CREATE DATABASE IF NOT EXISTS {db_name};
"""
    select_db_query = f"USE {db_name}"
    delete_db_query = f"""
    DROP DATABASE IF EXISTS {db_name};
"""
    engine.cursor.execute(create_db_query)
    engine.cursor.execute(select_db_query)
    create_query = """
    CREATE TABLE IF NOT EXISTS test_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    );
    """

    insert_query = """INSERT INTO test_table (name, age)
    VALUES ('John Doe', 28);
    """

    select_query = "SELECT * FROM test_table;"

    delete_query = "DROP TABLE IF EXISTS test_table;"

    engine.cursor.execute(create_query)
    engine.cursor.execute(insert_query)
    engine.connection.commit()
    engine.cursor.execute(select_query)
    rows = engine.cursor.fetchall()
    assert len(rows) == 1
    assert rows[0][0] == 1
    assert rows[0][1] == "John Doe"
    assert rows[0][2] == 28
    engine.cursor.execute(delete_query)
    engine.connection.commit()
    engine.cursor.execute(delete_db_query)
    engine.connection.commit()
