import json

JOINTS = 6


class Joint:
    def __init__(self, x, y, z):
        self.values = {"x": x, "y": y, "z": z}

    def get(self, key):
        return self.values.get(key)

    def set(self, key, value):
        self.values[key] = value

    def to_dict(self):
        return self.values

    def __str__(self):
        return json.dumps(self.values)


class Data:
    def __init__(self):
        self.joints = {}
        for i in range(JOINTS):
            self.joints[i + 1] = Joint(0, 0, 0)

    def get_joint(self, joint_id):
        return self.joints.get(joint_id)

    def set_joint(self, joint_id, x, y, z):
        joint = self.get_joint(joint_id)
        if joint:
            joint.set("x", x)
            joint.set("y", y)
            joint.set("z", z)

    def __str__(self):
        # Convert the joints to a dictionary with each joint serialized properly
        return json.dumps(self.joints, default=lambda o: o.to_dict())
