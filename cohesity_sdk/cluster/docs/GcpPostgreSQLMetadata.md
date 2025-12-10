# GcpPostgreSQLMetadata

Specifies the metadata types and values of GCP PostgreSQL Server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_postgre_sql_metadata import GcpPostgreSQLMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPostgreSQLMetadata from a JSON string
gcp_postgre_sql_metadata_instance = GcpPostgreSQLMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpPostgreSQLMetadata.to_json())

# convert the object into a dict
gcp_postgre_sql_metadata_dict = gcp_postgre_sql_metadata_instance.to_dict()
# create an instance of GcpPostgreSQLMetadata from a dict
gcp_postgre_sql_metadata_from_dict = GcpPostgreSQLMetadata.from_dict(gcp_postgre_sql_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


