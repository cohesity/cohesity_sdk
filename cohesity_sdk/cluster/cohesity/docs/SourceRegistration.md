# SourceRegistration

Specifies the Source Registration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be deprecated in future. Use connections field. | [optional] 
**connections** | [**[ConnectionConfig], none_type**](ConnectionConfig.md) | Specifies the list of connections for the source. | [optional] 
**connector_group_id** | **int, none_type** | Specifies the connector group id of connector groups. | [optional] 
**data_source_connection_id** | **str, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. Also, this is the &#39;string&#39; of connectionId. This property was added to accommodate for ID values that exceed 2^53 - 1, which is the max value for which JS maintains precision. | [optional] 
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | [optional] 
**id** | **int, none_type** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**name** | **str, none_type** | The user specified name for this source. | [optional] 
**source_id** | **int, none_type** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**source_info** | [**Object**](Object.md) |  | [optional] 
**authentication_status** | **str, none_type** | Specifies the status of the authentication during the registration of a Protection Source. &#39;Pending&#39; indicates the authentication is in progress. &#39;Scheduled&#39; indicates the authentication is scheduled. &#39;Finished&#39; indicates the authentication is completed. &#39;RefreshInProgress&#39; indicates the refresh is in progress. | [optional] [readonly] 
**last_refreshed_time_msecs** | **int, none_type** | Specifies the time when the source was last refreshed in milliseconds. | [optional] [readonly] 
**registration_time_msecs** | **int, none_type** | Specifies the time when the source was registered in milliseconds | [optional] [readonly] 
**aws_params** | [**AwsSourceRegistrationParams**](AwsSourceRegistrationParams.md) |  | [optional] 
**azure_params** | [**AzureSourceRegistrationParams**](AzureSourceRegistrationParams.md) |  | [optional] 
**cassandra_params** | [**CassandraSourceRegistrationParams**](CassandraSourceRegistrationParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSourceRegistrationParams**](CouchbaseSourceRegistrationParams.md) |  | [optional] 
**db2_params** | [**DB2SourceRegistrationParams**](DB2SourceRegistrationParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileRegistrationParams**](ElastifileRegistrationParams.md) |  | [optional] 
**ews_exchange_params** | [**EwsExchangeSourceRegistrationParams**](EwsExchangeSourceRegistrationParams.md) |  | [optional] 
**experimental_adapter_params** | [**ExperimentalAdapterSourceRegistrationParams**](ExperimentalAdapterSourceRegistrationParams.md) |  | [optional] 
**external_metadata** | [**EntityExternalMetadata**](EntityExternalMetadata.md) |  | [optional] 
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
**mongodb_ops_params** | [**MongoDBOpsManagerRegistrationParams**](MongoDBOpsManagerRegistrationParams.md) |  | [optional] 
**mongodb_params** | [**MongoDBSourceRegistrationParams**](MongoDBSourceRegistrationParams.md) |  | [optional] 
**netapp_params** | [**NetappRegistrationParams**](NetappRegistrationParams.md) |  | [optional] 
**nutanix_fs_params** | [**NutanixFSRegistrationParams**](NutanixFSRegistrationParams.md) |  | [optional] 
**office365_params** | [**Office365SourceRegistrationParams**](Office365SourceRegistrationParams.md) |  | [optional] 
**physical_params** | [**PhysicalSourceRegistrationParams**](PhysicalSourceRegistrationParams.md) |  | [optional] 
**postgres_params** | [**PostgresSourceRegistrationParams**](PostgresSourceRegistrationParams.md) |  | [optional] 
**s3_compatible_params** | [**S3CompatibleSourceRegistrationParams**](S3CompatibleSourceRegistrationParams.md) |  | [optional] 
**sap_hana_params** | [**SapHanaSourceRegistrationParams**](SapHanaSourceRegistrationParams.md) |  | [optional] 
**service_now_params** | [**ServiceNowSourceRegistrationParams**](ServiceNowSourceRegistrationParams.md) |  | [optional] 
**sfdc_params** | [**SfdcSourceRegistrationParams**](SfdcSourceRegistrationParams.md) |  | [optional] 
**uda_params** | [**UdaSourceRegistrationParams**](UdaSourceRegistrationParams.md) |  | [optional] 
**vmware_params** | [**VmwareSourceRegistrationParams**](VmwareSourceRegistrationParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


