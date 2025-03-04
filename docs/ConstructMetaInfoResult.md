# ConstructMetaInfoResult

Result to store meta-info from an object snapshot and additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment type for fetching the meta Info. | [optional] 
**oracle_params** | [**OracleRestoreMetaInfoResult**](OracleRestoreMetaInfoResult.md) |  | [optional] 
**sfdc_params** | [**SfdcMetaInfoResult**](SfdcMetaInfoResult.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.construct_meta_info_result import ConstructMetaInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructMetaInfoResult from a JSON string
construct_meta_info_result_instance = ConstructMetaInfoResult.from_json(json)
# print the JSON string representation of the object
print(ConstructMetaInfoResult.to_json())

# convert the object into a dict
construct_meta_info_result_dict = construct_meta_info_result_instance.to_dict()
# create an instance of ConstructMetaInfoResult from a dict
construct_meta_info_result_from_dict = ConstructMetaInfoResult.from_dict(construct_meta_info_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


