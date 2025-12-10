# ClusterOperationAttribute

Name value pair representing an attribute of the operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the attribute. Following attributres are possible. * &#x60;kUpgradePackageName&#x60; - Indicates the name of the package for   operation types is from enum &#x60;cluster_software_operation_type&#x60; that   represent upgrade related operations. * &#x60;kPatchPackageName&#x60; - Indicates the   name of the package for operation types is from enum   &#x60;cluster_software_operation_type&#x60; that represents patch related   operations. * &#x60;kPackageType&#x60; specifies whether operation is related to upgrade   or patch.  This will have values from enum &#x60;cluster_package_type&#x60;. * &#x60;kPackageSubType&#x60; specifies package sub type.  This will have values   from enum &#x60;cluster_package_sub_type&#x60;.  | 
**value** | **str** |  | 

## Example

```python
from cohesity_sdk.cluster.models.cluster_operation_attribute import ClusterOperationAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperationAttribute from a JSON string
cluster_operation_attribute_instance = ClusterOperationAttribute.from_json(json)
# print the JSON string representation of the object
print(ClusterOperationAttribute.to_json())

# convert the object into a dict
cluster_operation_attribute_dict = cluster_operation_attribute_instance.to_dict()
# create an instance of ClusterOperationAttribute from a dict
cluster_operation_attribute_from_dict = ClusterOperationAttribute.from_dict(cluster_operation_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


