# AzureDiskExclusionParams

Specifies parameters to exclude Azure Disks attached to Azure VM at job or object level. A disk satisfying any of this criteria will be excluded from the backup job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_ids** | **List[str]** | Array of disk ids to be excluded during backup. This is only used at object level exclusion. | [optional] 
**raw_query** | **str** | Raw boolean query given as input by the user to exclude volume based on tags. In the current version, the query contains only tags. Eg. query 1 - \&quot;K1\&quot; &#x3D; \&quot;V1\&quot; AND \&quot;K2\&quot; IN (\&quot;V2\&quot;, \&quot;V3\&quot;) AND \&quot;K4\&quot; !&#x3D; \&quot;V4\&quot; Eg. query 2 - \&quot;K1\&quot; !&#x3D; \&quot;V1\&quot; OR \&quot;K2\&quot; NOT IN (\&quot;V2\&quot;, \&quot;V3\&quot;) OR \&quot;K4\&quot; &#x3D; \&quot;V4\&quot; All Keys and Values must be wrapped inside double quotes. Comparision Operators supported - IN, NOT IN, &#x3D;, !&#x3D;. Logical Operators supported - AND, OR. We cannot have AND, OR together in the query. Only one of them is allowed. The processed form for this query is stored in the above tagParamsArray. | [optional] 
**tag_params_array** | [**List[AzureDiskTagParams]**](AzureDiskTagParams.md) | Array of TagParams objects. Each TagParams object consists of two vectors: for exclusion and inclusion. Each TagPararms object is present as an ORed item. User can only input queries of form: (&lt;&gt; AND &lt;&gt; AND &lt;&gt; ..) OR (&lt;&gt; AND &lt;&gt; AND &lt;&gt; ..) OR (..) OR (..) OR .. There cannot be an OR operator inside the bracket. Example query: (K1 &#x3D; V1 AND K2 &#x3D; V2 AND K3 !&#x3D; V3) OR (K4 &#x3D; V4 AND K6 !&#x3D; V6). This will lead to formation of two items in tagParamsArray. First item: {exclusionTagArray: [(K1, V1),  (K2, V2)], inclusionTagArray: [(K3, V3)]} Second item: {exclusionTagArray: [(K4, V4)], inclusionTagArray: [(K6, V6)]}. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_disk_exclusion_params import AzureDiskExclusionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDiskExclusionParams from a JSON string
azure_disk_exclusion_params_instance = AzureDiskExclusionParams.from_json(json)
# print the JSON string representation of the object
print(AzureDiskExclusionParams.to_json())

# convert the object into a dict
azure_disk_exclusion_params_dict = azure_disk_exclusion_params_instance.to_dict()
# create an instance of AzureDiskExclusionParams from a dict
azure_disk_exclusion_params_from_dict = AzureDiskExclusionParams.from_dict(azure_disk_exclusion_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


