# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2021-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from setuptools import setup

package_name = 'isaac_ros_mqtt_bridge'

setup(
    name=package_name,
    version='0.31.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Isaac ROS Maintainers',
    maintainer_email='isaac-ros-maintainers@nvidia.com',
    description='MQTT Bridge',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mqtt_to_ros_bridge_node = isaac_ros_mqtt_bridge.MqttToRosNode:main',
            'ros_to_mqtt_bridge_node = isaac_ros_mqtt_bridge.RosToMqttNode:main',
            'turtlebot4_mqtt_to_ros_bridge_node = isaac_ros_mqtt_bridge.MqttToRosNodeTurtlebot4:main',
            'turtlebot4_ros_to_mqtt_bridge_node = isaac_ros_mqtt_bridge.RosToMqttNodeTurtlebot4:main'
        ],
    },
)
