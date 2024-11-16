import unittest
import json

from modules.data import Joint, Data, JOINTS

# Assuming Joint and Data are already imported and available here


class TestJointAndData(unittest.TestCase):

    def test_joint_creation(self):
        # Test creating a Joint instance
        joint = Joint(1, 2, 3)
        self.assertEqual(joint.get("x"), 1)
        self.assertEqual(joint.get("y"), 2)
        self.assertEqual(joint.get("z"), 3)

    def test_joint_setter_and_getter(self):
        # Test setting and getting values in a Joint instance
        joint = Joint(1, 2, 3)
        joint.set("x", 10)
        joint.set("y", 20)
        joint.set("z", 30)
        self.assertEqual(joint.get("x"), 10)
        self.assertEqual(joint.get("y"), 20)
        self.assertEqual(joint.get("z"), 30)

    def test_joint_invalid_key(self):
        # Test getting a non-existent key
        joint = Joint(1, 2, 3)
        self.assertIsNone(joint.get("invalid"))

    def test_joint_str_method(self):
        # Test the __str__ method for Joint (JSON output)
        joint = Joint(1, 2, 3)
        self.assertEqual(joint.__str__(), '{"x": 1, "y": 2, "z": 3}')

    def test_data_initialization(self):
        # Test creating Data instance and default joint initialization
        data = Data()
        for joint_id in range(1, JOINTS + 1):
            joint = data.get_joint(joint_id)
            self.assertIsNotNone(joint)
            self.assertEqual(joint.get("x"), 0)
            self.assertEqual(joint.get("y"), 0)
            self.assertEqual(joint.get("z"), 0)

    def test_data_set_joint(self):
        # Test setting joint values in Data instance
        data = Data()
        data.set_joint(1, 10, 20, 30)
        joint = data.get_joint(1)
        self.assertEqual(joint.get("x"), 10)
        self.assertEqual(joint.get("y"), 20)
        self.assertEqual(joint.get("z"), 30)

    def test_data_set_joint_invalid_id(self):
        # Test setting joint with invalid joint id
        data = Data()
        data.set_joint(100, 10, 20, 30)  # Invalid joint ID
        joint = data.get_joint(100)  # Should be None
        self.assertIsNone(joint)

    def test_data_get_joint(self):
        # Test retrieving a joint by id from Data
        data = Data()
        joint = data.get_joint(1)
        self.assertIsNotNone(joint)
        self.assertEqual(joint.get("x"), 0)
        self.assertEqual(joint.get("y"), 0)
        self.assertEqual(joint.get("z"), 0)

    def test_data_str_method(self):
        # Test the __str__ method for Data (JSON output)
        data = Data()
        expected_json = json.dumps(
            {
                1: {"x": 0, "y": 0, "z": 0},
                2: {"x": 0, "y": 0, "z": 0},
                3: {"x": 0, "y": 0, "z": 0},
                4: {"x": 0, "y": 0, "z": 0},
                5: {"x": 0, "y": 0, "z": 0},
                6: {"x": 0, "y": 0, "z": 0},
            }
        )
        self.assertEqual(data.__str__(), expected_json)


if __name__ == "__main__":
    unittest.main()
