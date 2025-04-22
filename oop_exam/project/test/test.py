from project.climbing_robot import ClimbingRobot

import unittest

class TestClimbingRobot(unittest.TestCase):
    def test_valid_constructor_values(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        self.assertEqual(robot.category, 'Mountain')
        self.assertEqual(robot.part_type, 'Legs')
        self.assertEqual(robot.capacity, 100)
        self.assertEqual(robot.memory, 200)
        self.assertEqual(robot.installed_software, [])

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as context:
            ClimbingRobot('InvalidCategory', 'Legs', 100, 200)

        expected_message = "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']"
        self.assertEqual(str(context.exception), expected_message)

    def test_constructor_types(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)

        self.assertIsInstance(robot.category, str)
        self.assertIsInstance(robot.part_type, str)
        self.assertIsInstance(robot.capacity, int)
        self.assertIsInstance(robot.memory, int)
        self.assertIsInstance(robot.installed_software, list)

    def test_get_used_capacity_no_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        expected_value = 0
        self.assertEqual(robot.get_used_capacity(), expected_value)

    def test_get_used_capacity_with_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}
        software2 = {'name': 'Software2', 'capacity_consumption': 30, 'memory_consumption': 20}

        robot.install_software(software1)
        robot.install_software(software2)

        expected_value = software1['capacity_consumption'] + software2['capacity_consumption']
        self.assertEqual(robot.get_used_capacity(), expected_value)

    def test_get_used_capacity_with_duplicate_installed_software(self):

        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}

        robot.install_software(software1)
        robot.install_software(software1)  # Installing the same software again

        expected_value = software1['capacity_consumption'] *2
        self.assertEqual(expected_value, robot.get_used_capacity())

    def test_get_used_capacity_with_no_available_capacity(self):
        robot = ClimbingRobot('Mountain', 'Legs', 50, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 60, 'memory_consumption': 30}

        result = robot.install_software(software1)

        expected_value = 0
        self.assertEqual(robot.get_used_capacity(), expected_value)
        self.assertIn("cannot be installed", result)

    def test_get_available_capacity_no_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        expected_value = 100  # Initial capacity
        self.assertEqual(expected_value, robot.get_available_capacity())

    def test_get_available_capacity_with_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}
        software2 = {'name': 'Software2', 'capacity_consumption': 30, 'memory_consumption': 20}

        robot.install_software(software1)
        robot.install_software(software2)

        expected_value = 100 - (software1['capacity_consumption'] + software2['capacity_consumption'])
        self.assertEqual(expected_value, robot.get_available_capacity())

    def test_get_available_capacity_with_no_initial_capacity(self):
        robot = ClimbingRobot('Mountain', 'Legs', 0, 200)
        expected_value = 0  # Initial capacity is 0
        self.assertEqual(expected_value, robot.get_available_capacity())

    def test_get_available_capacity_with_negative_available_capacity(self):
        robot = ClimbingRobot('Mountain', 'Legs', 50, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 60, 'memory_consumption': 30}

        result = robot.install_software(software1)

        expected_value = 50  # Capacity cannot be negative
        self.assertEqual(expected_value, robot.get_available_capacity())
        self.assertIn("cannot be installed", result)

    def test_get_used_memory_no_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        expected_value = 0  # No software installed
        self.assertEqual(expected_value, robot.get_used_memory())

    def test_get_used_memory_with_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}
        software2 = {'name': 'Software2', 'capacity_consumption': 30, 'memory_consumption': 20}

        robot.install_software(software1)
        robot.install_software(software2)

        expected_value = software1['memory_consumption'] + software2['memory_consumption']
        self.assertEqual(expected_value, robot.get_used_memory())

    def test_get_used_memory_with_duplicate_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}

        robot.install_software(software1)
        robot.install_software(software1)  # Installing the same software again

        expected_value = software1['memory_consumption'] *2
        self.assertEqual(expected_value, robot.get_used_memory())

    def test_get_used_memory_with_no_available_memory(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 50)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 60}

        result = robot.install_software(software1)

        expected_value = 0
        self.assertEqual(expected_value, robot.get_used_memory())
        self.assertIn("cannot be installed", result)

    def test_get_available_memory_no_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        expected_value = 200
        self.assertEqual(expected_value, robot.get_available_memory())

    def test_get_available_memory_with_installed_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}
        software2 = {'name': 'Software2', 'capacity_consumption': 30, 'memory_consumption': 20}

        robot.install_software(software1)
        robot.install_software(software2)

        expected_value = 200 - (software1['memory_consumption'] + software2['memory_consumption'])
        self.assertEqual(expected_value, robot.get_available_memory())

    def test_get_available_memory_with_no_initial_memory(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 0)
        expected_value = 0
        self.assertEqual(expected_value, robot.get_available_memory())

    def test_get_available_memory_with_negative_available_memory(self):
        robot = ClimbingRobot('Mountain', 'Legs', 50, 100)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 60}

        result = robot.install_software(software1)

        expected_value = 40
        self.assertEqual(expected_value, robot.get_available_memory())

    def test_install_software_successful(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}

        result = robot.install_software(software1)

        expected_message = f"Software '{software1['name']}' successfully installed on {robot.category} part."
        self.assertEqual(expected_message, result)
        self.assertIn(software1, robot.installed_software)

    def test_install_software_insufficient_capacity(self):
        robot = ClimbingRobot('Mountain', 'Legs', 50, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 60, 'memory_consumption': 30}

        result = robot.install_software(software1)

        expected_message = f"Software '{software1['name']}' cannot be installed on {robot.category} part."
        self.assertEqual(expected_message, result)
        self.assertNotIn(software1, robot.installed_software)

    def test_install_software_insufficient_memory(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 30)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 40}

        result = robot.install_software(software1)

        expected_message = f"Software '{software1['name']}' cannot be installed on {robot.category} part."
        self.assertEqual(expected_message, result)
        self.assertNotIn(software1, robot.installed_software)

    def test_install_software_insufficient_capacity_and_memory(self):
        robot = ClimbingRobot('Mountain', 'Legs', 50, 30)
        software1 = {'name': 'Software1', 'capacity_consumption': 60, 'memory_consumption': 40}

        result = robot.install_software(software1)

        expected_message = f"Software '{software1['name']}' cannot be installed on {robot.category} part."
        self.assertEqual(expected_message, result)
        self.assertNotIn(software1, robot.installed_software)

    def test_install_software_with_available_capacity_and_memory(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}

        result = robot.install_software(software1)

        expected_message = f"Software '{software1['name']}' successfully installed on {robot.category} part."
        self.assertEqual(expected_message, result)
        self.assertIn(software1, robot.installed_software)

    def test_install_software_with_duplicate_software(self):
        robot = ClimbingRobot('Mountain', 'Legs', 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 50, 'memory_consumption': 30}

        robot.install_software(software1)
        result = robot.install_software(software1)

        expected_message = f"Software '{software1['name']}' successfully installed on {robot.category} part."
        self.assertEqual(expected_message, result)
        self.assertIn(software1, robot.installed_software)


if __name__ == '__main__':
    unittest.main()
