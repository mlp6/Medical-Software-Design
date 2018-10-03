def test_set_trace_integration():
    """manually set trace"""
    import pudb
    pudb.set_trace()
    assert 1 == 2

def test_pudb_b_integration():
    """automatically invoke debbuger on assertion fail"""
    import pudb.b
    # traceback is set up here
    assert 1 == 2
