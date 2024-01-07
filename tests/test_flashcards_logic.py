import pytest
from time import sleep

from flashcards_logic import Flashcard, FlashcardsSet, TestItem, Session, Test, TestResult
from lib.errors import (
    EmptyStringError, FlashcardNotInSetError, IndexOutOfRangeError,
    StringTooLongError, SetNotInSessionError, NotOpenedSetError,
    NotOpenedFlashcardError, ClosedTestItemError, TestNotStartedError,
    TestNotFinishedError
    )


def test_Flashcard_create_typical():
    flashcard = Flashcard('cat', 'kot', True)
    assert flashcard.phrase == 'cat'
    assert flashcard.definition == 'kot'
    assert flashcard.priority


def test_Flashcard_create_no_priority():
    flascard = Flashcard('cat', 'kot')
    assert flascard.phrase == 'cat'
    assert flascard.definition == 'kot'
    assert not flascard.priority


def test_Flashcard_create_empty_phrase_or_definition():
    with pytest.raises(EmptyStringError):
        Flashcard('cat', '')
        Flashcard('', 'kot')
        Flashcard('', '')


def test_Flashcard_phrase_set():
    flashcard = Flashcard('cat', 'pies')
    assert flashcard.phrase == 'cat'
    flashcard.phrase = 'dog'
    assert flashcard.phrase == 'dog'


def test_Flashcard_phrase_definition_set_too_long():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    with pytest.raises(StringTooLongError):
        Flashcard(string, 'kot')
    with pytest.raises(StringTooLongError):
        Flashcard('cat', string)
    flashcard = Flashcard('cat', 'kot')
    with pytest.raises(StringTooLongError):
        flashcard.phrase = string
    with pytest.raises(StringTooLongError):
        flashcard.definition = string


def test_Flashcard_phrase_set_empty():
    flashcard = Flashcard('cat', 'kot')
    assert flashcard.phrase == 'cat'
    with pytest.raises(EmptyStringError):
        flashcard.phrase = ''


def test_Flashcard_definition_set():
    flashcard = Flashcard('cat', 'pies')
    assert flashcard.definition == 'pies'
    flashcard.definition = 'kot'
    assert flashcard.definition == 'kot'


def test_Flashcard_definition_set_empty():
    flashcard = Flashcard('cat', 'kot')
    assert flashcard.definition == 'kot'
    with pytest.raises(EmptyStringError):
        flashcard.phrase = ''


def test_FlashcardsSet_create_typical():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    flashcards_set = FlashcardsSet('set1', flashcards)
    assert flashcards_set.name == 'set1'
    assert flashcards_set.flashcards[0].phrase == 'cat'


def test_FlashcardsSet_create_empty_name():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    with pytest.raises(EmptyStringError):
        FlashcardsSet('', flashcards)


def test_FlashcardsSet_too_long_name():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    with pytest.raises(StringTooLongError):
        FlashcardsSet(string)
    with pytest.raises(StringTooLongError):
        flashcards_set = FlashcardsSet('set1')
        flashcards_set.name = string


def test_FlashcardsSet_create_no_flashcards():
    flashcards_set = FlashcardsSet('empty_set')
    assert flashcards_set.name == 'empty_set'
    assert not len(flashcards_set.flashcards)


def test_FlashcardsSet_add_Flashcard():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    flashcards_set = FlashcardsSet('set1', flashcards)
    assert flashcards_set.flashcards[1].phrase == 'dog'
    assert flashcards_set.flashcards[1].definition == 'pies'
    new_flashcard = Flashcard('cow', 'krowa')
    flashcards_set.add_flashcard(new_flashcard)
    assert flashcards_set.flashcards[2].phrase == 'cow'
    assert flashcards_set.flashcards[2].definition == 'krowa'


def test_FlashcardSet_remove_Flashcard():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard1, flashcard2])
    assert len(flashcards_set.flashcards) == 2
    flashcards_set.remove_flashcard(flashcard1)
    assert len(flashcards_set.flashcards) == 1
    assert flashcards_set.flashcards[0] == flashcard2


def test_FlashcardsSet_remove_not_existing_flashcard():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard1, flashcard2])
    assert len(flashcards_set.flashcards) == 2
    with pytest.raises(FlashcardNotInSetError):
        flashcards_set.remove_flashcard(Flashcard('cow', 'krowa'))


def test_FlashcardsSet_flashcard_index_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard1, flashcard2])
    assert flashcards_set.flashcard_index(flashcard2) == 1


