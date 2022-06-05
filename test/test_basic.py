import json

import duboce as dub

fixture = [
    {"name": "John", "height": 178.8, "instrument": "guitar"},
    {"name": "Paul", "height": 180, "instrument": "bass"},
    {"name": "George", "height": 175, "instrument": "guitar"},
    {"name": "Ringo", "height": 173, "instrument": "drums"},
]


def test_basic_json():
    assert dub.Dot(fixture, x="height", y="name", stroke="instrument").__dict__ == {
        "@@type": "Dot",
        "data": fixture,
        "options": {"x": "height", "y": "name", "stroke": "instrument"},
    }
