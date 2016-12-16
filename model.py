from random import random
from math import cos, sin, pi


def coords_sum(first_coordinates, second_coordinates):
    return first_coordinates[0] + second_coordinates[0],\
           first_coordinates[1] + second_coordinates[1]


EDGE_LENGTH = 2
LEFT_DELTA_ANGLE = 0.4
RIGHT_DELTA_ANGLE = 0.4
SPLIT_PROBABILITY = 0.02
CIRCLE_RADIUS = 1


class Circle:
    def __init__(self, radius, alpha, coords):
        self.radius = radius
        self.alpha = alpha
        self.coords = coords

    def __repr__(self):
        return "Circle({}, {}, {}".format(self.radius, self.alpha, self.coords)


class TreeNode:
    def __init__(self, left_child, right_child, circle, delta, node_id):
        self.right_child = right_child
        self.left_child = left_child
        self.circle = circle
        self.delta = delta
        self.node_id = node_id


class Tree:
    def __init__(self):
        self.root = TreeNode(None, None, Circle(CIRCLE_RADIUS, 1, (0, 400)), 0, 0)
        self.root.left_child = TreeNode(None, None, Circle(CIRCLE_RADIUS, 1, (0, 400)), 0, 1)
        self.leaves = [self.root.left_child]

    def grow(self):
        new_leaves = []
        for leaf in self.leaves:
            radius = leaf.circle.radius
            node_id = leaf.node_id
            if random() > SPLIT_PROBABILITY:
                """
                new_leaf = TreeNode(None, None,
                                    Circle(radius, 1,
                                           coords_sum(
                                               leaf.circle.coords,
                                               (EDGE_LENGTH * cos(leaf.delta),
                                                EDGE_LENGTH * sin(leaf.delta)))), leaf.delta)
                leaf.left_child = new_leaf
                new_leaves.append(new_leaf)
                """
                leaf.circle.coords = coords_sum(leaf.circle.coords,
                                                (EDGE_LENGTH * cos(leaf.delta),
                                                 EDGE_LENGTH * sin(leaf.delta)))
                new_leaves.append(leaf)
            else:
                new_left_leaf = TreeNode(None, None,
                                         Circle(radius, 1,
                                                coords_sum(
                                                    leaf.circle.coords,
                                                    (EDGE_LENGTH * cos(leaf.delta),
                                                     EDGE_LENGTH * sin(leaf.delta)))), leaf.delta - LEFT_DELTA_ANGLE, node_id + 1)
                new_right_leaf = TreeNode(None, None,
                                          Circle(radius, 1,
                                                 coords_sum(
                                                     leaf.circle.coords,
                                                     (EDGE_LENGTH * cos(leaf.delta),
                                                      EDGE_LENGTH * sin(leaf.delta)))), leaf.delta + RIGHT_DELTA_ANGLE, node_id + 1)
                leaf.left_child = new_left_leaf
                leaf.right_child = new_right_leaf
                new_leaves.append(new_left_leaf)
                new_leaves.append(new_right_leaf)
        self.leaves = new_leaves
