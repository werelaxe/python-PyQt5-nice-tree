from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from math import log, log10

from PyQt5.QtGui import QPen

import model


def draw_circle(circle: model.Circle, qp: QPainter):
    qp.drawEllipse(circle.coords[0] - circle.radius,
                   circle.coords[1] - circle.radius,
                   circle.radius, circle.radius)


def draw_edge(first_tree_node: model.TreeNode, second_tree_node: model.TreeNode, qp: QPainter):

    first_x, first_y = first_tree_node.circle.coords
    second_x, second_y = second_tree_node.circle.coords
    first_radius = first_tree_node.circle.radius // 2
    second_radius = second_tree_node.circle.radius // 2
    qp.drawLine(first_x - first_radius, first_y - first_radius,
                second_x - second_radius, second_y - second_radius)


def draw_node(tree_node: model.TreeNode, prev_tree_node: model.TreeNode, qp: QPainter):
    factor = min(255, 512 / (tree_node.node_id + 1))
    qp.setPen(QPen(QColor(255, factor, 0), 10 / log(tree_node.node_id + 2), Qt.SolidLine))
    draw_edge(tree_node, prev_tree_node, qp)
    draw_circle(tree_node.circle, qp)
    if tree_node.left_child is not None:
        draw_node(tree_node.left_child, tree_node, qp)
    if tree_node.right_child is not None:
        draw_node(tree_node.right_child, tree_node, qp)


def draw_tree(tree: model.Tree, qp: QPainter):
    draw_node(tree.root, tree.root, qp)
