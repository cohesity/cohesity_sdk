# AssessSoftwareUpdateParams

Specifies parameters to assess cluster state for the software update (upgrade/patch).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_type** | **str** | Type of software package. | 
**phase** | **str** | Specifies the phase of software update. | 
**version_name** | **str** | Version name of the package. | 

## Example

```python
from cohesity_sdk.cluster.models.assess_software_update_params import AssessSoftwareUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of AssessSoftwareUpdateParams from a JSON string
assess_software_update_params_instance = AssessSoftwareUpdateParams.from_json(json)
# print the JSON string representation of the object
print(AssessSoftwareUpdateParams.to_json())

# convert the object into a dict
assess_software_update_params_dict = assess_software_update_params_instance.to_dict()
# create an instance of AssessSoftwareUpdateParams from a dict
assess_software_update_params_from_dict = AssessSoftwareUpdateParams.from_dict(assess_software_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


