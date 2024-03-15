# AwsTargetParamsForRecoverRDSPostgres

Specifies the recovery target params for RDS Postgres target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_known_source** | **bool, none_type** | Specifies whether the recovery should be performed to a known or a custom target. | 
**custom_server_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the custom destination Server configuration parameters where the RDS Postgres instances will be recovered. | [optional] 
**known_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the destination Source configuration parameters where the RDS Postgres instances will be recovered. This is mandatory if recoverToKnownSource is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


