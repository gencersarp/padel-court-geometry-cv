from src.geometry import order_quad_corners


def test_order_quad_corners_returns_clockwise_layout():
    points = [(300, 200), (100, 100), (80, 320), (330, 340)]
    ordered = order_quad_corners(points)

    assert ordered.shape == (4, 2)
    assert tuple(ordered[0]) == (100.0, 100.0)
    assert tuple(ordered[1]) == (300.0, 200.0)
    assert tuple(ordered[2]) == (330.0, 340.0)
    assert tuple(ordered[3]) == (80.0, 320.0)
