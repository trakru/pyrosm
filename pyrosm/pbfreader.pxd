cpdef parse_osm_data(filepath, bounding_box, exclude_relations)
cpdef get_way_data(ways, way_tags_to_keep, network_filter)
cdef get_primitive_blocks_and_string_tables(filepath)
cdef parse_dense(pblock, data, string_table, bounding_box)
cdef parse_nodes(pblock, data, bounding_box)
cdef parse_ways(data, stringtable, node_lookup)