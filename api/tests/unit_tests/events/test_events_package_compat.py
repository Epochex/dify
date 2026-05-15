from events import Events


def test_events_package_exposes_opensearchpy_compatible_events_class():
    calls: list[str] = []
    events = Events()

    events.request_start += lambda: calls.append("start")
    events.request_end += lambda: calls.append("end")

    events.request_start()
    events.request_end()

    assert calls == ["start", "end"]
