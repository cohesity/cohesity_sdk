# AzureDiskTagParams

Specifies the tag vectors used to exclude Azure Disks attached to Azure instance at global and object level. Contains two vectors: exclusion and inclusion. E.g., {exclusionTagArray: [(K1, V1),  (K2, V2)], inclusionTagArray: [(K3, V3)]} => This will exclude a particular volume iff it has all the tags in exclusionTagArray((K1, V1),  (K2, V2)) and has none of the tags in the inclusionTagArray((K3, V3)).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_tag_array** | [**List[AzureDiskTag]**](AzureDiskTag.md) | Array which contains tags for AND exclusion. E.g., exclusionTagArray: [(K1, V1),  (K2, V2)] &#x3D;&gt; This will exclude a particular volume iff it has both these tags. | [optional] 
**inclusion_tag_array** | [**List[AzureDiskTag]**](AzureDiskTag.md) | Array which contains tags for AND inclusion. E.g., inclusionTagArray: [(K3, V3),  (K4, V4)] &#x3D;&gt; This will exclude a particular volume iff it does not have both these tags. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_disk_tag_params import AzureDiskTagParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDiskTagParams from a JSON string
azure_disk_tag_params_instance = AzureDiskTagParams.from_json(json)
# print the JSON string representation of the object
print(AzureDiskTagParams.to_json())

# convert the object into a dict
azure_disk_tag_params_dict = azure_disk_tag_params_instance.to_dict()
# create an instance of AzureDiskTagParams from a dict
azure_disk_tag_params_from_dict = AzureDiskTagParams.from_dict(azure_disk_tag_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


