# PackageComponent

\"Software upgrade sub package. Aplicable for one helios package\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** | Name of sub package | 
**release** | **str** | Release Version of sub package. | 
**version** | **str** | Version of sub package. | 

## Example

```python
from cohesity_sdk.cluster.models.package_component import PackageComponent

# TODO update the JSON string below
json = "{}"
# create an instance of PackageComponent from a JSON string
package_component_instance = PackageComponent.from_json(json)
# print the JSON string representation of the object
print(PackageComponent.to_json())

# convert the object into a dict
package_component_dict = package_component_instance.to_dict()
# create an instance of PackageComponent from a dict
package_component_from_dict = PackageComponent.from_dict(package_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


