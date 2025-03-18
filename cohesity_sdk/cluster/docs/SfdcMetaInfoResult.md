# SfdcMetaInfoResult

Specifies the meta info params for salesforce object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_objects** | [**List[SfdcDependentObject]**](SfdcDependentObject.md) | Specifies the list of child objects. | [optional] 
**parent_objects** | [**List[SfdcDependentObject]**](SfdcDependentObject.md) | Specifies the list of parent objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sfdc_meta_info_result import SfdcMetaInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcMetaInfoResult from a JSON string
sfdc_meta_info_result_instance = SfdcMetaInfoResult.from_json(json)
# print the JSON string representation of the object
print(SfdcMetaInfoResult.to_json())

# convert the object into a dict
sfdc_meta_info_result_dict = sfdc_meta_info_result_instance.to_dict()
# create an instance of SfdcMetaInfoResult from a dict
sfdc_meta_info_result_from_dict = SfdcMetaInfoResult.from_dict(sfdc_meta_info_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


