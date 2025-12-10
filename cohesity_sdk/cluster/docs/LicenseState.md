# LicenseState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_attempts** | **int** | Specifies no of failed attempts at claiming the license server | [optional] 
**state** | **str** | Specifies the current state of licensing workflow. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.license_state import LicenseState

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseState from a JSON string
license_state_instance = LicenseState.from_json(json)
# print the JSON string representation of the object
print(LicenseState.to_json())

# convert the object into a dict
license_state_dict = license_state_instance.to_dict()
# create an instance of LicenseState from a dict
license_state_from_dict = LicenseState.from_dict(license_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


