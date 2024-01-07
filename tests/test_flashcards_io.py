from flashcards_io import Import, Export


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


def test_write_flashcards_write_to_csv():
    import_obj = Import()
    flashcards_set = import_obj.load_flashcards_set_from_csv('tests/test.csv')
    flashcards_set.name = 'test_export'
    export_obj = Export()
    export_obj.write_flashcards_set_to_csv(flashcards_set, 'tests')
    