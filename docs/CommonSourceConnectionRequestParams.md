# CommonSourceConnectionRequestParams

Specifies the common set of parameters to test connectivity with a source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | 

## Example

```python
from cohesity_sdk.models.common_source_connection_request_params import CommonSourceConnectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSourceConnectionRequestParams from a JSON string
common_source_connection_request_params_instance = CommonSourceConnectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(CommonSourceConnectionRequestParams.to_json())

# convert the object into a dict
common_source_connection_request_params_dict = common_source_connection_request_params_instance.to_dict()
# create an instance of CommonSourceConnectionRequestParams from a dict
common_source_connection_request_params_from_dict = CommonSourceConnectionRequestParams.from_dict(common_source_connection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


