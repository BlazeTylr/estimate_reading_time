from lib.estimate_reading_time import *

def test_estimate_reading_time_correct_number():
    string = 'qqtd anzh kbtx vxit jfzz aheq zexd hghm fzke jgzz pjfw venw bwjg qqjg eknb qeyb ajqg fbmz iwre truf ezda ujxj kave ruca hgxb rvmf dtur xcyg dzei tkvt hiuh urwk vewn purz guba weat tbez jccq bcih vqnv'
    actual = estimate_reading_time(20, string)
    expected = '0 h 2 min'
    assert actual == expected

def test_estimate_reading_time_less_than_a_minute():
    string = 'qqtd anzh kbtx vxit jfzz aheq zexd hghm fzke'
    actual = estimate_reading_time(20, string)
    expected = 'You can read that text less than a minute.'
    assert actual == expected