def test_FlashcardsSet_flashcard_index_not_in_the_set():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet('set1', [flashcard1, flashcard2])
    with pytest.raises(FlashcardNotInSetError):
        flashcards_set.flashcard_index(flashcard3)


def test_FlashcardsSet_len_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    assert flashcards_set.len() == 3


def test_FlashcardsSet_is_empty_typical():
    flashcards_set = FlashcardsSet('set1')
    assert flashcards_set.is_empty()
    flashcards_set.add_flashcard(Flashcard('cat', 'kot'))
    assert not flashcards_set.is_empty()


def test_FlashcardsSet_draw_flashcards_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    drawn_flashcards_set = flashcards_set.draw_flashcards(2)
    assert drawn_flashcards_set.name == 'set1'
    assert drawn_flashcards_set.len() == 2
    flashcards = drawn_flashcards_set.flashcards
    assert flashcard1 in flashcards or flashcard2 in flashcards


def test_FlashcardsSet_draw_flashcards_empty_set():
    flashcards_set = FlashcardsSet('set1')
    with pytest.raises(IndexOutOfRangeError):
        flashcards_set.draw_flashcards(3)


def test_FlashcardsSet_draw_flashcards_invalid_count():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    flashcards_set.draw_flashcards(3)
    with pytest.raises(IndexOutOfRangeError):
        flashcards_set.draw_flashcards(4)
    with pytest.raises(IndexOutOfRangeError):
        flashcards_set.draw_flashcards(0)
    with pytest.raises(IndexOutOfRangeError):
        flashcards_set.draw_flashcards(-1)


def test_TestItem_get_question_typical():
    flashcard = Flashcard('cat', 'kot')
    test_item = TestItem(flashcard)
    assert not test_item.is_opened()
    test_item.open()
    assert test_item.get_question() == 'cat'


def test_TestItem_get_question_not_opened():
    flashcard = Flashcard('cat', 'kot')
    test_item = TestItem(flashcard)
    assert not test_item.is_opened()
    with pytest.raises(ClosedTestItemError):
        test_item.get_question()


def test_TestItem_set_correct_answer_and_result_typical():
    flashcard = Flashcard('cat', 'kot')
    test_item = TestItem(flashcard)
    test_item.open()
    assert test_item.get_question() == 'cat'
    test_item.set_answer('kot')
    assert test_item.result()
    assert not test_item.is_opened()


def test_TestItem_set_wrong_answer_and_result_typical():
    flashcard = Flashcard('cat', 'kot')
    test_item = TestItem(flashcard)
    test_item.open()
    assert test_item.get_question() == 'cat'
    test_item.set_answer('pies')
    assert not test_item.result()
    assert not test_item.is_opened()


def test_TestItem_set_answer_after_closed():
    flashcard = Flashcard('cat', 'kot')
    test_item = TestItem(flashcard)
    test_item.open()
    assert test_item.get_question() == 'cat'
    test_item.set_answer('pies')
    assert not test_item.result()
    with pytest.raises(ClosedTestItemError):
        test_item.set_answer('kot')


def test_TestItem_question_definition_typical():
    flashcard = Flashcard('cat', 'kot')
    test_item = TestItem(flashcard, mode=1)
    test_item.open()
    assert test_item.get_question() == 'kot'
    test_item.set_answer('cat')
    assert test_item.result()
    assert not test_item.is_opened()


def test_Test_start_test_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    test = Test(flashcards_set)
    assert test.name() == 'set1'
    assert not test.is_started()
    test.start()
    assert test.is_started()


def test_Test_empty_flashcards_set():
    flashcards_set = FlashcardsSet('set')
    with pytest.raises(FlashcardNotInSetError):
        Test(flashcards_set)


def test_Test_get_test():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    test = Test(flashcards_set)
    test.start()
    test_items = test.get_test()
    assert test_items[0].get_question() == 'cat'
    assert test_items[2].get_question() == 'cow'


def test_Test_solve_test_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    test = Test(flashcards_set)
    test.start()
    test_items = test.get_test()
    assert test_items[0].get_question() == 'cat'
    assert test_items[2].get_question() == 'cow'
    test_items[0].set_answer('kot')
    test_items[2].set_answer('krowa')
    assert test.result().get_correct_answers_count() == 2
    assert test.result().get_questions_count() == 3


