# SfdcDependentObject

Specifies dependent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of an object | 
**name** | **str** | Name of an object | 

## Example

```python
from cohesity_sdk.cluster.models.sfdc_dependent_object import SfdcDependentObject

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcDependentObject from a JSON string
sfdc_dependent_object_instance = SfdcDependentObject.from_json(json)
# print the JSON string representation of the object
print(SfdcDependentObject.to_json())

# convert the object into a dict
sfdc_dependent_object_dict = sfdc_dependent_object_instance.to_dict()
# create an instance of SfdcDependentObject from a dict
sfdc_dependent_object_from_dict = SfdcDependentObject.from_dict(sfdc_dependent_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


