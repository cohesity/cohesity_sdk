# ConstructMetaInfoRequest

Params to construct meta info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment type of the Protection group | 
**oracle_params** | [**ConstructRestoreMetaInfoOracleParams**](ConstructRestoreMetaInfoOracleParams.md) |  | [optional] 
**sfdc_params** | [**ConstructMetaInfoSfdcParams**](ConstructMetaInfoSfdcParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.construct_meta_info_request import ConstructMetaInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructMetaInfoRequest from a JSON string
construct_meta_info_request_instance = ConstructMetaInfoRequest.from_json(json)
# print the JSON string representation of the object
print(ConstructMetaInfoRequest.to_json())

# convert the object into a dict
construct_meta_info_request_dict = construct_meta_info_request_instance.to_dict()
# create an instance of ConstructMetaInfoRequest from a dict
construct_meta_info_request_from_dict = ConstructMetaInfoRequest.from_dict(construct_meta_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


