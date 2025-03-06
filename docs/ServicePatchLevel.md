# ServicePatchLevel

Patch level of a service. It is the number of patches applied for the service on the cluster. If a service is never patched the patch level is 0. If two patches were applied, patch level is 2.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_level** | **int** | Specifies patch level of the service after the patch operation. | [optional] 
**patch_version** | **str** | Specifies the version of the service patch after the patch operation. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**start_level** | **int** | Specifies patch level of the service before the patch operation. | [optional] 
**start_version** | **str** | Specifies the version of the service running on the cluster before the patch operation. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_patch_level import ServicePatchLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePatchLevel from a JSON string
service_patch_level_instance = ServicePatchLevel.from_json(json)
# print the JSON string representation of the object
print(ServicePatchLevel.to_json())

# convert the object into a dict
service_patch_level_dict = service_patch_level_instance.to_dict()
# create an instance of ServicePatchLevel from a dict
service_patch_level_from_dict = ServicePatchLevel.from_dict(service_patch_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


