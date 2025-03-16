# McmObjectIdentifier

Specifies the object identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**object_id** | **int** | Specifies the object id. | 
**region_id** | **str** | Specifies the region id. Applicable only in case of DMaaS. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_identifier import McmObjectIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectIdentifier from a JSON string
mcm_object_identifier_instance = McmObjectIdentifier.from_json(json)
# print the JSON string representation of the object
print(McmObjectIdentifier.to_json())

# convert the object into a dict
mcm_object_identifier_dict = mcm_object_identifier_instance.to_dict()
# create an instance of McmObjectIdentifier from a dict
mcm_object_identifier_from_dict = McmObjectIdentifier.from_dict(mcm_object_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


