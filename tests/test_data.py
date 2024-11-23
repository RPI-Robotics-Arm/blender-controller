import json
import pytest
from modules.data import Joint, Data, JOINTS


@pytest.fixture
def joint():
    """Fixture for creating a Joint instance."""
    return Joint(1, 2, 3)


@pytest.fixture
def data():
    """Fixture for creating a Data instance."""
    return Data()


def test_joint_creation(joint):
    """Test creating a Joint instance."""
    assert joint.get("x") == 1
    assert joint.get("y") == 2
    assert joint.get("z") == 3


def test_joint_setter_and_getter(joint):
    """Test setting and getting values in a Joint instance."""
    joint.set("x", 10)
    joint.set("y", 20)
    joint.set("z", 30)
    assert joint.get("x") == 10
    assert joint.get("y") == 20
    assert joint.get("z") == 30


def test_joint_invalid_key(joint):
    """Test getting a non-existent key."""
    assert joint.get("invalid") is None


def test_joint_str_method(joint):
    """Test the __str__ method for Joint (JSON output)."""
    assert str(joint) == '{"x": 1, "y": 2, "z": 3}'


def test_data_initialization(data):
    """Test creating Data instance and default joint initialization."""
    for joint_id in range(1, JOINTS + 1):
        joint = data.get_joint(joint_id)
        assert joint is not None
        assert joint.get("x") == 0
        assert joint.get("y") == 0
        assert joint.get("z") == 0


def test_data_set_joint(data):
    """Test setting joint values in Data instance."""
    data.set_joint(1, 10, 20, 30)
    joint = data.get_joint(1)
    assert joint.get("x") == 10
    assert joint.get("y") == 20
    assert joint.get("z") == 30


def test_data_set_joint_invalid_id(data):
    """Test setting joint with invalid joint id."""
    data.set_joint(100, 10, 20, 30)  # Invalid joint ID
    joint = data.get_joint(100)  # Should be None
    assert joint is None


def test_data_get_joint(data):
    """Test retrieving a joint by id from Data."""
    joint = data.get_joint(1)
    assert joint is not None
    assert joint.get("x") == 0
    assert joint.get("y") == 0
    assert joint.get("z") == 0


def test_data_str_method(data):
    """Test the __str__ method for Data (JSON output)."""
    expected_json = json.dumps(
        {i: {"x": 0, "y": 0, "z": 0} for i in range(1, JOINTS + 1)}
    )
    assert str(data) == expected_json
