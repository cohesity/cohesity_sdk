# EBSTag

A key - value pair tag that may be specified on AWS volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cohesity_sdk.models.ebs_tag import EBSTag

# TODO update the JSON string below
json = "{}"
# create an instance of EBSTag from a JSON string
ebs_tag_instance = EBSTag.from_json(json)
# print the JSON string representation of the object
print(EBSTag.to_json())

# convert the object into a dict
ebs_tag_dict = ebs_tag_instance.to_dict()
# create an instance of EBSTag from a dict
ebs_tag_from_dict = EBSTag.from_dict(ebs_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


