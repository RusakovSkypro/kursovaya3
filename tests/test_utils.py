from src.utils import load_operation, mask_card, filter_sort
def test_load_operation():
    text_test = [
        {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
        }
    ]

    assert load_operation('data_test.json') == text_test


def test_mask_card():
    assert mask_card("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert mask_card("Счет 64686473678894779589") == 'Счет **9589'



def test_filter_sort():
    list = [{"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
  {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  {"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
  {"date": "2018-03-23T10:45:06.972075"},
  {"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878"}]

    assert filter_sort(list) == [{"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
  {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  {"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878"},
  {"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

def test_form_date():
    list_test = "2019-08-26T10:50:58.294041"

    assert form_date(list_test) == '26.08.2019'

