# RecoverRDSPostgresToKnownSourceConfig

Specifies the configuration for recovering RDS Postgres instance to the known target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the instance in which to deploy the Rds instance. | [optional] 
**recover_to_new_source** | **bool, none_type** | Specifies the parameter whether the recovery should be performed to a new target. | [optional] 
**region** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the AWS region in which to deploy the Rds instance. | [optional] 
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the target source details where RDS Postgres database will be recovered. This source id should be a RDS Postgres target instance id were databases could be restored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


