# GcpSqlServerMetadata

Specifies the metadata types and values of GCP SQL Server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_sql_server_metadata import GcpSqlServerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSqlServerMetadata from a JSON string
gcp_sql_server_metadata_instance = GcpSqlServerMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpSqlServerMetadata.to_json())

# convert the object into a dict
gcp_sql_server_metadata_dict = gcp_sql_server_metadata_instance.to_dict()
# create an instance of GcpSqlServerMetadata from a dict
gcp_sql_server_metadata_from_dict = GcpSqlServerMetadata.from_dict(gcp_sql_server_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


