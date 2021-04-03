#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 23:18
# @Author  : Jack
class UndirectedGraph(object):
    """undirected graph"""
    def __init__(self, vertex_num):
        self._vertex_num = vertex_num   # the number of vertices.
        # from scratch. the adjacency list
        self._adj_list = [[] for _ in range(vertex_num)]

    def add_edge(self, s: int, t: int) -> bool:
        """
        making a connection between two vertices
        :param s: a vertex
        :param t: another vertex
        :return: True or False
        """
        if s > self._vertex_num or t > self._vertex_num:
            return False
        self._adj_list[s].append(t)
        self._adj_list[t].append(s)
        return True

    def __str__(self):
        # the __str__ attribute must return string data
        return str(self._adj_list)

    def __len__(self):
        # Calling the len() function is essentially calling the __len__() function.
        return self._vertex_num

    def __getitem__(self, ind):
        # By this way, the objects generated by this class can be iterated.
        if ind > self._vertex_num:
            raise IndexError("No Such Vertex!")
        return self._adj_list[ind]


class DirectedGraph(object):
    """Directed graph."""
    def __init__(self, vertex_num):
        self._vertex_num = vertex_num   # the number of vertices.
        # from scratch. the adjacency list.
        self._adj_list = [[] for _ in range(vertex_num)]

    def add_edge(self, from_vertex, to_vertex):
        """
        one vertex points to_vertex another
        :param from_vertex: previous vertex
        :param to_vertex: next vertex
        :return: True or False
        """
        if from_vertex > self._vertex_num or to_vertex > self._vertex_num:
            return False
        self._adj_list[from_vertex].append(to_vertex)
        return True

    def __str__(self):
        return str(self._adj_list)

    def __len__(self):
        # Calling the len() function is essentially calling the __len__() function.
        return self._vertex_num

if __name__ == "__main__":
    ug = UndirectedGraph(10)
    ug.add_edge(1, 9)
    ug.add_edge(1, 3)
    ug.add_edge(3, 2)
    print(ug)

    dg = DirectedGraph(10)
    dg.add_edge(1, 9)
    dg.add_edge(1, 3)
    dg.add_edge(3, 4)

