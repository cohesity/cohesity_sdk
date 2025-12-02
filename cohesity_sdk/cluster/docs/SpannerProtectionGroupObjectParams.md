# SpannerProtectionGroupObjectParams

Specifies the object parameters to create Google Spanner Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the database. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.spanner_protection_group_object_params import SpannerProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of SpannerProtectionGroupObjectParams from a JSON string
spanner_protection_group_object_params_instance = SpannerProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(SpannerProtectionGroupObjectParams.to_json())

# convert the object into a dict
spanner_protection_group_object_params_dict = spanner_protection_group_object_params_instance.to_dict()
# create an instance of SpannerProtectionGroupObjectParams from a dict
spanner_protection_group_object_params_from_dict = SpannerProtectionGroupObjectParams.from_dict(spanner_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


