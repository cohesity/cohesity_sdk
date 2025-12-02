# GcpMySQLMetadata

Specifies the metadata types and values of GCP MySQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_my_sql_metadata import GcpMySQLMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMySQLMetadata from a JSON string
gcp_my_sql_metadata_instance = GcpMySQLMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpMySQLMetadata.to_json())

# convert the object into a dict
gcp_my_sql_metadata_dict = gcp_my_sql_metadata_instance.to_dict()
# create an instance of GcpMySQLMetadata from a dict
gcp_my_sql_metadata_from_dict = GcpMySQLMetadata.from_dict(gcp_my_sql_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


