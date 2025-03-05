# ADProtectionGroupParams

Specifies the parameters which are specific to Active directory related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[ActiveDirectoryProtectionGroupObjectParams]**](ActiveDirectoryProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 

## Example

```python
from cohesity_sdk.models.ad_protection_group_params import ADProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of ADProtectionGroupParams from a JSON string
ad_protection_group_params_instance = ADProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(ADProtectionGroupParams.to_json())

# convert the object into a dict
ad_protection_group_params_dict = ad_protection_group_params_instance.to_dict()
# create an instance of ADProtectionGroupParams from a dict
ad_protection_group_params_from_dict = ADProtectionGroupParams.from_dict(ad_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