def test_Test_solve_test_auto_close():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    test = Test(flashcards_set)
    test.start()
    assert test.is_started()
    test_items = test.get_test()
    assert test_items[0].get_question() == 'cat'
    assert test_items[2].get_question() == 'cow'
    test_items[0].set_answer('kot')
    test_items[2].set_answer('krowa')
    test.close()
    assert test.result().get_correct_answers_count() == 2
    assert test.result().get_questions_count() == 3


def test_Test_time_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1])
    test = Test(flashcards_set)
    test.start()
    sleep(2)
    test.close()
    assert test.time() == pytest.approx(2.0, 0.1)


def test_Test_time_during_test():
    flashcard1 = Flashcard('cat', 'kot')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1])
    test = Test(flashcards_set)
    test.start()
    sleep(2)
    assert test.time() == pytest.approx(2.0, 0.1)


def test_Test_time_test_not_started():
    flashcard1 = Flashcard('cat', 'kot')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1])
    test = Test(flashcards_set)
    sleep(2)
    with pytest.raises(TestNotStartedError):
        test.time()


def test_Test_change_test_after_closing():
    flashcard1 = Flashcard('cat', 'kot')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1])
    test = Test(flashcards_set)
    test.start()
    test_items = test.get_test()
    assert test_items[0].get_question() == 'cat'
    test_items[0].set_answer('kotek')
    assert test.result().get_correct_answers_count() == 0
    assert test.result().get_questions_count() == 1
    with pytest.raises(ClosedTestItemError):
        test_items[0].set_answer('kot')
    assert test.result().get_correct_answers_count() == 0
    assert test.result().get_questions_count() == 1


def test_Test_is_finished():
    flashcard1 = Flashcard('cat', 'kot')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1])
    test = Test(flashcards_set)
    assert not test.is_finished()
    test.start()
    assert not test.is_finished()
    test.close()
    assert test.is_finished()


def test_TestResult_typical():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcard3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1, flashcard2, flashcard3])
    test = Test(flashcards_set)
    test.start()
    test_items = test.get_test()
    test_items[0].set_answer('kot')
    test_items[2].set_answer('krowa')
    sleep(2)
    test_result: TestResult = test.result()
    assert test_result.get_correct_answers_count() == 2
    assert test_result.get_incorrect_answers_count() == 1
    assert test_result.get_questions_count() == 3
    assert test_result.get_accuracy() == pytest.approx(66.66, 0.01)
    assert test_result.get_duration() == pytest.approx(2.0, 0.1)
    assert test_result.get_time_per_question() == pytest.approx(0.66, 0.1)


def test_TestResult_test_not_finished():
    flashcard1 = Flashcard('cat', 'kot')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard1])
    test = Test(flashcards_set)
    with pytest.raises(TestNotFinishedError):
        test.result()


def test_Session_create_typical():
    session = Session('user1')
    assert session.username == 'user1'


def test_Session_create_empty_username():
    with pytest.raises(EmptyStringError):
        Session('')


def test_Session_create_too_long_username():
    with pytest.raises(StringTooLongError):
        Session('aaaaaaaaaaaaaaaaaaaaaaaaaa')  # 26 chars


def test_Session_set_username_typical():
    session = Session('user1')
    assert session.username == 'user1'
    session.username = 'user2'
    assert session.username == 'user2'


def test_Session_set_empty_username():
    session = Session('user1')
    assert session.username == 'user1'
    with pytest.raises(EmptyStringError):
        session.username = ''


def test_Session_set_too_long_username():
    session = Session('user1')
    assert session.username == 'user1'
    with pytest.raises(StringTooLongError):
        session.username = 'aaaaaaaaaaaaaaaaaaaaaaaaaa'


def test_Session_add_set():
    session = Session('user')
    assert not session.flashcards_sets
    flashcards_set = FlashcardsSet('set1')
    session.add_set(flashcards_set)
    assert flashcards_set in session.flashcards_sets


def test_Session_remove_set_typical():
    session = Session('user')
    flashcards_set = FlashcardsSet('set1')
    session.add_set(flashcards_set)
    assert flashcards_set in session.flashcards_sets
    session.remove_set(flashcards_set)
    assert flashcards_set not in session.flashcards_sets


def test_Session_remove_set_not_in_session():
    session = Session('user')
    flashcards_set = FlashcardsSet('set1')
    with pytest.raises(SetNotInSessionError):
        session.remove_set(flashcards_set)


