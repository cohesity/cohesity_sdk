# FortknoxProvisionStatus

The provision status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the status message. | [optional] 
**status** | **str** | Specifies the status code. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_provision_status import FortknoxProvisionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxProvisionStatus from a JSON string
fortknox_provision_status_instance = FortknoxProvisionStatus.from_json(json)
# print the JSON string representation of the object
print(FortknoxProvisionStatus.to_json())

# convert the object into a dict
fortknox_provision_status_dict = fortknox_provision_status_instance.to_dict()
# create an instance of FortknoxProvisionStatus from a dict
fortknox_provision_status_from_dict = FortknoxProvisionStatus.from_dict(fortknox_provision_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


