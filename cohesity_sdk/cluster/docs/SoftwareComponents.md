# SoftwareComponents

List of software components.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**components** | [**List[PackageComponent]**](PackageComponent.md) | List of cluster software components. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.software_components import SoftwareComponents

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareComponents from a JSON string
software_components_instance = SoftwareComponents.from_json(json)
# print the JSON string representation of the object
print(SoftwareComponents.to_json())

# convert the object into a dict
software_components_dict = software_components_instance.to_dict()
# create an instance of SoftwareComponents from a dict
software_components_from_dict = SoftwareComponents.from_dict(software_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


