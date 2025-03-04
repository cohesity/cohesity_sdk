# HostSettingCheck

Specifies the host checking details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Specifies the result of host checking performed by agent. | [optional] 
**type** | **str** | Specifies the type of host checking that was performed. | [optional] 

## Example

```python
from cohesity_sdk.models.host_setting_check import HostSettingCheck

# TODO update the JSON string below
json = "{}"
# create an instance of HostSettingCheck from a JSON string
host_setting_check_instance = HostSettingCheck.from_json(json)
# print the JSON string representation of the object
print(HostSettingCheck.to_json())

# convert the object into a dict
host_setting_check_dict = host_setting_check_instance.to_dict()
# create an instance of HostSettingCheck from a dict
host_setting_check_from_dict = HostSettingCheck.from_dict(host_setting_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


