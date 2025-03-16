# CreateRecoveryRequest

Specifies the request parameters to create a Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the Recovery. | 
**snapshot_environment** | **str** | Specifies the type of environment of snapshots for which the Recovery has to be performed. | 
**acropolis_params** | [**RecoverAcropolisParams**](RecoverAcropolisParams.md) |  | [optional] 
**aws_params** | [**RecoverAwsParams**](RecoverAwsParams.md) |  | [optional] 
**azure_params** | [**RecoverAzureParams**](RecoverAzureParams.md) |  | [optional] 
**cassandra_params** | [**CassandraParams**](CassandraParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseParams**](CouchbaseParams.md) |  | [optional] 
**elastifile_params** | [**RecoverElastifileParams**](RecoverElastifileParams.md) |  | [optional] 
**exchange_params** | [**RecoverExchangeParams**](RecoverExchangeParams.md) |  | [optional] 
**flashblade_params** | [**RecoverFlashbladeParams**](RecoverFlashbladeParams.md) |  | [optional] 
**gcp_params** | [**RecoverGcpParams**](RecoverGcpParams.md) |  | [optional] 
**generic_nas_params** | [**RecoverGenericNasParams**](RecoverGenericNasParams.md) |  | [optional] 
**gpfs_params** | [**RecoverGpfsParams**](RecoverGpfsParams.md) |  | [optional] 
**hbase_params** | [**HbaseParams**](HbaseParams.md) |  | [optional] 
**hdfs_params** | [**HdfsParams**](HdfsParams.md) |  | [optional] 
**hive_params** | [**HiveParams**](HiveParams.md) |  | [optional] 
**hyperv_params** | [**RecoverHyperVParams**](RecoverHyperVParams.md) |  | [optional] 
**ibm_flash_system_params** | [**RecoverPureParams**](RecoverPureParams.md) |  | [optional] 
**isilon_params** | [**RecoverIsilonParams**](RecoverIsilonParams.md) |  | [optional] 
**kubernetes_params** | [**RecoverKubernetesParams**](RecoverKubernetesParams.md) |  | [optional] 
**kvm_params** | [**RecoverKvmParams**](RecoverKvmParams.md) |  | [optional] 
**mongodb_params** | [**MongodbParams**](MongodbParams.md) |  | [optional] 
**mssql_params** | [**RecoverSqlParams**](RecoverSqlParams.md) |  | [optional] 
**netapp_params** | [**RecoverNetappParams**](RecoverNetappParams.md) |  | [optional] 
**office365_params** | [**RecoverO365Params**](RecoverO365Params.md) |  | [optional] 
**oracle_params** | [**RecoverOracleParams**](RecoverOracleParams.md) |  | [optional] 
**physical_params** | [**RecoverPhysicalParams**](RecoverPhysicalParams.md) |  | [optional] 
**pure_params** | [**RecoverPureParams**](RecoverPureParams.md) |  | [optional] 
**sfdc_params** | [**RecoverSalesforceParams**](RecoverSalesforceParams.md) |  | [optional] 
**uda_params** | [**UdaParams**](UdaParams.md) |  | [optional] 
**view_params** | [**RecoverViewParams**](RecoverViewParams.md) |  | [optional] 
**vmware_params** | [**RecoverVmwareParams**](RecoverVmwareParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_recovery_request import CreateRecoveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecoveryRequest from a JSON string
create_recovery_request_instance = CreateRecoveryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRecoveryRequest.to_json())

# convert the object into a dict
create_recovery_request_dict = create_recovery_request_instance.to_dict()
# create an instance of CreateRecoveryRequest from a dict
create_recovery_request_from_dict = CreateRecoveryRequest.from_dict(create_recovery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


