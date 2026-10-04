from pipeline import clean_data
def test_clean():
        assert clean_data("1001") == 0
        assert clean_data("111") == 1