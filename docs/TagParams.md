# TagParams

Specifies the tag vectors used to exclude EBS volumes attached to EC2 instances at global and object level. Contains two vectors: exclusion and inclusion. E.g., {exclusionTagArray: [(K1, V1),  (K2, V2)], inclusionTagArray: [(K3, V3)]} => This will exclude a particular volume iff it has all the tags in exclusionTagArray((K1, V1),  (K2, V2)) and has none of the tags in the inclusionTagArray((K3, V3)).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_tag_array** | [**List[EBSTag]**](EBSTag.md) | Array which contains tags for AND exclusion. E.g., exclusionTagArray: [(K1, V1),  (K2, V2)] &#x3D;&gt; This will exclude a particular volume iff it has both these tags. | [optional] 
**inclusion_tag_array** | [**List[EBSTag]**](EBSTag.md) | Array which contains tags for AND inclusion. E.g., inclusionTagArray: [(K3, V3),  (K4, V4)] &#x3D;&gt; This will exclude a particular volume iff it does not have both these tags. | [optional] 

## Example

```python
from cohesity_sdk.models.tag_params import TagParams

# TODO update the JSON string below
json = "{}"
# create an instance of TagParams from a JSON string
tag_params_instance = TagParams.from_json(json)
# print the JSON string representation of the object
print(TagParams.to_json())

# convert the object into a dict
tag_params_dict = tag_params_instance.to_dict()
# create an instance of TagParams from a dict
tag_params_from_dict = TagParams.from_dict(tag_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


