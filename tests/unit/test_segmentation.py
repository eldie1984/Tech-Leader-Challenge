import pytest
from FireSegmentation.segmentation import segmentacionDeIncendios

def test_segmentacionDeIncendios():
    # Mock list of fires
    fuegos = [
        {"id": "fire1", "x": 1.0, "y": 1.0, "time": "2022-01-01T00:00:00"},
        {"id": "fire2", "x": 2.0, "y": 2.0, "time": "2022-01-01T01:00:00"},
        {"id": "fire3", "x": 3.0, "y": 3.0, "time": "2022-01-01T02:00:00"},
    ]

    # Call the segmentacionDeIncendios function
    num, lista = segmentacionDeIncendios(fuegos, 1.5, 60)

    # Check that the function returns the correct number of segments
    assert num == 2

    # Check that the function returns the correct list of segments
    assert lista == [["fire1"], ["fire2", "fire3"]]