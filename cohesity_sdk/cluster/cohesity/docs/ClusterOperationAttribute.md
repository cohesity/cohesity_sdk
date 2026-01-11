# ClusterOperationAttribute

Name value pair representing an attribute of the operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the attribute. Following attributres are possible. * &#x60;kUpgradePackageName&#x60; - Indicates the name of the package for   operation types is from enum &#x60;cluster_software_operation_type&#x60; that   represent upgrade related operations. * &#x60;kPatchPackageName&#x60; - Indicates the   name of the package for operation types is from enum   &#x60;cluster_software_operation_type&#x60; that represents patch related   operations. * &#x60;kPackageType&#x60; specifies whether operation is related to upgrade   or patch.  This will have values from enum &#x60;cluster_package_type&#x60;. * &#x60;kPackageSubType&#x60; specifies package sub type.  This will have values   from enum &#x60;cluster_package_sub_type&#x60;.  | 
**value** | **str** |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


