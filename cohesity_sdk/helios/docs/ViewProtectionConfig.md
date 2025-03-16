# ViewProtectionConfig

Specifies the View protection config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_group_param** | [**ExistingGroupParam**](ExistingGroupParam.md) | Specifies the parameters used for existing protection group. | [optional] 
**new_group_param** | [**NewGroupParam**](NewGroupParam.md) | Specifies the parameters used for new protection group. | [optional] 
**protection_group_type** | **str** | Specifies the View protection group type. | 

## Example

```python
from cohesity_sdk.helios.models.view_protection_config import ViewProtectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ViewProtectionConfig from a JSON string
view_protection_config_instance = ViewProtectionConfig.from_json(json)
# print the JSON string representation of the object
print(ViewProtectionConfig.to_json())

# convert the object into a dict
view_protection_config_dict = view_protection_config_instance.to_dict()
# create an instance of ViewProtectionConfig from a dict
view_protection_config_from_dict = ViewProtectionConfig.from_dict(view_protection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


