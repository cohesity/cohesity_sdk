# PatchDetail

Detail of a patch. It gives the service and version information of the the patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Specifies the user friendly name of the service. | [optional] 
**import_version** | **str** | Specifies the version of the imported service patch. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**status** | **str** | Specifies the status of the patch whether it is accepted or rejected. A patch is rejected if it is older than the version available or applied on the cluster. | [optional] 
**version** | **str** | Specifies the existing version of the service. This is the available service patch version if exists. If there is no patch available, then it is the applied patch version if applied. If both don&#39;t exist, it is the base version of the service. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.patch_detail import PatchDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDetail from a JSON string
patch_detail_instance = PatchDetail.from_json(json)
# print the JSON string representation of the object
print(PatchDetail.to_json())

# convert the object into a dict
patch_detail_dict = patch_detail_instance.to_dict()
# create an instance of PatchDetail from a dict
patch_detail_from_dict = PatchDetail.from_dict(patch_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


