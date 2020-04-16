import pytest
from pyrosm import get_path


@pytest.fixture
def test_pbf():
    pbf_path = get_path("test_pbf")
    return pbf_path


def test_parsing_landuse_with_defaults(test_pbf):
    from pyrosm import OSM
    from pyrosm.landuse import get_landuse_data
    from geopandas import GeoDataFrame
    import pyproj
    from pyrosm._arrays import concatenate_dicts_of_arrays
    osm = OSM(filepath=test_pbf)
    osm._read_pbf()
    tags_as_columns = osm.conf.tags.landuse

    nodes = concatenate_dicts_of_arrays(osm._nodes)
    gdf = get_landuse_data(nodes,
                           osm._node_coordinates,
                           osm._way_records,
                           osm._relations,
                           tags_as_columns,
                           None)

    assert isinstance(gdf, GeoDataFrame)

    # Required keys
    required = ['id', 'geometry']
    for col in required:
        assert col in gdf.columns

    # Test shape
    assert len(gdf) == 50
    assert gdf.crs == pyproj.CRS.from_epsg(4326)
