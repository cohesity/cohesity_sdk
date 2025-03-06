# SfdcObjectFieldExclusion

Specifies the field names to be excluded for the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_field_names** | **List[str]** | Specifies the list of Sfdc API names of the fields to be excluded in this object. | [optional] 
**object_id** | **int** | Specifies the id of the object in which some fields are to be excluded. This should be a leaf level object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sfdc_object_field_exclusion import SfdcObjectFieldExclusion

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcObjectFieldExclusion from a JSON string
sfdc_object_field_exclusion_instance = SfdcObjectFieldExclusion.from_json(json)
# print the JSON string representation of the object
print(SfdcObjectFieldExclusion.to_json())

# convert the object into a dict
sfdc_object_field_exclusion_dict = sfdc_object_field_exclusion_instance.to_dict()
# create an instance of SfdcObjectFieldExclusion from a dict
sfdc_object_field_exclusion_from_dict = SfdcObjectFieldExclusion.from_dict(sfdc_object_field_exclusion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


