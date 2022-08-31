from dodal.devices.det_dim_constants import EIGER2_X_16M_SIZE
from dodal.devices.detector import DetectorParams


def create_detector_params_with_directory(directory):
    return DetectorParams(
        100,
        1.0,
        1,
        directory,
        "test",
        0,
        1.0,
        0.0,
        0.0,
        1,
        False,
        detector_size_constants=EIGER2_X_16M_SIZE,
    )


def test_if_trailing_slash_not_provided_then_appended():
    params = create_detector_params_with_directory("test/dir")
    assert params.directory == "test/dir/"


def test_if_trailing_slash_provided_then_not_appended():
    params = create_detector_params_with_directory("test/dir/")
    assert params.directory == "test/dir/"
