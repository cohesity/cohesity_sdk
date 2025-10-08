# SourceRegistrationUpdateRequestParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**AwsSourceRegistrationParams**](AwsSourceRegistrationParams.md) |  | [optional] 
**azure_params** | [**AzureSourceRegistrationParams**](AzureSourceRegistrationParams.md) |  | [optional] 
**cassandra_params** | [**CassandraSourceRegistrationParams**](CassandraSourceRegistrationParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSourceRegistrationParams**](CouchbaseSourceRegistrationParams.md) |  | [optional] 
**db2_params** | [**DB2SourceRegistrationParams**](DB2SourceRegistrationParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileRegistrationParams**](ElastifileRegistrationParams.md) |  | [optional] 
**ews_exchange_params** | [**EwsExchangeSourceRegistrationParams**](EwsExchangeSourceRegistrationParams.md) |  | [optional] 
**experimental_adapter_params** | [**ExperimentalAdapterSourceRegistrationParams**](ExperimentalAdapterSourceRegistrationParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeRegistrationParams**](FlashbladeRegistrationParams.md) |  | [optional] 
**gcp_params** | [**GcpSourceRegistrationParams**](GcpSourceRegistrationParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasRegistrationParams**](GenericNasRegistrationParams.md) |  | [optional] 
**google_workspace_params** | [**GoogleWorkspaceSourceRegistrationParams**](GoogleWorkspaceSourceRegistrationParams.md) |  | [optional] 
**gpfs_params** | [**GpfsRegistrationParams**](GpfsRegistrationParams.md) |  | [optional] 
**hbase_params** | [**HbaseSourceRegistrationParams**](HbaseSourceRegistrationParams.md) |  | [optional] 
**hdfs_params** | [**HdfsSourceRegistrationParams**](HdfsSourceRegistrationParams.md) |  | [optional] 
**hive_params** | [**HiveSourceRegistrationParams**](HiveSourceRegistrationParams.md) |  | [optional] 
**hyperv_params** | [**HyperVSourceRegistrationParams**](HyperVSourceRegistrationParams.md) |  | [optional] 
**isilon_params** | [**IsilonRegistrationParams**](IsilonRegistrationParams.md) |  | [optional] 
**kubernetes_params** | [**KubernetesSourceRegistrationParams**](KubernetesSourceRegistrationParams.md) |  | [optional] 
**last_modified_timestamp_usecs** | **int, none_type** | Specifies the last time this protection source was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the protection source was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error. | [optional] 
**mongodb_ops_params** | [**MongoDBOpsManagerRegistrationParams**](MongoDBOpsManagerRegistrationParams.md) |  | [optional] 
**mongodb_params** | [**MongoDBSourceRegistrationParams**](MongoDBSourceRegistrationParams.md) |  | [optional] 
**netapp_params** | [**NetappRegistrationParams**](NetappRegistrationParams.md) |  | [optional] 
**office365_params** | [**Office365SourceRegistrationParams**](Office365SourceRegistrationParams.md) |  | [optional] 
**physical_params** | [**PhysicalSourceRegistrationParams**](PhysicalSourceRegistrationParams.md) |  | [optional] 
**s3_compatible_params** | [**S3CompatibleSourceRegistrationParams**](S3CompatibleSourceRegistrationParams.md) |  | [optional] 
**sap_hana_params** | [**SapHanaSourceRegistrationParams**](SapHanaSourceRegistrationParams.md) |  | [optional] 
**service_now_params** | [**ServiceNowSourceRegistrationParams**](ServiceNowSourceRegistrationParams.md) |  | [optional] 
**sfdc_params** | [**SfdcSourceRegistrationParams**](SfdcSourceRegistrationParams.md) |  | [optional] 
**uda_params** | [**UdaSourceRegistrationParams**](UdaSourceRegistrationParams.md) |  | [optional] 
**vmware_params** | [**VmwareSourceRegistrationParams**](VmwareSourceRegistrationParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


