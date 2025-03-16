# SfdcProtectionGroupParams

Specifies the parameters to create SFDC Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[SfdcProtectionGroupObjectParams]**](SfdcProtectionGroupObjectParams.md) | Specifies the list of objects to be protected. | 

## Example

```python
from cohesity_sdk.cluster.models.sfdc_protection_group_params import SfdcProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcProtectionGroupParams from a JSON string
sfdc_protection_group_params_instance = SfdcProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(SfdcProtectionGroupParams.to_json())

# convert the object into a dict
sfdc_protection_group_params_dict = sfdc_protection_group_params_instance.to_dict()
# create an instance of SfdcProtectionGroupParams from a dict
sfdc_protection_group_params_from_dict = SfdcProtectionGroupParams.from_dict(sfdc_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


