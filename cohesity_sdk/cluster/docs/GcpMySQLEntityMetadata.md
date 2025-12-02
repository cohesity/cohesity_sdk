# GcpMySQLEntityMetadata

Specifies the entity metadata of GCP MySQL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[GcpMySQLMetadata]**](GcpMySQLMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_my_sql_entity_metadata import GcpMySQLEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMySQLEntityMetadata from a JSON string
gcp_my_sql_entity_metadata_instance = GcpMySQLEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpMySQLEntityMetadata.to_json())

# convert the object into a dict
gcp_my_sql_entity_metadata_dict = gcp_my_sql_entity_metadata_instance.to_dict()
# create an instance of GcpMySQLEntityMetadata from a dict
gcp_my_sql_entity_metadata_from_dict = GcpMySQLEntityMetadata.from_dict(gcp_my_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


