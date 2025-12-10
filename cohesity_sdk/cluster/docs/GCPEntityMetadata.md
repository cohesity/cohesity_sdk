# GCPEntityMetadata

Specifies the entity metadata of GCP entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloy_db_postgre_sql_params** | [**GcpAlloyDBPostgreSQLEntityMetadata**](GcpAlloyDBPostgreSQLEntityMetadata.md) |  | [optional] 
**gcp_sql_params** | [**GcpSqlServerMetadata**](GcpSqlServerMetadata.md) |  | [optional] 
**my_sql_params** | [**GcpMySQLEntityMetadata**](GcpMySQLEntityMetadata.md) |  | [optional] 
**postgre_sql_params** | [**GcpPostgreSQLEntityMetadata**](GcpPostgreSQLEntityMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_entity_metadata import GCPEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GCPEntityMetadata from a JSON string
gcp_entity_metadata_instance = GCPEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(GCPEntityMetadata.to_json())

# convert the object into a dict
gcp_entity_metadata_dict = gcp_entity_metadata_instance.to_dict()
# create an instance of GCPEntityMetadata from a dict
gcp_entity_metadata_from_dict = GCPEntityMetadata.from_dict(gcp_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


