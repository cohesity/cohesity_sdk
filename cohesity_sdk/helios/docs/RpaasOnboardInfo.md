# RpaasOnboardInfo

Defines the onboarding status for RPaaS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** | Specifies whether the onboarding is complete. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_onboard_info import RpaasOnboardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasOnboardInfo from a JSON string
rpaas_onboard_info_instance = RpaasOnboardInfo.from_json(json)
# print the JSON string representation of the object
print(RpaasOnboardInfo.to_json())

# convert the object into a dict
rpaas_onboard_info_dict = rpaas_onboard_info_instance.to_dict()
# create an instance of RpaasOnboardInfo from a dict
rpaas_onboard_info_from_dict = RpaasOnboardInfo.from_dict(rpaas_onboard_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


