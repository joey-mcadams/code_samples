import collections

from .models import Dimension

"""
1. Explain what SQL queries your solution is making and why.
    "get" and "filter" are both setting up SQL queries for lazy evaluation. 
    Those are executed when I access the data referenced by those queries. 


2. Assume there are hundreds of dimensions and the hierarchy is loaded on every page load. What caching strategies
would you suggest?
    - Hint: The answer here is not a SQL query using `RECURSIVE`.

    Depends on how often they're updated / TPS.  

    Based on those numbers, go with one of these: 
    https://www.prisma.io/dataguide/managing-databases/introduction-database-caching

    But in the end, we're pretty much forced to use a SQL query with 'RECURSIVE'.  
"""


def list_children(dimension_id: int) -> list | None:
    """ List a dimension and all its children in a nested hierarchy. """
    data = Dimension.objects.all()

    output = _get_children_from_parent(data, dimension_id)
    return output


def list_hierarchy(company_id: int) -> list:
    """ List the complete nested hierarchy for a company. """
    data = Dimension.objects.all()
    top_level_dimensions = filter(lambda x: (x.company_id == company_id and x.parent_id is None), data)

    hierarchies = []
    for dimension in top_level_dimensions:
        hierarchies.extend(_get_children_from_parent(data, dimension.id))
    return hierarchies


def _get_children_from_parent(data: collections.Iterable, dimension_id: int) -> list:
    """
    Gets a list of children for a given dimension ID.

    :param data: The SQL database rows
    :param dimension_id: The ID of the dimension we are looking for.
    """
    out_list = []
    for element in data:
        if element.id == dimension_id:
            out_list.append(element.name)
            if element.has_children:
                out_list.extend(_get_children(data, element, [], 1))

    return out_list


def _get_children(data, element, out_list, depth=0) -> list:
    """
    Recursive function to get each child of a dimension that has children.

    :param data: The SQL database rows
    :param element: The element to get children for
    :param out_list: Used for recursion, initialize with []
    :param depth: Used for recursion, initialize with 0
    """
    # TODO: Can likely make this and _get_children_from_parent one function.
    # Was just focusing on making 1 SQL call.

    for row in data:
        if row.parent_id == element.id:
            out_list.append(depth * "\t" + row.name)
            if row.has_children:
                out_list.extend(_get_children(data, row, [], depth + 1))

    return out_list
