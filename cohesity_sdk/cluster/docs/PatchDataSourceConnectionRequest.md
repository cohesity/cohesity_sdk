# PatchDataSourceConnectionRequest

Specifies the properties of a data-source connection to patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_vips** | **List[str]** | List of cluster virtual IPs associated with the connection. | [optional] 
**connection_name** | **str** | New name for the connection being patched. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.patch_data_source_connection_request import PatchDataSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDataSourceConnectionRequest from a JSON string
patch_data_source_connection_request_instance = PatchDataSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchDataSourceConnectionRequest.to_json())

# convert the object into a dict
patch_data_source_connection_request_dict = patch_data_source_connection_request_instance.to_dict()
# create an instance of PatchDataSourceConnectionRequest from a dict
patch_data_source_connection_request_from_dict = PatchDataSourceConnectionRequest.from_dict(patch_data_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


