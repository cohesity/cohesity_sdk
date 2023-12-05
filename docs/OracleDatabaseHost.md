# OracleDatabaseHost

Specifies details about an Oracle database host.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_count** | **int** | Specifies the number of channels to be created for this host. Default value for the number of channels will be calculated as the minimum of number of nodes in Cohesity cluster and 2 * number of CPU on the host. | [optional] 
**host_id** | **str, none_type** | Specifies the id of the database host from which backup is allowed. | [optional] 
**port** | **int** | Specifies the port where the Database is listening. | [optional] 
**sbt_host_params** | [**OracleSbtHostParams**](OracleSbtHostParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


