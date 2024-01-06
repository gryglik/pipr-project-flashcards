from flashcards_io import Import


def test_load_flashcards_set_from_csv_typical():
    import_obj = Import()
    flashcards_set = import_obj.load_flashcards_set_from_csv('tests/test.csv')
    assert flashcards_set.name == 'test'
    assert flashcards_set.flashcards[0].phrase == 'cat'
    assert flashcards_set.flashcards[0].definition == 'kot'
    assert not flashcards_set.flashcards[0].priority
    assert flashcards_set.flashcards[1].phrase == 'dog'
    assert flashcards_set.flashcards[1].definition == 'pies'
    assert flashcards_set.flashcards[1].priority
