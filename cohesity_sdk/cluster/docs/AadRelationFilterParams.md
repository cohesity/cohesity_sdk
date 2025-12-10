# AadRelationFilterParams

Determines filter that can be applied for a Aad node edge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation_type** | **str** | Filters the edges which matches with specified node relation type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aad_relation_filter_params import AadRelationFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of AadRelationFilterParams from a JSON string
aad_relation_filter_params_instance = AadRelationFilterParams.from_json(json)
# print the JSON string representation of the object
print(AadRelationFilterParams.to_json())

# convert the object into a dict
aad_relation_filter_params_dict = aad_relation_filter_params_instance.to_dict()
# create an instance of AadRelationFilterParams from a dict
aad_relation_filter_params_from_dict = AadRelationFilterParams.from_dict(aad_relation_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


