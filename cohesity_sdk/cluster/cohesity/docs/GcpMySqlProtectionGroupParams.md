# GcpMySqlProtectionGroupParams

Specifies the parameters which are specific to Google MySQL related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_mysql_tag_ids** | **[[int]], none_type** | Array of arrays of MySQL Tag Ids that specify db instances to Exclude. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**mysql_tag_ids** | **[[int]], none_type** | Array of arrays of MySQL Tag Ids that specify db instances to Protect. | [optional] 
**objects** | [**[GcpMySqlProtectionGroupObjectParams]**](GcpMySqlProtectionGroupObjectParams.md) | Specifies the MySQL databases to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


