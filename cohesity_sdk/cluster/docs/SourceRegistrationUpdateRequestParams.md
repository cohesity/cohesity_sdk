# SourceRegistrationUpdateRequestParams

Specifies the Source registration Update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**async_registration** | **bool** | Indicates whether the source should be registered asynchronously. Currently supported only for VMware sources. | [optional] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**data_source_connection_id** | **str** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. Also, this is the &#39;string&#39; of connectionId. This property was added to accommodate for ID values that exceed 2^53 - 1, which is the max value for which JS maintains precision. | [optional] 
**encryption_key** | **str** | Specifies the key that user has encrypted the credential with. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | 
**is_internal_encrypted** | **bool** | Specifies if credentials are encrypted by internal key. | [optional] 
**name** | **str** | A user specified name for this source. | [optional] 
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
**last_modified_timestamp_usecs** | **int** | Specifies the last time this protection source was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the protection source was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error. | [optional] 
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

## Example

```python
from cohesity_sdk.cluster.models.source_registration_update_request_params import SourceRegistrationUpdateRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRegistrationUpdateRequestParams from a JSON string
source_registration_update_request_params_instance = SourceRegistrationUpdateRequestParams.from_json(json)
# print the JSON string representation of the object
print(SourceRegistrationUpdateRequestParams.to_json())

# convert the object into a dict
source_registration_update_request_params_dict = source_registration_update_request_params_instance.to_dict()
# create an instance of SourceRegistrationUpdateRequestParams from a dict
source_registration_update_request_params_from_dict = SourceRegistrationUpdateRequestParams.from_dict(source_registration_update_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


