from data.calc import calculate_sum,calculate_sub

def test_cal_sum():
    a = calculate_sum(2,3)
    assert a==5
    
def test_cal_sub():
    b = calculate_sub(5,2)
    assert b==3