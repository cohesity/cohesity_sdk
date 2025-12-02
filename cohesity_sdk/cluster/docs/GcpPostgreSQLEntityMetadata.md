# GcpPostgreSQLEntityMetadata

Specifies the entity metadata of GCP PostgreSQL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[GcpPostgreSQLMetadata]**](GcpPostgreSQLMetadata.md) | Specifies the metadata list. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_postgre_sql_entity_metadata import GcpPostgreSQLEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPostgreSQLEntityMetadata from a JSON string
gcp_postgre_sql_entity_metadata_instance = GcpPostgreSQLEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpPostgreSQLEntityMetadata.to_json())

# convert the object into a dict
gcp_postgre_sql_entity_metadata_dict = gcp_postgre_sql_entity_metadata_instance.to_dict()
# create an instance of GcpPostgreSQLEntityMetadata from a dict
gcp_postgre_sql_entity_metadata_from_dict = GcpPostgreSQLEntityMetadata.from_dict(gcp_postgre_sql_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


