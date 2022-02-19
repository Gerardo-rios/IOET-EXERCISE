import pytest
from datetime import datetime
from main import compare_schedules, is_encounter,get_employes,write_txt

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (["MO10:15-12:00","TU10:00-12:00","TH13:00-13:15","SA14:00-18:00","SU20:00-21:00"], ["MO10:00-12:00","TH12:00-14:00","SU20:00-21:00"], 3),
        (["MO10:00-12:00","TH12:00-14:00","SU20:00-21:00"], ["MO10:15-12:00","TU10:00-12:00","TH13:00-13:15","SA14:00-18:00","SU20:00-21:00"] , 3),
        (["MO10:00-12:00","TH12:00-14:00","SU20:00-21:00","TU10:00-12:00"], ["TU10:00-12:00","MO10:00-12:00","TH12:00-14:00","SU20:00-21:00"], 4),
    ]
)
def test_compare_schedules(input_a, input_b, expected):
    assert compare_schedules(input_a, input_b) == expected


@pytest.mark.parametrize(
    "input_a, input_b, input_c, input_d, expected",
    [
        (datetime.strptime("10:00","%H:%M"), datetime.strptime("12:00","%H:%M"), datetime.strptime("10:15","%H:%M"), datetime.strptime("11:00","%H:%M"), True),
        (datetime.strptime("11:00","%H:%M"), datetime.strptime("12:00","%H:%M"), datetime.strptime("10:15","%H:%M"), datetime.strptime("10:50","%H:%M"), False),
        (datetime.strptime("15:00","%H:%M"), datetime.strptime("18:00","%H:%M"), datetime.strptime("18:00","%H:%M"), datetime.strptime("20:00","%H:%M"), True),
        (datetime.strptime("15:00","%H:%M"), datetime.strptime("18:00","%H:%M"), datetime.strptime("18:10","%H:%M"), datetime.strptime("20:00","%H:%M"), False),
    ]
)
def test_is_encounter(input_a, input_b, input_c, input_d, expected):
    assert is_encounter(input_a, input_b, input_c, input_d) == expected


def test_get_employes(mocker):
    mockData = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\nANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
    mocker.patch('main.read_txt', return_value=mockData)
    assert get_employes() == [['RENE', 'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'], ['ASTRID', 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'], ['ANDRES', 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']]
    
    
def test_write(tmpdir):
    employe1 = "SARA"
    employe2 = "JUAN"
    encounters = "4"
    fpath = f"{tmpdir}/test.txt"
    write_txt(employe1, employe2, encounters, fpath)
    data_in = employe1 + "-" + employe2 + ":" + encounters + "\n"

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == data_out


