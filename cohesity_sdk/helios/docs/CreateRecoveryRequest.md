# CreateRecoveryRequest

Specifies the request parameters to create a Recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Recovery. | 
**snapshot_environment** | **str** | Specifies the type of environment of snapshots for which the Recovery has to be performed. | 
**vmware_params** | [**RecoverVmwareParams**](RecoverVmwareParams.md) |  | [optional] 
**aws_params** | [**RecoverAwsParams**](RecoverAwsParams.md) |  | [optional] 
**gcp_params** | [**RecoverGcpParams**](RecoverGcpParams.md) |  | [optional] 
**azure_params** | [**RecoverAzureParams**](RecoverAzureParams.md) |  | [optional] 
**kvm_params** | [**RecoverKvmParams**](RecoverKvmParams.md) |  | [optional] 
**acropolis_params** | [**RecoverAcropolisParams**](RecoverAcropolisParams.md) |  | [optional] 
**mssql_params** | [**RecoverSqlParams**](RecoverSqlParams.md) |  | [optional] 
**netapp_params** | [**RecoverNetappParams**](RecoverNetappParams.md) |  | [optional] 
**generic_nas_params** | [**RecoverGenericNasParams**](RecoverGenericNasParams.md) |  | [optional] 
**isilon_params** | [**RecoverIsilonParams**](RecoverIsilonParams.md) |  | [optional] 
**flashblade_params** | [**RecoverFlashbladeParams**](RecoverFlashbladeParams.md) |  | [optional] 
**elastifile_params** | [**RecoverElastifileParams**](RecoverElastifileParams.md) |  | [optional] 
**gpfs_params** | [**RecoverGpfsParams**](RecoverGpfsParams.md) |  | [optional] 
**physical_params** | [**RecoverPhysicalParams**](RecoverPhysicalParams.md) |  | [optional] 
**hyperv_params** | [**RecoverHyperVParams**](RecoverHyperVParams.md) |  | [optional] 
**exchange_params** | [**RecoverExchangeParams**](RecoverExchangeParams.md) |  | [optional] 
**cassandra_params** | [**CassandraParams**](CassandraParams.md) |  | [optional] 
**uda_params** | [**UdaParams**](UdaParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseParams**](CouchbaseParams.md) |  | [optional] 
**hbase_params** | [**HbaseParams**](HbaseParams.md) |  | [optional] 
**hdfs_params** | [**HdfsParams**](HdfsParams.md) |  | [optional] 
**hive_params** | [**HiveParams**](HiveParams.md) |  | [optional] 
**mongodb_params** | [**MongodbParams**](MongodbParams.md) |  | [optional] 
**pure_params** | [**RecoverPureParams**](RecoverPureParams.md) |  | [optional] 
**kubernetes_params** | [**RecoverKubernetesParams**](RecoverKubernetesParams.md) |  | [optional] 
**office365_params** | [**RecoverO365Params**](RecoverO365Params.md) |  | [optional] 
**oracle_params** | [**RecoverOracleParams**](RecoverOracleParams.md) |  | [optional] 
**sfdc_params** | [**RecoverSalesforceParams**](RecoverSalesforceParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


