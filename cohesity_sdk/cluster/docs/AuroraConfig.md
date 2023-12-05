# AuroraConfig

Specifies the parameters to recover AWS Aurora.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_instance_id** | **str, none_type** | Specifies the DB instance identifier to use for the restored DB. | 
**db_port** | **int, none_type** | Specifies the port to use for the DB in the restored Aurora instance. | 
**enable_auto_minor_version_upgrade** | **bool, none_type** | Specifies whether to enable auto minor version upgrade in the restored DB. | 
**enable_copy_tags_to_snapshots** | **bool, none_type** | Specifies whether to enable copying of tags to snapshots of the DB. | 
**enable_iam_db_authentication** | **bool, none_type** | Specifies whether to enable IAM authentication for the DB. | 
**is_multi_az_deployment** | **bool, none_type** | Specifies whether this is a multi-az deployment or not. | 
**db_option_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies entity representing the Aurora option group to use while restoring the DB. | [optional] 
**db_parameter_group** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the entity representing the Aurora parameter group to use while restoring the DB. | [optional] 
**enable_public_accessibility** | **bool, none_type** | Specifies whether this DB will be publicly accessible or not. | [optional] 
**point_in_time_usecs** | **int, none_type** | Specifies a point in time for recovery in microseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


