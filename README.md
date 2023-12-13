RL-Warehouse
A sample Q-learning code

Source: https://www.youtube.com/watch?v=iKdlKYG78j4

Original Jupyter notebook: https://colab.research.google.com/drive/1E2RViy7xmor0mhqskZV14_NUj2jMpJz3


Scenario - Robots in a Warehouse
A growing e-commerce company is building a new warehouse, and the company would like all of the picking operations in the new warehouse to be performed by warehouse robots.

In the context of e-commerce warehousing, “picking” is the task of gathering individual items from various locations in the warehouse in order to fulfill customer orders.
After picking items from the shelves, the robots must bring the items to a specific location within the warehouse where the items can be packaged for shipping.

In order to ensure maximum efficiency and productivity, the robots will need to learn the shortest path between the item packaging area and all other locations within the warehouse where the robots are allowed to travel.

We will use Q-learning to accomplish this task!


I added a grid view to the test section ...