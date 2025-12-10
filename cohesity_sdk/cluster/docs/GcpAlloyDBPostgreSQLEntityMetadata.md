# GcpAlloyDBPostgreSQLEntityMetadata

Specifies the entity metadata of GCP AlloyDB PostgreSQL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[GcpAlloyDBPostgreSQLMetadata]**](GcpAlloyDBPostgreSQLMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_alloy_db_postgre_sql_entity_metadata import GcpAlloyDBPostgreSQLEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpAlloyDBPostgreSQLEntityMetadata from a JSON string
gcp_alloy_db_postgre_sql_entity_metadata_instance = GcpAlloyDBPostgreSQLEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpAlloyDBPostgreSQLEntityMetadata.to_json())

# convert the object into a dict
gcp_alloy_db_postgre_sql_entity_metadata_dict = gcp_alloy_db_postgre_sql_entity_metadata_instance.to_dict()
# create an instance of GcpAlloyDBPostgreSQLEntityMetadata from a dict
gcp_alloy_db_postgre_sql_entity_metadata_from_dict = GcpAlloyDBPostgreSQLEntityMetadata.from_dict(gcp_alloy_db_postgre_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


