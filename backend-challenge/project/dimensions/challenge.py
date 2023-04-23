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


"""
TODO: Figure out how to run this with Django 

with recursive parent(id, name, level) as (values (1, "ACCOUNT", 0)
                                           union
                                           select dimensions_dimension.id, dimensions_dimension.name, parent.level + 1
                                           from dimensions_dimension,
                                                parent
                                           where dimensions_dimension.parent_id = parent.id
                                           order by 1
    ) select substr(".................", 1, level) || name from parent
"""


def list_children(dimension_id: int) -> list | None:
    """ List a dimension and all its children in a nested hierarchy. """
    dim_parent = Dimension.objects.get(id=dimension_id)

    if dim_parent.has_children:  # This will reduce the number of queries.
        return _get_children_from_parent(dim_parent, [], 0)
    else:
        return [dim_parent.name]


def list_hierarchy(company_id: int) -> list:
    """ List the complete nested hierarchy for a company. """
    top_level_dimensions = Dimension.objects.filter(company_id=company_id, parent_id=None)
    hierarchies = []
    for dimension in top_level_dimensions:
        hierarchies.extend(_get_children_from_parent(dimension, [], 0))
    return hierarchies


def _get_children_from_parent(parent: object, child_list: list, depth: int) -> list:
    """
    Recursively look for children of a parent and return that list of children.

    :param parent: A Dimension object representing the parent
    :param child_list: Used for recursion. Should be set as a [] list to start this function
    :param depth: Used for recursion. Should be set as 0 to start.
    """
    child_list.append(depth * "\t" + parent.name)

    dim_children = Dimension.objects.filter(parent_id=parent.id)

    for child in dim_children:
        if child.has_children:
            _get_children_from_parent(child, child_list, depth + 1)
        else:
            child_list.append((depth + 1) * "\t" + child.name)

    return child_list