def test_Session_open_set_typical():
    flashcards_set1 = FlashcardsSet('set1')
    flashcards_set2 = FlashcardsSet('set2')
    session = Session('user')
    session.add_set(flashcards_set1)
    session.add_set(flashcards_set2)
    assert not session.opened_set
    session.open_set(flashcards_set2)
    assert session.opened_set == flashcards_set2


def test_Session_open_set_not_in_session():
    flashcards_set1 = FlashcardsSet('set1')
    flashcards_set2 = FlashcardsSet('set2')
    session = Session('user')
    session.add_set(flashcards_set1)
    session.open_set(flashcards_set1)
    assert session.opened_set == flashcards_set1
    with pytest.raises(SetNotInSessionError):
        session.open_set(flashcards_set2)


def test_Session_close_set():
    flashcards_set1 = FlashcardsSet('set1')
    session = Session('user')
    session.add_set(flashcards_set1)
    session.open_set(flashcards_set1)
    assert session.opened_set == flashcards_set1
    session.close_set()
    assert not session.opened_set


def test_Session_open_flashcard_typical():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard_1, flashcard_2])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    assert not session.opened_flashcard
    session.open_flashcard(1)
    assert session.opened_flashcard == flashcard_2


def test_Session_open_flashcard_no_opened_set():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard_1, flashcard_2])
    session = Session('user')
    session.add_set(flashcards_set)
    with pytest.raises(NotOpenedSetError):
        session.open_flashcard(flashcard_2)


def test_Session_open_flashcard_index_out_of_range():
    flashcards_set = FlashcardsSet('set1')
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    with pytest.raises(IndexOutOfRangeError):
        session.open_flashcard(3)


def test_Session_close_flashcard():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard_1, flashcard_2])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    session.open_flashcard(1)
    assert session.opened_flashcard == flashcard_2
    session.close_flashcard()
    assert not session.opened_flashcard


def test_Session_flashcard_index_typical():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard_1, flashcard_2])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    session.open_flashcard(1)
    assert session.opened_flashcard == flashcard_2
    assert session.flashcard_index() == 1


def test_Session_flashcard_index_no_opened_flashcard():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard_1, flashcard_2])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    with pytest.raises(NotOpenedFlashcardError):
        session.flashcard_index()


def test_Session_next_flashcard_typical():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    session.open_flashcard(1)
    assert session.opened_flashcard == flashcard_2
    session.next_flashcard()
    assert session.opened_flashcard == flashcard_3
    session.next_flashcard()
    assert session.opened_flashcard == flashcard_1


def test_Session_next_flashcard_no_opened_flashcard():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    with pytest.raises(NotOpenedFlashcardError):
        session.next_flashcard()


def test_Session_previous_flashcard_typical():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    session.open_flashcard(1)
    assert session.opened_flashcard == flashcard_2
    session.previous_flashcard()
    assert session.opened_flashcard == flashcard_1
    session.previous_flashcard()
    assert session.opened_flashcard == flashcard_3


def test_Session_previous_flashcard_no_opened_flashcard():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    with pytest.raises(NotOpenedFlashcardError):
        session.previous_flashcard()


def test_Session_flashcard_counter_info_typical():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    session.open_flashcard(1)
    assert session.flashcard_counter_info() == '2 / 3'


def test_Session_countr_info_no_opened_set():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    assert session.flashcard_counter_info() == '0 / 0'


def test_Session_counter_info_no_opened_flashcard():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    assert session.flashcard_counter_info() == '0 / 3'


def test_Session_generate_test_typical():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    test = session.generate_test(2)
    test.start()
    assert test.result().get_correct_answers_count() == 0
    assert test.result().get_questions_count() == 2


def test_Session_generate_test_not_opened_set():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    with pytest.raises(NotOpenedSetError):
        session.generate_test(2)


def test_Session_generate_test_invalid_question_count():
    flashcard_1 = Flashcard('cat', 'kot')
    flashcard_2 = Flashcard('dog', 'pies')
    flashcard_3 = Flashcard('cow', 'krowa')
    flashcards_set = FlashcardsSet(
        'set1', [flashcard_1, flashcard_2, flashcard_3])
    session = Session('user')
    session.add_set(flashcards_set)
    session.open_set(flashcards_set)
    with pytest.raises(IndexOutOfRangeError):
        session.generate_test(4)
    with pytest.raises(IndexOutOfRangeError):
        session.generate_test(0)
    with pytest.raises(IndexOutOfRangeError):
        session.generate_test(-1)
