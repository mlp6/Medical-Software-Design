def test_rectify():
    from env_detect import rectify

    import numpy as np
    insig = np.array([50, 150, 2, 300])
    rect_out = rectify(insig)
    assert np.array_equal(rect_out, [50, 150, 2, 300])

    insig = np.array([-50, 150, -2, 300])
    rect_out = rectify(insig)
    assert np.array_equal(rect_out, [50, 150, 2, 300])

    insig = np.array([-50, -150, -2, -300])
    rect_out = rectify(insig)
    assert np.array_equal(rect_out, [50, 150, 2, 300])

def test_rectify_nan():
    from env_detect import removeNanAndInf

    import numpy as np
    insig = np.array([10, 150, NaN, 300])
    rect_out = rectify(insig)
    assert np.array_equal(rect_out, ([10, 150, 225, 300]))

    #Case to consider
    #insig = np.array([10, 150, NaN, NaN, 300])
    #rect_out = rectify(insig)
    #assert np.array_equal(rect_out, ([])


    insig = np.array([10, 150, 2, NaN])
    rect_out = rectify(insig)
    assert np.array_equal(rect_out, ([10, 150, -146]))

    insig = np.array([NaN, 150, 2, 300])
    rect_out = rectify(insig)
    assert.np.array_equal(rect_out, ([298, 150, 2, 300]))

    #Case to consider
    #insig = np.array([NaN, NaN, NaN, NaN])
    #rect_out = rectify(insig)
    # assert np.array_equal(rect_out, ([])

def test_rectify_inf():
    #placeholder unit test for rectify infs
