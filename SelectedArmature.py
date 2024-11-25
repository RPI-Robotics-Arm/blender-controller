import bpy

class Joint:
    """
    Represents a single joint with its world-space location in Pose Mode.
    """
    def __init__(self, armature, joint_name):
        self.name = joint_name
        self.location = {}  # To store the joint's (x, y, z) location in world space

        # Ensure the armature has the joint
        if joint_name in armature.pose.bones:
            bone = armature.pose.bones[joint_name]

            # Compute world-space location
            world_position = armature.matrix_world @ bone.matrix.translation
            
            # round to three decimal places
            self.location['x'] = round(world_position.x, 3)
            self.location['y'] = round(world_position.y, 3)
            self.location['z'] = round(world_position.z, 3)
            
        else:
            raise ValueError(f"Joint '{joint_name}' not found in armature '{armature.name}'.")

    def __str__(self):
        if self.location:
            return (f"Joint: {self.name}, "
                    f"Location: X: {self.location['x']}, Y: {self.location['y']}, Z: {self.location['z']}")
        return f"Joint: {self.name}, Location: Not Found"


class JointCollection:
    # Hold all joints (1-6 inclusive)
    def __init__(self):
        self.joints = []

    def add_joint(self, joint):
        self.joints.append(joint)

    def __str__(self):
        return "\n".join(str(joint) for joint in self.joints)


def main():
    # Ensure an armature object is selected
    if bpy.context.object and bpy.context.object.type == 'ARMATURE':
        armature = bpy.context.object  # Get the selected armature object

        # Enter Pose Mode to access bone transformations
        bpy.ops.object.mode_set(mode='POSE')

        # Create the joint collection
        joint_collection = JointCollection()

        # List of joint names to create (j1 to j5)
        joint_names = [f"j{i}" for i in range(1, 7)]

        # Add each joint to the collection
        for joint_name in joint_names:
            try:
                joint = Joint(armature, joint_name)
                joint_collection.add_joint(joint)
            except ValueError as e:
                print(e)

        # Print all joint positions
        print("Joint positions:")
        print(joint_collection)

        # Return to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')

    else:
        print("Please select an Armature object.")


# Run the main function
if __name__ == "__main__":
    main()
