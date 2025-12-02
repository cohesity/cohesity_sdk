# TargetSiteParam

Specifies the target Site to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**target_doc_lib_name** | **str** | Specifies the name for the target doc lib. | [optional] 
**target_doc_lib_prefix** | **str** | Specifies the prefix for the target doc lib. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.target_site_param import TargetSiteParam

# TODO update the JSON string below
json = "{}"
# create an instance of TargetSiteParam from a JSON string
target_site_param_instance = TargetSiteParam.from_json(json)
# print the JSON string representation of the object
print(TargetSiteParam.to_json())

# convert the object into a dict
target_site_param_dict = target_site_param_instance.to_dict()
# create an instance of TargetSiteParam from a dict
target_site_param_from_dict = TargetSiteParam.from_dict(target_site_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


